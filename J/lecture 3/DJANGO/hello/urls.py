from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("jonas", views.jonas, name="jonas"),
    path("<str:name>", views.greet, name="greet")
]
