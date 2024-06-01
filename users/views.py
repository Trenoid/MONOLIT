from django.shortcuts import render

# Create your views here.

def login(request):
    context = {
        'title' : 'Авторизация',
        "login_method" : "login",
    }

    return render(request, "users/authorization.html", context)


def registration(request):
    context = {
        'title' : 'Регистрация',
        "login_method" : "register",

    }
    return render(request, "users/authorization.html", context)


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


