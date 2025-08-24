# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, "app/mainapp/index.html")

def our_team(request):
    return render(request, "app/mainapp/our_team.html")