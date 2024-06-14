from re import template
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import FormView, TemplateView
from django.contrib.auth import login as auth_login
from django.contrib.messages.views import SuccessMessageMixin

from users.forms import UserLoginForm, UserRegistrationForm
from carts.models import Cart
from common.views import TitleMixin
from users.models import User, EmailVerification, ReferralCode
from main.forms import ContactForm

import string, random


class LoginView(TitleMixin,FormView):
    template_name = 'users/authorization_login.html'
    form_class = UserLoginForm
    title = "Авторизация"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = auth.authenticate(username=username, password=password)

        session_key = self.request.session.session_key

        if user:
            auth_login(self.request, user)
            messages.success(self.request, f"{username} Вы вошли в аккаунт")

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            redirect_page = self.request.POST.get("next", None)
            if redirect_page and redirect_page != reverse("user:logout"):
                return HttpResponseRedirect(redirect_page)

            return HttpResponseRedirect(reverse("main:index"))

        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Авторизация'
        context['login_method'] = 'login'
        return context



# class RegistrationView(CreateView, SuccessMessageMixin):
#     template_name = 'users/authorization_register.html'
#     form_class = UserRegistrationForm
#     success_message = "Вы успешно зарегестрировались"

#     def form_valid(self, form):
#         user = form.save()
#         session_key = self.request.session.session_key

#         auth_login(self.request, user)

#         if session_key:
#             Cart.objects.filter(session_key=session_key).update(user=user)

#         messages.success(self.request, f"{user.username} Вы успешно зарегистрированы и вошли в аккаунт")
#         return HttpResponseRedirect(self.get_success_url())

#     def get_success_url(self):
#         return reverse("main:index")

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Регистрация'
#         context['login_method'] = 'register'
#         return context

class RegistrationView(CreateView, SuccessMessageMixin):
    template_name = 'users/authorization_register.html'
    form_class = UserRegistrationForm
    success_message = "Вы успешно зарегестрировались"

    def form_valid(self, form):
        user = form.save()

        # Создание уникального реферального кода
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        while ReferralCode.objects.filter(code=code).exists():
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        referral_code = ReferralCode.objects.create(code=code)
        user.referral_code = referral_code
        user.save()

        session_key = self.request.session.session_key
        auth_login(self.request, user)

        if session_key:
            Cart.objects.filter(session_key=session_key).update(user=user)

        messages.success(self.request, f"{user.username} Вы успешно зарегистрированы и вошли в аккаунт")
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("main:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['login_method'] = 'register'
        return context



class EmailVerificationView(TitleMixin, TemplateView):
    title = "Подтверждение электронной почты"
    template_name = "users/email_verification.html"

    def get(self, request, *args, **kwargs) -> HttpResponse:
        code = kwargs.get('code')
        email = kwargs.get('email')
        try:
            user = User.objects.get(email=email)
            email_verification = EmailVerification.objects.filter(user=user, code=code)
            if email_verification.exists(): # and not email_verification.first().is_expired()
                user.is_verified_email = True
                user.save()
                return super().get(request, *args, **kwargs)
            else:
                messages.error(request, "Неверный код подтверждения или пользователь не найден.")
        except User.DoesNotExist:
            messages.error(request, "Пользователь с данной электронной почтой не найден.")
        return HttpResponseRedirect(reverse("main:index"))









def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request,user)

            if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

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





def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username = username,password = password)


            session_key = request.session.session_key


            if user:
                auth.login(request,user)
                messages.success(request,f"{username} Вы вошли в аккаунт")
                
                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                redirect_page = request.POST.get("next",None)
                if redirect_page and redirect_page != reverse("user:logout"):
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



class AccountView(TemplateView):
    template_name = "users/account.html"

    def get_context_data(self, **kwargs):
        context =  super(AccountView,self).get_context_data()
        context['title'] = 'Личный кабинет'
        return context
    


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

    return HttpResponseRedirect(reverse("main:index"))
    return render(request, "main/index.html", context)


def recovery_account(request):
    context = {
        'title' : 'Восстановление'
    }

    return redirect(reverse("main:index"))


def users_cart(request):
    form = ContactForm()
    context = {
        'title': 'Корзина',
        'form': form,
    }
    return render(request, "users/user_cart.html", context)

@login_required
def create_order(request):
    pass

def email_ver(requset):
    return render(requset,"users/email_verification.html")

def pay(request):
    context = {
        'title' : 'Покупка',
    }
    return render(request,'users/pay.html',context)