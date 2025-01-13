from django.urls import path
from .views import *

urlpatterns = [
    path("musician/create/", musician_create, name="musician_create"),
    path("musician/list/", musician_list, name="musician_list"),
    path("musician/<int:id>/edit/", musician_edit, name="musician_edit"),
]
