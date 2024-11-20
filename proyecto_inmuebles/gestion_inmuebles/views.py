from django.shortcuts import render,redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse,HttpResponseRedirect
from .models import ContactForm
from .forms import ContactFormForm#,ContactFormModelForm,CustomUserCreationForm,UserUpdateForm,PasswordForm
#para registro usuarios
#from django.contrib.auth import logout, authenticate, login

from django.contrib import messages




# Create your views here.
def indice(request):
  
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
          return HttpResponseRedirect('exito')
    return render(request, 'contactoM.html', {'form': form})
  
def exito(request):
    return render(request, "exito.html", {})
    
  
def log_in(request):
    return render(request, "login.html", {})  