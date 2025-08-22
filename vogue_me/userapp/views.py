import json

import requests
from django.conf import settings
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from mailapp.models import *
from mailapp.utils import *
from .models import RegisterUserForm


# Create your views here.

def login(request):
    if request.method == "POST":
        pass
    else:
        pass

    return render(request, "app/userapp/login.html", {
        "GOOGLE_CLIENT_ID"  : settings.GOOGLE_CLIENT_ID,
    })

def sns_login(request, provider):
    if provider == "google":
        params = {
            "code"          : request.GET.get("code"),
            "client_id"     : settings.GOOGLE_CLIENT_ID,
            "client_secret" : settings.GOOGLE_CLIENT_SECRET,
            "redirect_uri"  : f"http://{request.get_host()}/user/sns_login/google",
            "grant_type"    : "authorization_code",
        }
        token_response = requests.post("https://oauth2.googleapis.com/token", headers={"Content-Type" : "application/x-www-form-urlencoded"}, data=params)
        token_response.raise_for_status()  # HTTP 오류 발생 시 예외 발생
        token_data = token_response.json()
        access_token = token_data.get('access_token')

        headers = {'Authorization': f'Bearer {access_token}'}

        user_info_response = requests.get('https://www.googleapis.com/oauth2/v3/userinfo', headers=headers)
        user_info_response.raise_for_status()
        user_info = user_info_response.json()

        email = user_info.get('email')
        name = user_info.get('name', '')
        print(email, name)

        # if User.objects.filter(email=email).exists():

    return HttpResponse("sns login done")

def pick_style(request):
    return render(request, "app/userapp/pick_style.html")


def signup(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data["username"]).exists():
                form.add_error("email", "이미 가입된 계정입니다.")
            else:
                user = form.save()
                new_auth = LoginAuth()
                new_auth.user = user
                new_auth.save()
                context = {
                    "auth_link" : "http://"+request.META['HTTP_HOST'] + reverse('userapp:verify_auth_link', kwargs={"encrypted_code" : new_auth.get_encrypted_code()}),
                    "due_time" : new_auth.expires_at.strftime("%Y.%m.%d %H:%M:%S")
                }
                send_mail_with(user.email, "회원가입 본인인증", MailForm.AUTH_LINK, context)
    else:
        form = RegisterUserForm()

    return render(request, "app/userapp/signup.html", {"form":form})

def check_email_dup(request):
    if request.method == "GET": return redirect("mainapp:index")

    data = json.loads(request.body.decode('utf-8'))
    email = data.get("email")
    return JsonResponse({ "already_exist" : User.objects.filter(email=email).exists() })


def verify_auth_link(request, encrypted_code):
    print("code = ", encrypted_code)
    return redirect("userapp:login")
