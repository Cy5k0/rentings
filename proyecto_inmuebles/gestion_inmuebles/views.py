from django.shortcuts import render,redirect,get_object_or_404  #get_object_or_404 para filtrar un elemento

#login
#from django.contrib.auth import authenticate, login
#from django.contrib import messages
from .models import PerfilUsuario 
#


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse,HttpResponseRedirect
from .models import ContactForm
from .forms import ContactFormForm,UserUpdateForm,PerfilUpdateForm #,ContactFormModelForm#,CustomUserCreationForm,UserUpdateForm,PasswordForm
#para registro usuarios
#from django.contrib.auth import logout, authenticate, login

from django.contrib import messages

#registro
from .forms import RegistroForm
#from django.db.models.signals import post_save
#from django.dispatch import receiver
#from django.contrib.auth.models import User
from django.contrib.auth import login
#from .forms import RegistroUser

#buscador
from django.http import JsonResponse
from .models import Inmueble,Ciudad,ImagenInmueble,TipoInmueble
#

#misdatos
from .models import PerfilUsuario


# Create your views here.
def indice(request):
    if request.user.is_authenticated:
        perfil = PerfilUsuario.objects.get(user=request.user)
            
        # Guardar el nombre de usuario y tipo de usuario en la sesión
        request.session['usuario'] = request.user.username
        request.session['tipo_usuario'] = perfil.tipo_usuario.tipo 
        tipo_usuario=request.session.get('tipo_usuario')
        print(tipo_usuario)
        return render(request, 'index.html', {'usuario': request.session.get('usuario'), 'tipo_usuario':tipo_usuario })
      
        #return render(request, 'index.html', {'usuario': request.session.get('usuario'), 'tipo_usuario':tipo_usuario })

    return render(request,'index.html',{})


def contacto(request):
    if request.method == 'GET':
        form=ContactFormForm()
    else:
        #para el formulario normal
        form = ContactFormForm(request.POST)
        #para el formulario modal
        #form = ContactFormModelForm(request.POST)
        if form.is_valid():
          contact_form = ContactForm.objects.create(**form.cleaned_data)
          return HttpResponseRedirect('/exito/')
      
    return render(request, 'contactoM.html', {'form': form})
  
#def contactoM(request):
#    if request.method == 'GET':
#        form=ContactFormForm()
#    else:
#        #para el formulario normal
#        #form = ContactFormForm(request.POST)
#        #para el formulario modal
#        form = ContactFormModelForm(request.POST)
#        if form.is_valid():
#          contact_form = ContactForm.objects.create(**form.cleaned_data)
#          return HttpResponseRedirect('exito')
#    return render(request, 'contactoM.html', {'form': form})
    
def exito(request):
    return render(request, "exito.html")
    
#version1  
#def log_in(request):
#    return render(request, "login.html", {})  
#def log_in(request):
#    print('hola')
#    if request.method == "POST":
#        # Captura de los datos del formulario
#        username = request.POST['username']
#        password = request.POST['password']

#        # Autenticación del usuario
#        user = authenticate(request, username=username, password=password)
#        
#        if user is not None:
#            # Si la autenticación es exitosa, iniciar sesión
#            login(request, user)
#            
#            # Obtener información del perfil del usuario
#            perfil = PerfilUsuario.objects.get(user=user)
#            
#            # Guardar nombre y tipo de usuario en la sesión
#            request.session['usuario'] = user.username
#            request.session['tipo_usuario'] = perfil.tipo_usuario
#            print('hola')
#            print("Entrando a la condición de sesión")
#
#            if 'usuario' in request.session:
#                print(f"Usuario en sesión: {request.session['usuario']}")
#            else:
#                print("No hay usuario en la sesión")
#            # Redirigir a la página principal o a otra página
#            return redirect('indice')  # la ruta de destino
#        else:
#            # Si la autenticación falla, muestra un mensaje de error
#            messages.error(request, "Su nombre de usuario y contraseña no coinciden. Inténtelo de nuevo.")
#    
#    # Si la petición es GET o hay un error, muestra la página de login
#    return render(request, "login.html", {})  
  
  
#def register(request):
#    if request.method == 'POST':
#        form = RegistroUser(request.POST)
#        if form.is_valid():
#            user = form.save()
#            login(request, user)
#            return redirect('indice')  # Redirige a la página principal
#    else:
#        form = RegistroUser()

#    return render(request, 'registro.html', {'form': form})  


#@receiver(post_save, sender=User)
#def crear_perfil_usuario(sender, instance, created, **kwargs):
#    if created:
#        PerfilUsuario.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def guardar_perfil_usuario(sender, instance, **kwargs):
#    instance.perfil.save()


