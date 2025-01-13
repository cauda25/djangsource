from django.shortcuts import render, redirect
from .models import Photo
from .forms import *


def photo_list(request):
    photos = Photo.objects.all()
    return render(request, "photo/list.html", {"photos": photos})


def photo_post(request):
    if request.method == "POST":
        # title = request.POST.get("title")
        # author = request.POST.get("author")
        # image = request.POST.get("image")
        # description = request.POST.get("description")
        # prive = request.POST.get("prive")

        # photo = Photo(
        #     title=title,
        #     author=author,
        #     image=image,
        #     description=description,
        #     prive=prive,
        # )

        # photo.save()

        # form 사용
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save()
            return redirect("photo_detail", id=photo.id)
    else:
        form = PhotoForm()
    return render(request, "photo/create.html", {"form": form})


def photo_detail(request, id):
    photo = Photo.objects.get(id=id)

    return render(request, "photo/details.html", {"photo": photo})


def photo_edit(request, id):
    photo = Photo.objects.get(id=id)
    if request.method == "POST":
        # image = request.POST.get("image")
        # description = request.POST.get("description")
        # prive = request.POST.get("prive")

        # if image:
        #     photo.image = image
        # if description:
        #     photo.description = description
        # if prive:
        #     photo.prive = prive

        # photo.save()
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect("photo_detail", id=id)

    else:
        form = PhotoForm(instance=photo)

    return render(request, "photo/edit.html", {"form": form, "photo": photo})


def photo_remove(request, id):
    photo = Photo.objects.get(id=id)
    photo.delete()
    return redirect("photo_list")
