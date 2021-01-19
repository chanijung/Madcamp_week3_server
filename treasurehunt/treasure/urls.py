from django.urls import path, include
from . import views

app_name = "treasure"
urlpatterns = [
    path("hide/", views.hide, name="hide"),
    path("hunt/", views.hunt, name="hunt"),
    path("seek/", views.seek, name="seek"),
    path("my/", views.my, name="my")
]