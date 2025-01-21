from django.urls import path
from .views.base_views import *
from .views.question_views import *
from .views.answer_views import *
from .views.comment_views import *

app_name = "board"

urlpatterns = [
    path("", index, name="index"),
    #### 질문
    path("qusetion/<int:id>/", detail, name="detail"),
    path("qusetion/create/", create, name="create"),
    path("qusetion/modify/<int:id>/", modify, name="modify"),
    path("qusetion/delete/<int:id>/", delete, name="delete"),
    #### 답변
    path("answer/create/<int:id>/", answer_create, name="answer_create"),
    path("answer/modify/<int:id>/", answer_modify, name="answer_modify"),
    path("answer/delete/<int:id>/", answer_delete, name="answer_delete"),
    #### 질문 댓글
    path("comment/create/question/<int:id>/", comment_create_question, name="ccq"),
    path("comment/modify/question/<int:id>/", comment_modify_question, name="cmq"),
    path("comment/delete/question/<int:id>/", comment_delete_question, name="cdq"),
    #### 답변 댓글
    path("comment/create/answer/<int:id>/", comment_create_answer, name="cca"),
    path("comment/modify/answer/<int:id>/", comment_modify_answer, name="cma"),
    path("comment/delete/answer/<int:id>/", comment_delete_answer, name="cda"),
]
