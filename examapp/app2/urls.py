from django.urls import path
from . import views

app_name = "app2"

urlpatterns = [
    # name 태그 이름 중복 가능 다만 후열의 만든내용으로 덮어쓰기됨
    path("", views.app2_list, name="list"),
]
