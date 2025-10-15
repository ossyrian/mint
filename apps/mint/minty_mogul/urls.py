from django.urls import path

from . import views

app_name = "minty_mogul"

urlpatterns = [
    path("", views.landing, name="landing"),
]
