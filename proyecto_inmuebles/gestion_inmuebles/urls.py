from django.urls import path
from . import views

from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.indice , name="indice"),
    ]