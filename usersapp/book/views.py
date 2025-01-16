from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm


def book_list(request):
    book = Book.objects.order_by("-id")
    return render(request, "book/list.html", {"book": book})


def book_deatail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, "book/detail.html", {"book": book})


def book_edit(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("books:detail", id=id)

    else:
        form = BookForm(instance=book)
    return render(request, "book/edit.html", {"form": form, "id": id})


def book_create(request):

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect("books:detail", id=book.id)

    else:
        form = BookForm()
    return render(request, "book/create.html", {"form": form})


def book_remove(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect("books:list")
