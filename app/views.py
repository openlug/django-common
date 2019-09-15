from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

name = "Rabbit House 成员管理系统"


def index(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse("profile"))
        return render(request, 'app/index.html', {
            "name": name
        })
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse("profile"))
        else:
            return redirect(reverse("index"))


@login_required
def profile(request):
    if request.user.username == "admin":
        user_profile = "flag redacted. login as admin on server to get flag."
    else:
        user_profile = "仅 admin 用户可阅览 flag。"
    return render(request, 'app/profile.html', {
        "name": name,
        "username": request.user,
        "profile": user_profile
    })


def log_out(request):
    logout(request)
    return redirect(reverse("index"))


from django.contrib.auth import models


def update_last_login(sender, user, **kwargs):
    pass


models.update_last_login = update_last_login
