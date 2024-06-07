from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form__input',
        'placeholder': 'Имя',
        'required': 'required'
    }))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'class': 'form__input',
        'placeholder': '+ (   ) -- -- -- --',
        'required': 'required'
    }))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form__input',
        'placeholder': 'Город',
        'required': 'required'
    }))