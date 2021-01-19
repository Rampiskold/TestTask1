from django.urls import path, re_path

from accounts.views import LoginPage, RegisterPage, edit, logoutUser


app_name = 'account'
urlpatterns = [
   path('login/', LoginPage.as_view(), name="login"),
   path('register/', RegisterPage.as_view(), name="register"),
   path('edit/', edit, name='edit'),
   path('logout/', logoutUser, name="logout"),
]
