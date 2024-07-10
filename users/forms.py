import email
import uuid
from datetime import timedelta
from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.timezone import now
from users.tasks import send_email_verification

from users.models import User,EmailVerification, Order

class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ["username","password",]


    username = forms.CharField()
    password = forms.CharField()

    # username = forms.CharField(
    #     label = "username",
    #     widget=forms.TextInput(attrs={"autofocus": True,
    #                                   "class" : "authorization__input",
    #                                   "placeholder": "Имя пользователя"},))
    
    # password = forms.CharField(
    #     label = "password",
    #     widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                       "class" : "authorization__input",
    #                                       "placeholder": "Пароль"
    #                                       }),
    # )


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Подтвердите пароль')

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f"Пользователь с именем '{username}' уже существует")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f"Пользователь с почтой '{email}' уже существует")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError(f"Пользователь с номером телефона '{phone}' уже существует")
        return phone

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            send_email_verification.delay(user.id)
        return user



# class CreateOrderForm(forms.Form):
#     promo = forms.CharField(required=False)
    
#     # promo = forms.CharField(
#     #     widget=forms.TextInput(
#     #         attrs={
#     #             "class": "form-comtrol",
#     #             "placeholder" : "Введите промокод",
#     #         }
#     #     )

#     # )


class OrderForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'pay-form__input',
        'placeholder': 'Имя',
        'required': 'required'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'pay-form__input',
        'placeholder': 'E-mail',
        'required': 'required'
    }))
    promocod = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'class': 'pay-form__input',
        'placeholder': 'Промокод',  
    }))

    class Meta:
        model = Order
        fields = ('name','email','promocod')


