from django import forms

# para formularios model
# from django.forms import ModelForm
# registro usuarios

# para el register
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import Usuario
# from .models import TipoUsuario
# from django import forms
# from django.contrib.auth.models import User
# from .models import PerfilUsuario,TipoUsuario

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import PerfilUsuario, TipoUsuario

#######


class ContactFormForm(forms.Form):
    # debe contener los atributos necesarios para poder recibir los datos necesarios en el modelo ContactForm
    # contact_form_uuid no necesita ser declarado en el form
    customer_name = forms.CharField(max_length=64, label="Nombre")
    customer_email = forms.EmailField(label="Correo")
    message = forms.CharField(label="Mensaje")


# class RegistroUser(UserCreationForm):
#    id_nacional = forms.CharField(max_length=20, required=True)
#    nombre = forms.CharField(max_length=50, required=True)
#    apellido_paterno = forms.CharField(max_length=50, required=True)
#    apellido_materno = forms.CharField(max_length=50, required=True)
#    correo_electronico = forms.EmailField(required=False, widget=forms.EmailInput)
#    direccion = forms.CharField(max_length=150, required=True)
#    telefono = forms.CharField(max_length=15, required=True)
#    tipo_usuario = forms.ModelChoiceField(queryset=TipoUsuario.objects.all(), required=True)

#    class Meta:
#        model = Usuario
#        fields = ['username', 'password1', 'password2', 'id_nacional', 'nombre', 'apellido_paterno', 'apellido_materno', 'correo_electronico', 'direccion', 'telefono', 'tipo_usuario']

# class RegistroForm(forms.ModelForm):
#    telefono = forms.CharField(max_length=15, required=False)
#    direccion = forms.CharField(max_length=150, required=False)
#    id_nacional = forms.CharField(max_length=20, required=True)
#    tipo_usuario = forms.ModelChoiceField(
#        queryset=TipoUsuario.objects.all(),
#        required=False,
#        empty_label="Seleccione un tipo de usuario"
#    )
#
#    class Meta:
#        model = User
#        fields = ['username', 'first_name', 'last_name', 'email', 'password',  'telefono']

#    def save(self, commit=True):
#        user = super().save(commit=False)
#        user.set_password(self.cleaned_data['password'])
#        if commit:
#            user.save()
#            PerfilUsuario.objects.create(
#                user=user,
#                telefono=self.cleaned_data['telefono'],
#                direccion=self.cleaned_data['direccion'],
#                id_nacional=self.cleaned_data['id_nacional'],
#                tipo_usuario=self.cleaned_data['tipo_usuario']
#            )
#        return user


class RegistroForm(UserCreationForm):
    telefono = forms.CharField(max_length=15, required=False)
    direccion = forms.CharField(max_length=150, required=False)
    id_nacional = forms.CharField(max_length=20, required=True)
    tipo_usuario = forms.ModelChoiceField(
        queryset=TipoUsuario.objects.all(),
        required=False,
        empty_label="Seleccione un tipo de usuario",
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "telefono",
            "direccion",
            "id_nacional",
            "tipo_usuario",
        ]

    def save(self, commit=True):
        # Primero guarda el usuario
        user = super().save(commit=False)
        # Asigna el password
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()  # Guarda el usuario

            # Crea el perfil asociado
            PerfilUsuario.objects.create(
                user=user,
                telefono=self.cleaned_data["telefono"],
                direccion=self.cleaned_data["direccion"],
                id_nacional=self.cleaned_data["id_nacional"],
                tipo_usuario=self.cleaned_data["tipo_usuario"],
            )

            # Asignar grupo según el tipo de usuario
            tipo_usuario = self.cleaned_data["tipo_usuario"]
            if tipo_usuario:
                if tipo_usuario.tipo == "1":  # Arrendador
                    grupo_arrendador, _ = Group.objects.get_or_create(
                        name="Arrendadores"
                    )
                    user.groups.add(grupo_arrendador)
                elif tipo_usuario.tipo == "2":  # Arrendatario
                    grupo_arrendatario, _ = Group.objects.get_or_create(
                        name="Arrendatarios"
                    )
                    user.groups.add(grupo_arrendatario)

        return user
