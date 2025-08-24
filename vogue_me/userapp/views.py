import json

from django.db import transaction
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from mailapp.models import *
from .models import RegisterUserForm, Member
from .sns_login.google import Google


def sns_login(request, provider):
    if provider == "google":
        return Google.login(request)

    return HttpResponse("sns login done")

def pick_style(request):
    return render(request, "app/userapp/pick_style.html")

@transaction.atomic
def signup(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data["username"]).exists():
                form.add_error("email", "이미 가입된 계정입니다.")
            else:
                user = form.save()
                LoginAuth.send_auth_mail(request, user)
                Member.add_new_member(user=user, sns_type="email")
                return render(request, "layout/redirect.html", {"redirect":reverse("userapp:login"), "msg":"가입하신 이메일로 본인인증을 위한 메일이 발송되었습니다."})
    else:
        form = RegisterUserForm()

    return render(request, "app/userapp/signup.html", {"form":form})

def check_email_dup(request):
    if request.method == "GET": return redirect("mainapp:index")

    data = json.loads(request.body.decode('utf-8'))
    email = data.get("email")
    return JsonResponse({ "already_exist" : User.objects.filter(email=email).exists() })


def verify_auth_link(request, user_id, encrypted_code):
    if not User.objects.filter(id=user_id).exists():
        return render(request, "layout/redirect.html", {"redirect":":BACK", "msg":"본인인증 주소를 확인해주세요."})

    user = User.objects.get(id=user_id)
    auth = user.auth.order_by("-created_at").first()
    if not auth:
        return render(request, "layout/redirect.html", {"redirect":":BACK", "msg":"본인인증 주소를 확인해주세요."})

    if auth.is_authed():
        return render(request, "layout/redirect.html", {"redirect":":BACK", "msg":"인증이 완료된 링크입니다."})

    if auth.is_expired():
        LoginAuth.send_auth_mail(request, user)
        return render(request, "layout/redirect.html", {"redirect":":BACK", "msg":"인증기간이 만료되어, 신규 본인인증메일을 발송하였습니다.\\r\\n새로운 본인인증메일에서 다시 시도해주세요."})

    if auth.is_valid(encrypted_code):
        return render(request, "layout/redirect.html", {"redirect":reverse("mainapp:index"), "msg":"본인인증이 완료되었습니다."})
    else:
        return render(request, "layout/redirect.html", {"redirect":":BACK", "msg":"본인인증 주소를 확인해주세요."})
