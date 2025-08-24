import requests
from django.db import transaction
from django.shortcuts import render, redirect

from mailapp.models import *
from mailapp.utils import *
from userapp.models import Member


class Google():
    @classmethod
    def get_auth_param(cls, request):
        return {
            "code"          : request.GET.get("code"),
            "client_id"     : settings.GOOGLE_CLIENT_ID,
            "client_secret" : settings.GOOGLE_CLIENT_SECRET,
            "redirect_uri"  : f"http://{request.get_host()}/user/sns_login/google",
            "grant_type"    : "authorization_code",
        }

    @classmethod
    def get_access_token(cls, params):
        _url     = "https://oauth2.googleapis.com/token"
        _headers = {"Content-Type" : "application/x-www-form-urlencoded"}

        response = requests.post(_url, params, headers=_headers)
        response.raise_for_status()  # HTTP 오류 발생 시 예외 발생

        data     = response.json()
        token    = data.get('access_token')
        return token

    """
    -> SNS 로그인	-> 계정 존재	-> 인증한 사람이면		-> 메인페이지
                                    -> 인증 안한 사람이면	-> 로그인 페이지로.
                    -> 없는 계정	-> 회원가입시키고 -> 인증메일 발송
    """
    @transaction.atomic
    @classmethod
    def login(cls, request):
        params   = Google.get_auth_param(request)
        token    = Google.get_access_token(params)
        headers  = {'Authorization': f'Bearer {token}'}

        response = requests.get('https://www.googleapis.com/oauth2/v3/userinfo', headers=headers)
        response.raise_for_status()

        data     = response.json()
        email    = data.get("email")

        if User.objects.filter(username=email).exists():
            login_user = User.objects.get(username=email)
            sns_type   = login_user.member.sns_type
            if sns_type != "google":
                return render(request, "layout/redirect.html", {"redirect":reverse("userapp:login"), "msg":"로그인하실 계정종류를 확인해주세요."})

            # is_authed  = login_user.auth.order_by("-created_at").first().is_authed()
            is_authed  = login_user.member.is_authed()
            if is_authed: return redirect("mainapp:index")
            else:         return render(request, "layout/redirect.html", {"redirect":reverse("userapp:login"), "msg":"가입하신 메일에서 본인인증을 완료해주세요."})
        else:
            new_user   = Member.add_new_user(email, data.get("given_name"), data.get("family_name"))
            new_member = Member.add_new_member(new_user, "google", data.get("picture"))
            LoginAuth.send_auth_mail(request, new_member.user)
            return render(request, "layout/redirect.html", {"redirect":reverse("userapp:login"), "msg":"가입하신 이메일로 본인인증을 위한 메일이 발송되었습니다."})
