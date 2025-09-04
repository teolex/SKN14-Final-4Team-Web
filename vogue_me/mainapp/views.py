# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

@login_required
def index(request):
    return render(request, "app/mainapp/index.html")

def detail(request):
    return render(request, "app/mainapp/detail.html")