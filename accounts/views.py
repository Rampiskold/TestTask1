from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import View

from .forms import *
from .models import *


# Функция редактирования профиля
@login_required()
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST, files=request.FILES)
        active_users = User.objects.filter(is_active=True)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request,
                          'accounts/edit.html',
                          {
                            'user_form': user_form,
                            'profile_form': profile_form,
                            'active_users': active_users
                           })
    else:
        active_users = User.objects.filter(is_active=True)
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'accounts/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form,
                       'active_users': active_users})


# Функция регистрации
class RegisterPage(View):
    def get(self, request):
        form = CreateUserForm()
        data = {"form": form}
        return render(request, 'accounts/register.html', data)

    def post(self, request):
        form = CreateUserForm(request.POST)
        data = {"form": form}
        if form.is_valid():
            new_user = form.cleaned_data.get('username')
            new_u = form.save()

            profile = Profile.objects.create(user=new_u)
            new_u = profile.save()

            messages.success(request, 'Аккаунт был успешно создан ' + new_user)
            return redirect('account:login')
        return render(request, 'account/register.html', data)


# Функция входа
class LoginPage(View):
    def get(self, request):
        data = {}
        return render(request, 'accounts/login.html', data)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing:landing')
        else:
            messages.info(request, 'Неверное имя пользователя или пароль')
        return redirect('account:login')


# Функция выхода из учётной записи
def logoutUser(request):
    logout(request)
    return redirect('landing:landing')
