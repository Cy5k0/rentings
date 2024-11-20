from django import forms
from .models import ContactForm
#para formularios model
from django.forms import ModelForm
#registro usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactFormForm(forms.Form):
    #debe contener los atributos necesarios para poder recibir los datos necesarios en el modelo ContactForm
    #contact_form_uuid no necesita ser declarado en el form
    customer_name = forms.CharField(max_length=64, label="Nombre")
    customer_email = forms.EmailField(label="Correo")
    message = forms.CharField(label="Mensaje")
    

class ContactFormModelForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
        labels = {
            'customer_email': 'Correo electrónico',
            'customer_name': 'Nombre del cliente',
            'message': 'Mensaje',
        }    
    