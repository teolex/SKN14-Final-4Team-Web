# Create your views here.
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

@login_required
def index(request):
    # 기존에 입력한 선호 스타일이 있는지 체크

    return render(request, "app/mainapp/index.html")

def detail(request, id):
    return render(request, "app/mainapp/detail.html")