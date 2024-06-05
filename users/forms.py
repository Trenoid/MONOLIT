import uuid
from datetime import timedelta
from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.timezone import now


from users.models import User,EmailVerification

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


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "phone",
            "password1",
            "password2"
        )

    username = forms.CharField()
    email = forms.CharField()
    phone = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    def save(self, commit: bool = True) -> Any:
        user =  super(UserRegistrationForm,self).save(commit = True)
        expiration = now() + timedelta(hours=48)
        record = EmailVerification.objects.create(code = uuid.uuid4() , user = user,expiration = expiration)
        record.send_verification_email()
        return user



class CreateOrderForm(forms.Form):
    promo = forms.CharField(required=False)
    
    # promo = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-comtrol",
    #             "placeholder" : "Введите промокод",
    #         }
    #     )

    # )
