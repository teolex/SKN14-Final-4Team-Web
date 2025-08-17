from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class LoginAuth(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    auth_code   = models.CharField(max_length=10)
    created_at  = models.DateTimeField(auto_now_add=True)
    due_time    = models.DateTimeField()
    authed_time = models.DateTimeField(null=True)