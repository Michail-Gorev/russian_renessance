from .models import Employer
from django.forms import ModelForm, TextInput, forms, CharField, EmailField
from django import forms

STOP_LIST = [
    'мат',
    'мат',
    'мат',
]


class UserForm(ModelForm):
    class Meta:
        model = Employer
        fields = ['name', 'e_mail', 'organization']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            "e_mail": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Е-mail'
            }),
            "organization": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Организация'
            })
        }

    def clean_recipients(self):
        data = self.cleaned_data['name']
        if "мат" in data:
            raise forms.ValidationError("You have forgotten about Fred!")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data
