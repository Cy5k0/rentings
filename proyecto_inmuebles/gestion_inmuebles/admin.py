from django.contrib import admin
from .models import Inmueble, Pais,EstadoProvincia,Ciudad,TipoInmueble,Inmueble,UsuarioInmueble,Solicitud
from .models import ContactForm
from django.contrib.auth.models import User

from .models import (
    Inmueble,
    Pais,
    EstadoProvincia,
    Ciudad,
    TipoInmueble,
    Inmueble,
    UsuarioInmueble,
    Solicitud,
    TipoUsuario,
)

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_active")  
    search_fields = ("username", "email")  # Búsqueda por username y correo
    list_filter = ("is_active", "is_staff")  # Filtros para usuario activo y staff

admin.site.unregister(User)  
admin.site.register(User, UserAdmin)  # Registrar User con la nueva configuración
#class UsuarioAdmin(admin.ModelAdmin):
#    list_display = ("nombre", "apellido_paterno", "telefono")
#    search_fields = ("nombre", "id_nacional")
#    list_filter = ("nombre", "estado")


admin.site.register(Inmueble)
admin.site.register(Pais)
admin.site.register(EstadoProvincia)
admin.site.register(Ciudad)
admin.site.register(TipoInmueble)
#admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(UsuarioInmueble)
admin.site.register(Solicitud)
admin.site.register(ContactForm)