from django.urls import path
from .views import *

urlpatterns = [
    # http://127.0.0.1:8000/photo/
    path("", photo_list, name="photo_list"),
    # http://127.0.0.1:8000/photo/1 상세조회
    path("<int:id>/", photo_detail, name="photo_detail"),
    # http://127.0.0.1:8000/photo/1/edit 수정
    path("<int:id>/edit/", photo_edit, name="photo_edit"),
    # http://127.0.0.1:8000/photo/new/ 추가
    path("new/", photo_post, name="photo_post"),
    # http://127.0.0.1:8000/photo/1/remove 삭제
    path("<int:id>/remove/", photo_remove, name="photo_remove"),
]
