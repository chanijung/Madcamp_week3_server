from django.urls import path, include
from . import views

app_name = "treasure"
urlpatterns = [
    path("hide/", views.hide, name="hide")
]