from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(ModelAdmin):
    add = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'is_superuser', 'is_staff']
    list_filter = ['balance', 'email', 'is_superuser']

admin.site.register(CustomUser, CustomUserAdmin)