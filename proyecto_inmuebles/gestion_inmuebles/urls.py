from django.urls import path
from . import views

from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("", views.indice , name="indice"),
    path("contacto/", views.contacto , name="contacto"),
    path("exito/", views.exito , name="exito"),
    path("arriendos/", views.arriendos , name="arriendos"),
    path('buscar-ciudades/', views.buscar_ciudades, name='buscar_ciudades'),
    path('buscar_inmuebles/', views.buscar_inmuebles, name='buscar_inmuebles'),
    path('registro/', views.register, name='registro'),
    path("misdatos/", views.misdatos , name="misdatos"),
    path('editar/', views.update_profile, name='update_profile'),
    
    path('dashboard_prop/', views.mostrar_inmuebles, name='dashboard_prop'),
    path('add_propiedad/', views.add_inmuebles, name='agregar_propiedad'),
    path('mostrar_un_inmuebles/<int:inmueble_id>/', views.mostrar_un_inmuebles, name='mostrar_un_inmuebles'),
    
    
    #ajax para mostrar ciudades, estados
    path('ajax/cargar-estados/', views.cargar_estados, name='ajax_cargar_estados'),
    path('ajax/cargar-ciudades/', views.cargar_ciudades, name='ajax_cargar_ciudades'),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)