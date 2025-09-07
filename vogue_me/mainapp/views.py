# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apiapp.models import ChatHistory


@login_required
def index(request):
    context = {}
    # 기존에 입력한 선호 스타일이 있는지 체크
    if ChatHistory.objects.filter(user_id=request.user.id).count() == 0:
        context["newbie"] = True

    # 마지막에 대화했던 AI 정보 호출해서 화면에 구성.
    last_ai = ChatHistory.objects.last().influencer
    request.session["last_ai_id"] = last_ai.id
    context["last_ai"] = {
        "name"  : last_ai.name,
        "image" : last_ai.profile_img_url,
        "voice" : last_ai.voice_info,
    }

    return render(request, "app/mainapp/index.html", context)

def detail(request, id):
    return render(request, "app/mainapp/detail.html")