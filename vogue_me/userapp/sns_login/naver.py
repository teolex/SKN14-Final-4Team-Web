from django.db import transaction

from mailapp.models import *
from mailapp.utils import *
from .sns_login import SnsLogin


class Naver(SnsLogin):
    def __init__(self):
        super().__init__("naver", settings.NAVER_CLIENT_ID, settings.NAVER_CLIENT_SECRET)
        self.token_url    = "https://nid.naver.com/oauth2.0/token"
        self.userinfo_url = "https://openapi.naver.com/v1/nid/me"

    @transaction.atomic
    def login(self, request):
        params   = self.get_auth_params(request)
        token    = self.get_access_token(self.token_url, params)
        headers  = {'Authorization': f'Bearer {token}'}

        data     = self.get_json_response(self.userinfo_url, headers=headers)
        data     = data.get("response")
        email    = data.get("email")
        name     = data.get("name")

        print(f"{data=}")
        """
        data={'resultcode': '00', 'message': 'success',
              'response': {
                  'id': 'UXTOkq3td-F6KxX9hB9pVUJxhej9Wi5v9_tEgZyVl6k',
                  'profile_image': 'https://phinf.pstatic.net/contact/1/2016/8/29/ubangbang_1472447388934.jpg',
                  'email': 'ubangbang@naver.com',
                  'name': '송지훈'}}
        """
        first_name, last_name = self._name_refine(name)

        info     = {
            "email"      : email,
            "first_name" : first_name,
            "last_name"  : last_name,
            "photo_url"  : data.get("profile_image"),
        }
        user_exist = User.objects.filter(username=email).exists()

        if user_exist:  return self.run_when_user_exist(request, email)
        else:           return self.run_when_user_not_exist(request, **info)

    def _name_refine(self, name):
        if " " not in name:
            name = f"{name[1:]} {name[0]}"

        full_name = name.split(" ")
        return full_name[0], full_name[1]   # first_name, last_name