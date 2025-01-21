from django.shortcuts import render, get_object_or_404, redirect
from .models import Answer, Question, Comment
from .forms import QuestionForm, AnswerForm, CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils import timezone


########################### 댓글
@login_required(login_url="users:login")
def comment_create_question(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.question = question
            comment.save()
            return redirect("board:detail", question.id)
    else:
        form = CommentForm()
    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="users:login")
def comment_modify_question(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modityed_at = timezone.now()
            comment.save()
            return redirect("board:detail", comment.question.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="users:login")
def comment_delete_question(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect("board:detail", comment.question.id)


@login_required(login_url="users:login")
def comment_create_answer(request, id):
    answer = get_object_or_404(Answer, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.answer = answer
            comment.save()
            return redirect("board:detail", answer.question.id)
    else:
        form = CommentForm()
    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="users:login")
def comment_modify_answer(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modityed_at = timezone.now()
            comment.save()
            return redirect("board:detail", comment.answer.question.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="users:login")
def comment_delete_answer(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect("board:detail", comment.answer.question.id)


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


########################### 질문
@login_required(login_url="users:login")
def delete(request, id):
    question = Question.objects.get(id=id)
    question.delete()
    return redirect("board:index")


@login_required(login_url="users:login")
def modify(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modityed_at = timezone.now()
            question.save()
            return redirect("board:detail", id)
    else:
        form = QuestionForm(instance=question)
    return render(request, "board/question_form.html", {"form": form})


@login_required(login_url="users:login")
def create(request):

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect("board:index")
    else:
        form = QuestionForm()
    return render(request, "board/question_form.html", {"form": form})


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
