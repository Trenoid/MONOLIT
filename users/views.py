from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
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
                messages.success(request,f"{username} Вы вошли в аккаунт")

                if request.POST.get("next",None):
                    return HttpResponseRedirect(request.POST.get("next"))

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
            messages.success(request,f"{user.username} Вы успешно зарегестрированны и вошли в аккаунт")
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm() 


    context = {
        'title' : 'Регистрация',
        "login_method" : "register",
        "form" : form

    }
    return render(request, "users/authorization_register.html", context)


@login_required
def account(request):
    context = {
        'title' : 'Личный кабинет'
    }

    return render(request, "users/account.html", context)

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request,f"{request.user.username} Вы вышли из аккаунта")
    context = {
        'title' : 'Главная страница'
    }

    return render(request, "main/index.html", context)


def recovery_account(request):
    context = {
        'title' : 'Восстановление'
    }

    return redirect(reverse("main:index"))


