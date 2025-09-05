from django.contrib.auth.models import User
from django.db import models

from mainapp.models.influencer import Influencer


# Create your models here.

class ChatHistory(models.Model):
    user          = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chats")
    influencer    = models.ForeignKey(Influencer, on_delete=models.CASCADE, related_name="chats", default=1)
    talker_type   = models.CharField(max_length=4)
    style_text    = models.TextField()
    optional_text = models.TextField(blank=True, null=True)
    voice_url     = models.CharField(max_length=256, null=True)
    talked_at     = models.DateTimeField(auto_now_add=True)

    @property
    def time(self):
        return self.talked_at.strftime("%H:%M %p")