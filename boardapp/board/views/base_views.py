from django.shortcuts import render, get_object_or_404
from ..models import Question
from django.core.paginator import Paginator


def detail(request, id):
    question = get_object_or_404(Question, id=id)

    return render(request, "board/question_detail.html", {"question": question})


def index(request):

    page = request.GET.get("page", 1)

    # 전체 질문 추출(작성일시 내림차순)
    objects = Question.objects.order_by("-created_at")

    paginator = Paginator(objects, 10)
    question_list = paginator.get_page(page)

    return render(request, "board/question_list.html", {"question_list": question_list})
