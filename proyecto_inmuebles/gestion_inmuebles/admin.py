from django.contrib import admin
from .models import Inmueble, Pais,EstadoProvincia,Ciudad,TipoInmueble,Inmueble,Usuario,UsuarioInmueble,Solicitud
from .models import ContactForm


admin.site.register(Inmueble)
admin.site.register(Pais)
admin.site.register(EstadoProvincia)
admin.site.register(Ciudad)
admin.site.register(TipoInmueble)
admin.site.register(Usuario)
admin.site.register(UsuarioInmueble)
admin.site.register(Solicitud)
admin.site.register(ContactForm)