from django.urls import path
from . import views

from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.indice , name="indice"),
    path("contacto/", views.contacto , name="contacto"),
    path("exito/", views.exito , name="exito"),
    path("arriendos/", views.arriendos , name="arriendos"),
    path('buscar-ciudades/', views.buscar_ciudades, name='buscar_ciudades'),
    path('registro/', views.register, name='registro'),
    ]