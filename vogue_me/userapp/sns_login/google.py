from django.db import transaction

from mailapp.models import *
from mailapp.utils import *
from .sns_login import SnsLogin


class Google(SnsLogin):
    def __init__(self):
        super().__init__("google", settings.GOOGLE_CLIENT_ID, settings.GOOGLE_CLIENT_SECRET)
        self.token_url    = "https://oauth2.googleapis.com/token"
        self.userinfo_url = "https://www.googleapis.com/oauth2/v3/userinfo"

    """
    -> SNS 로그인	-> 계정 존재	-> 인증한 사람이면		-> 메인페이지
                                    -> 인증 안한 사람이면	-> 로그인 페이지로.
                    -> 없는 계정	-> 회원가입시키고 -> 인증메일 발송
    """
    @transaction.atomic
    def login(self, request):
        params   = self.get_auth_params(request)
        token    = self.get_access_token(self.token_url, params)
        headers  = {'Authorization': f'Bearer {token}'}

        data     = self.get_json_response(self.userinfo_url, headers=headers)
        email    = data.get("email")
        info     = {
            "email"      : email,
            "first_name" : data.get("given_name"),
            "last_name"  : data.get("family_name"),
            "photo_url"  : data.get("picture"),
        }
        user_exist = User.objects.filter(username=email).exists()

        if user_exist:  return self.run_when_user_exist(request, email)
        else:           return self.run_when_user_not_exist(request, **info)
