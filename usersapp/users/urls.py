from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.users_login, name="login"),
    path("logout/", views.users_logout, name="logout"),
    path("register/", views.user_register, name="register"),
]
