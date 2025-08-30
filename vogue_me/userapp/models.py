from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


class Member(models.Model):
    user      = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="member")
    authed    = models.CharField(max_length=1, choices=[("Y","인증됨"),("N","미인증")], default="N")
    sns_type  = models.CharField(max_length=10)
    photo_url = models.CharField(max_length=256, null=False, default="/static/default_user.jpg")

    @classmethod
    def add_new_user(cls, email, first_name, last_name):
        user = User(username=email, email=email, first_name=first_name, last_name=last_name)
        user.set_unusable_password()
        user.save()
        return user

    @classmethod
    def add_new_member(cls, user, sns_type, photo_url="/static/default_user.jpg"):
        member = Member.objects.create(user=user, sns_type=sns_type, photo_url=photo_url)
        return member

    def is_authed(self):
        return "Y" == self.authed



# Create your models here.
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True)     # User 의 email 속성을 덮어쓰기 위해 선언

    class Meta:
        model  = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        if email:
            cleaned_data["username"] = email  # username 필드에 email 을 설정
        return cleaned_data

    def save(self):
        user = super().save(commit=False)
        user.username = self.cleaned_data["username"]  # email → username
        user.email = self.cleaned_data["email"]
        user.save()
        return user

