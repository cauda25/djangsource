from django.urls import path
from .views import *

app_name = "poll"

# path("경로",뷰,name="별칭")
# 뷰  1) 함수형 뷰 2) 클래스 뷰

urlpatterns = [
    path("", index, name="index"),
    path("<int:question_id>/", detail, name="detail"),
    path("<int:question_id>/vote/", vote, name="vote"),
    path("<int:question_id>/results/", results, name="results"),
]
