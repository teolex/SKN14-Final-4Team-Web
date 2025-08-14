from django.shortcuts import render

# Create your views here.

def login(request):
    if request.method == "POST":
        pass
    else:
        pass

    return render(request, "app/userapp/login.html")


def pick_style(request):
    return render(request, "app/userapp/pick_style.html")

def make_avatar(request):
    if request.method == "POST":
        pass
    else:
        pass
    return render(request, "app/userapp/make_avatar.html")
