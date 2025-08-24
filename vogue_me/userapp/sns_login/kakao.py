from django.db import transaction
from django.http import HttpResponse

from mailapp.utils import *
from .sns_login import SnsLogin


class Kakao(SnsLogin):
    def __init__(self):
        super().__init__("kakao", settings.KAKAO_CLIENT_ID, settings.KAKAO_CLIENT_SECRET)
        self.token_url    = "https://kauth.kakao.com/oauth/token"
        self.userinfo_url = "https://kapi.kakao.com/v2/user/me"

    @transaction.atomic
    def login(self, request):
        params   = self.get_auth_params(request)
        token    = self.get_access_token(self.token_url, params)
        headers  = {
            'Authorization': f'Bearer {token}',
            "Content-Type" : "application/x-www-form-urlencoded;charset=utf-8"
        }

        data     = self.get_json_response(self.userinfo_url, headers=headers)
        """
        data={
            'id': 4411795988,
            'connected_at': '2025-08-24T08:44:39Z',
            'properties': {
                'profile_image': 'http://k.kakaocdn.net/dn/7JAOr/btsM4S9rAUB/hKUwu4ann07fNmdFkHI6nk/img_640x640.jpg',
                'thumbnail_image': 'http://k.kakaocdn.net/dn/7JAOr/btsM4S9rAUB/hKUwu4ann07fNmdFkHI6nk/img_110x110.jpg'},
                'kakao_account': {
                    'profile_image_needs_agreement': False,
                    'profile': {
                        'thumbnail_image_url': 'http://k.kakaocdn.net/dn/7JAOr/btsM4S9rAUB/hKUwu4ann07fNmdFkHI6nk/img_110x110.jpg',
                        'profile_image_url': 'http://k.kakaocdn.net/dn/7JAOr/btsM4S9rAUB/hKUwu4ann07fNmdFkHI6nk/img_640x640.jpg',
                        'is_default_image': False
                    }
                }
            }
        """
        # kko_account = data.get('kakao_account', {})
        # email    = kko_account.get("email")
        # info     = {
        #     "email"      : email,
        #     "first_name" : data.get("given_name"),
        #     "last_name"  : data.get("family_name"),
        #     "photo_url"  : data.get("picture"),
        # }
        # user_exist = User.objects.filter(username=email).exists()

        # if user_exist:  return self.run_when_user_exist(request, email)
        # else:           return self.run_when_user_not_exist(request, **info)

        return HttpResponse("sns login done")
