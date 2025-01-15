from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path("", views.home, name="home"),
    # login,logout 직접 작성시
    # path("login/", views.users_login, name="login"),
    # path("login/", views.users_login, name="login"),
    # 장고의 auth가 제공하느 login,logout class view 를 사용
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path("register/", views.user_register, name="register"),
]
