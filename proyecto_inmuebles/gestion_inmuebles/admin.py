from django.contrib import admin
from .models import (
    Inmueble,
    Pais,
    EstadoProvincia,
    Ciudad,
    TipoInmueble,
    Inmueble,
    Usuario,
    UsuarioInmueble,
    Solicitud,
    TipoUsuario,
)


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido_paterno", "telefono")
    search_fields = ("nombre", "id_nacional")
    list_filter = ("nombre", "estado")


admin.site.register(Inmueble)
admin.site.register(Pais)
admin.site.register(EstadoProvincia)
admin.site.register(Ciudad)
admin.site.register(TipoInmueble)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(UsuarioInmueble)
admin.site.register(Solicitud)
