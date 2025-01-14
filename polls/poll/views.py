from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views.generic.base import TemplateView
from .models import *


# 클래스 뷰
class HomeView(TemplateView):
    template_name = "home.html"


# 함수형 뷰
# HttpResponse 객체 리턴
# render(request,템플릿명) 리턴
# redirect() 리턴


def index(request):
    # return HttpResponse("Hello")

    # 전체 question 조회
    question = Question.objects.all()
    return render(request, "poll/index.html", {"question": question})


def detail(request, question_id):
    # get() : 원하는 정보를 찾지 못하는 경우 DoesNotExist 발생
    # try:
    #     question = Question.objects.get(id=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question id를 확인해 주세요")
    question = get_object_or_404(Question, id=question_id)
    return render(request, "poll/detail.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    # post
    if request.method == "POST":
        # 사용자가 선택한 choice 가져오기
        selected_choice = request.POST.get("choice")
        # choice 테이블에서 vote 추가하기
        # Choice 찾기
        # Choice.objects.get() or get_object_or_404(Choice, id=choice)
        choice = question.choice_set.get(id=selected_choice)
        choice.votes += 1
        choice.save()

        return redirect("poll:results", question_id=question.id)


def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, "poll/results.html", {"question": question})
