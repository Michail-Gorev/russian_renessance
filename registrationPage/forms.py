from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, CheckboxInput

from registrationPage.models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'e_mail', 'isIndividual', 'company']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            "e_mail": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e-mail'
            }),
            "isIndividual": CheckboxInput(attrs={
                'class': 'form-control '
            }),
            "company": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Компания',

            })
        }


class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