def register(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("indice")
    else:
        form = RegistroForm()
    return render(request, template_name="registration/register.html",  context={"form": form})




#version1
#def buscar_ciudades(request):
#    # Verificar si la solicitud es AJAX y si existe el parámetro 'q'
#    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and 'q' in request.GET:
#        query = request.GET.get('q')
#        #firstname__startswith
#        #ciudades = Ciudad.objects.filter(nombre__icontains=query).select_related('estado_provincia__pais')[:20]
#        ciudades = Ciudad.objects.filter(nombre__startswith=query).select_related('estado_provincia__pais').order_by('nombre')[:20]
#        #resultados = [{'nombre': c.nombre, 'estado': c.estado, 'pais': c.pais} for c in ciudades]

#        resultados = [
#            {
#                'id': ciudad.id,
#                'nombre': ciudad.nombre,
#                'estado': ciudad.estado_provincia.nombre,
#                'pais': ciudad.estado_provincia.pais.nombre
#            }
#            for ciudad in ciudades
#        ]
#        return JsonResponse({'resultados': resultados})
#    return JsonResponse({'resultados': []})
def buscar_ciudades(request):
    query = request.GET.get('q', '')

    # Filtrar las ciudades con inmuebles disponibles
    if query:
        # inmuebles disponibles
        ciudades = Ciudad.objects.filter(
            nombre__icontains=query,
            inmueble__disponible=True
        ).distinct()
    else:
        ciudades = []

    # Construir la lista de resultados con la jerarquía de Ciudad -> Estado -> País
    resultados = [{
        'nombre': ciudad.nombre,
        'estado': ciudad.estado_provincia.nombre,
        'pais': ciudad.estado_provincia.pais.nombre,
        'id': ciudad.id
    } for ciudad in ciudades]
    
    return JsonResponse({'resultados': resultados})



def buscar_inmuebles(request):
    ciudad_id = request.GET.get('ciudad_id')
    
    if ciudad_id:
        # Filtrar inmuebles disponibles en la ciudad seleccionada 
        inmuebles = Inmueble.objects.filter(ciudad_id=ciudad_id, disponible=True)
    else:
        inmuebles = Inmueble.objects.filter(disponible=True)  # listado de inmuebles de la ciudad seleccionada
    
    
    # fotos del inmueble
    inmuebles_con_imagenes = []
    for inmueble in inmuebles:
        imagenes = ImagenInmueble.objects.filter(propiedad=inmueble)
        inmuebles_con_imagenes.append({
            'inmueble': inmueble,
            'imagenes': imagenes
        })
    
    context = {
        'inmuebles_con_imagenes': inmuebles_con_imagenes,
        'ciudades': Ciudad.objects.all()  # Para mostrar las ciudades en el menú desplegable
    }
    
    return render(request, 'arriendos.html', context)




def arriendos(request):
    tusuario = request.session.get('tipo_usuario')
    if not tusuario:
        # Si no hay usuario en la sesión, redirigir al login
        return redirect('login')
    return render(request, "arriendos.html")



#actualizar datos del perfil
def misdatos(request):
    perfil = PerfilUsuario.objects.get(user=request.user)
    TIPOS_USUARIO = (
        # ("0", "Nulo"),
        ("1", "Arrendador"),
        ("2", "Arrendatario"),
        # ("3", "Administrador"),
    )
   # tipousuario = TIPOS_USUARIO.get (perfil.tipo_usuario.nombre, "Descripción no disponible")

    #se envia por parametro los 2 modelos
    context = {
        'user': request.user,  # Datos del user de django
        'perfil': perfil  # Datos perfilusuario
        #,'tipo_usuario': tipousuario 
    }
    return render(request, "misdatos.html", context)

@login_required
def update_profile(request):
    # Obtener o crear el perfil del usuario si no existe
    perfil, created = PerfilUsuario.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        perfil_form = PerfilUpdateForm(request.POST, instance=perfil)

        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            messages.success(request, 'Tu perfil ha sido actualizado.')
            return redirect('update_profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        perfil_form = PerfilUpdateForm(instance=perfil)

    context = {
        'user_form': user_form,
        'perfil_form': perfil_form
    }
    return render(request, 'update_profile.html', context)


def mostrar_inmuebles(request):
 
    inmuebles = Inmueble.objects.filter(propietario=request.user)
    
    
    # fotos del inmueble
    inmuebles_con_imagenes = []
    for inmueble in inmuebles:
        print(inmueble.pk)
        imagenes = ImagenInmueble.objects.filter(propiedad=inmueble)
        tipoinmueble = inmueble.tipo_inmueble
        #tipoinmueble = TipoInmueble.objects.filter(TipoInmueble =inmuebles.tipo_inmueble)
        inmuebles_con_imagenes.append({
            'inmueble': inmueble,
            'imagenes': imagenes,
            'tipoinmueble': tipoinmueble
        })
    
    context = {
        'inmuebles_con_imagenes': inmuebles_con_imagenes,
#        'ciudades': Ciudad.objects.all()  # Para mostrar las ciudades en el menú desplegable
    }
    
    return render(request, 'propiedades.html', context)


def add_inmuebles(request):
    if request.method == "POST":
#        titulo = request.POST["titulo"]
#        contenido = request.POST["contenido"]
#        nuevo_post = Post(
#            titulo=titulo, contenido=contenido, fecha_publicacion=datetime.now()
#        )
#        nuevo_post.save()
        return redirect("dashboard_prop")
    return render(request, "add_propiedad.html")


def mostrar_un_inmuebles(request,inmueble_id):
 
    inmuebles = get_object_or_404(Inmueble, pk=inmueble_id, propietario=request.user)
    
    
    # fotos del inmueble
    print(inmuebles.pk)
    imagenes = ImagenInmueble.objects.filter(propiedad=inmuebles)
    tipoinmueble = inmuebles.tipo_inmueble
    #tipoinmueble = TipoInmueble.objects.filter(TipoInmueble =inmuebles.tipo_inmueble)
    context={
        'inmueble': inmuebles,
        'imagenes': imagenes,
        'tipoinmueble': tipoinmueble
    }
    
 
    
    return render(request, 'add_fotoinmueble.html', context)