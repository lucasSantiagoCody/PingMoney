from .models import CustomUser
from django import forms


class CustomUserCreationForm(forms.ModelForm):
    model = CustomUser
    fields = ['full_name', 'email', 'cpf_cnpj', 'password']

class CustomUserChangeForm(forms.ModelForm):
    model = CustomUser
    fields = ['full_name', 'email', 'cpf_cnpj', 'password']
