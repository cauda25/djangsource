from django.shortcuts import render, get_object_or_404, redirect
from ..models import Answer, Question
from ..forms import AnswerForm

from django.contrib.auth.decorators import login_required
from django.utils import timezone


########################### 답변
@login_required(login_url="users:login")
def answer_modify(request, id):
    answser = get_object_or_404(Answer, id=id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answser)
        if form.is_valid():
            answser = form.save(commit=False)
            answser.modityed_at = timezone.now()
            answser.save()
            return redirect("board:detail", answser.question.id)
    else:
        form = AnswerForm(instance=answser)
    return render(request, "board/answer_form.html", {"form": form})


@login_required(login_url="users:login")
def answer_delete(request, id):
    answer = get_object_or_404(Answer, id=id)
    answer.delete()

    return redirect("board:detail", answer.question.id)


@login_required(login_url="users:login")
def answer_create(request, id):

    question = get_object_or_404(Question, id=id)
    # form 사용 방식
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            # answer.save() Question 정보없음
            answer = form.save(commit=False)  # commit=False db에 저장하지 않고 진행
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect("board:detail", id)
    else:
        form = AnswerForm()

    # content = request.POST.get("content")
    # # Answer 생성
    # # 방법1)
    # anwser = Answer(content=content, question=question)
    # anwser.save()

    # # 방법2)
    # Answer.objects.create()

    # # 방법3)
    # question.answer_set.create(content=content)
    # return redirect("board:detail", id)
    context = {"form": form, "question": question}
    return render(request, "board/question_detail.html", context)
