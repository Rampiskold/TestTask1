from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

# Форма регистрации пользователя
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control',
                                                    'type': 'password'}),
        }


# Форма редактирования пользователя
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')


# Форма редактирования профиля пользователя
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
        # fields = ('date_of_birth', 'imag')
