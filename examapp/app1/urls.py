from django.urls import path

# from . import views
from .views import app1_list

app_name = "app1"

urlpatterns = [
    # path("", views.app1_list, name="list"),
    path("", app1_list, name="list"),
]
