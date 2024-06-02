from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm

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
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request,user)
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm() 


    context = {
        'title' : 'Регистрация',
        "login_method" : "register",
        "form" : form

    }
    return render(request, "users/authorization_register.html", context)


def account(request):
    context = {
        'title' : 'Личный кабинет'
    }

    return render(request, "users/account.html", context)


def logout(request):
    auth.logout(request)
    context = {
        'title' : 'Главная страница'
    }

    return render(request, "main/index.html", context)


def recovery_account(request):
    context = {
        'title' : 'Восстановление'
    }

    return redirect(reverse("main:index"))


