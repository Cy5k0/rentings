from django.shortcuts import render,redirect

#login
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import PerfilUsuario 
#


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse,HttpResponseRedirect
from .models import ContactForm
from .forms import ContactFormForm#,ContactFormModelForm#,CustomUserCreationForm,UserUpdateForm,PasswordForm
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


# Create your views here.
def indice(request):
    tusuario = request.session.get('tipo_usuario')
    if not tusuario:
        # Si no hay usuario en la sesión, redirigir al login
        return render(request,'index.html',{'tusuario': tusuario})
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
def log_in(request):
    if request.method == "POST":
        # Captura de los datos del formulario
        username = request.POST['username']
        password = request.POST['password']

        # Autenticación del usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Si la autenticación es exitosa, iniciar sesión
            login(request, user)
            
            # Obtener información del perfil del usuario
            perfil = PerfilUsuario.objects.get(user=user)
            
            # Guardar nombre y tipo de usuario en la sesión
            request.session['usuario'] = user.username
            request.session['tipo_usuario'] = perfil.tipo_usuario 
            
            # Redirigir a la página principal o a otra página
            return redirect('indice')  # Cambia 'pagina_principal' a la ruta de destino
        else:
            # Si la autenticación falla, muestra un mensaje de error
            messages.error(request, "Su nombre de usuario y contraseña no coinciden. Inténtelo de nuevo.")
    
    # Si la petición es GET o hay un error, muestra la página de login
    return render(request, "login.html", {})  
  
  
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