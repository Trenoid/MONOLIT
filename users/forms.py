from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User

class UserLoginForm(AuthenticationForm):


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

    class Meta:
        model = User
        fields = ["username","password",]