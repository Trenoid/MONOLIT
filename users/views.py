from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm

def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username = username,password = password)
            if user:
                auth.login(request,user)
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {
        'title' : 'Авторизация',
        "login_method" : "login",
        "form" : form,
    }

    return render(request, "users/authorization_login.html", context)


def registration(request):
    context = {
        'title' : 'Регистрация',
        "login_method" : "register",

    }
    return render(request, "users/authorization_register.html", context)


def account(request):
    context = {
        'title' : 'Личный кабинет'
    }

    return render(request, "users/account.html", context)


def logout(request):
    context = {
        'title' : 'Главная страница'
    }

    return render(request, "main/index.html", context)


def recovery_account(request):
    context = {
        'title' : 'Восстановление'
    }

    return render(request, "users/recovery_account.html", context)


