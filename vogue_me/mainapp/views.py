# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

@login_required
def index(request):
    return HttpResponse("<h1>여기에 채팅 화면 나오기</h1>")

def style(request):
    return render(request, "app/mainapp/style.html")

def our_team(request):
    return render(request, "app/mainapp/our_team.html")