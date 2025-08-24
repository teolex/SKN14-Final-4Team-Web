"""
URL configuration for vogue_me project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import path

from . import views as v


class CustomLoginView(LoginView):
    template_name = "app/userapp/login.html"

    def form_valid(self, form):
        user = form.get_user()

        if not user.member.is_authed():
            form.add_error(None, "본인 인증을 완료하지 않았습니다.")
            return self.form_invalid(form)

        login(self.request, user)
        return redirect(self.get_success_url())


app_name = 'userapp'

_login_view = CustomLoginView.as_view(
    template_name="app/userapp/login.html",
    extra_context={
        "GOOGLE_CLIENT_ID"  : settings.GOOGLE_CLIENT_ID,
    }
)

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name="app/userapp/login.html"), name="login"),
    path('login/', _login_view, name="login"),

    # path('login/', v.login, name="login"),
    path('sns_login/<str:provider>', v.sns_login, name="sns_login"),
    path('pick_style/', v.pick_style, name="pick_style"),

    path('signup/', v.signup, name="signup"),
    path('check_email', v.check_email_dup, name="check_email_dup"),
    path('verify/<int:user_id>/<str:encrypted_code>', v.verify_auth_link, name="verify_auth_link"),

]