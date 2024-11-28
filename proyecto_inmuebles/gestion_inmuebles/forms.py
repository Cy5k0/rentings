from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import (
    PerfilUsuario,
    TipoUsuario,
    ImagenInmueble,
    Inmueble,
    Pais,
    EstadoProvincia,
    Ciudad,
)

#######


class ContactFormForm(forms.Form):
    # debe contener los atributos necesarios para poder recibir los datos necesarios en el modelo ContactForm
    # contact_form_uuid no necesita ser declarado en el form
    customer_name = forms.CharField(max_length=64, label="Nombre")
    customer_email = forms.EmailField(label="Correo")
    message = forms.CharField(label="Mensaje")


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


class UserUpdateForm(forms.ModelForm):
    # telefono = forms.CharField(max_length=15, required=False)
    # direccion = forms.CharField(max_length=150, required=False)
    # id_nacional = forms.CharField(max_length=20, required=True)
    # tipo_usuario = forms.ModelChoiceField(
    #    queryset=TipoUsuario.objects.all(),
    #    required=False,
    #    empty_label="Seleccione un tipo de usuario",
    # )
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            # 'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            #'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            #'id_nacional': forms.TextInput(attrs={'class': 'form-control'}),
            #'tipo_usuario': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ["telefono", "direccion", "id_nacional", "tipo_usuario"]
        widgets = {
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
            "direccion": forms.TextInput(attrs={"class": "form-control"}),
            "id_nacional": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_usuario": forms.Select(attrs={"class": "form-control"}),
        }


class FotoInmuebleForm(forms.ModelForm):
    class Meta:
        model = ImagenInmueble
        fields = ["imagen"]
        # widgets = {
        #'imagen': forms.ClearableFileInput(attrs={'multiple': False}),
        # }


class InmuebleUpdateForm(forms.ModelForm):
    pais = forms.ModelChoiceField(
        queryset=Pais.objects.all(),
        widget=forms.Select(attrs={"class": "form-control", "id": "id_pais"}),
        required=True,
    )

    # estado_provincia = forms.ModelChoiceField(
    #    queryset=EstadoProvincia.objects.none(),
    estado_provincia = forms.IntegerField(
        widget=forms.Select(attrs={"class": "form-control", "id": "id_estado"}),
        # required=True,
    )

    # ciudad = forms.ModelChoiceField(
    #    queryset=Ciudad.objects.none(),
    ciudad = forms.IntegerField(
        widget=forms.Select(attrs={"class": "form-control", "id": "id_ciudad"}),
        # required=True,
    )

    class Meta:
        model = Inmueble
        fields = [
            "nombre",
            "descripcion",
            "m2_construidos",
            "m2_totales",
            "n_estacionamientos",
            "n_habitaciones",
            "n_baños",
            "precio",
            "moneda",
            "calle",
            "numero",
            "pais",
            "estado_provincia",
            "ciudad",
            "codigo_postal",
            "tipo_inmueble",
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
            "m2_construidos": forms.TextInput(attrs={"class": "form-control"}),
            "m2_totales": forms.TextInput(attrs={"class": "form-control"}),
            "n_estacionamientos": forms.TextInput(attrs={"class": "form-control"}),
            "n_habitaciones": forms.TextInput(attrs={"class": "form-control"}),
            "n_baños": forms.TextInput(attrs={"class": "form-control"}),
            "precio": forms.TextInput(attrs={"class": "form-control"}),
            "moneda": forms.TextInput(attrs={"class": "form-control"}),
            "calle": forms.TextInput(attrs={"class": "form-control"}),
            "numero": forms.TextInput(attrs={"class": "form-control"}),
            #'ciudad': forms.Select(attrs={'class': 'form-control'}),
            "codigo_postal": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_inmueble": forms.Select(attrs={"class": "form-control"}),
        }

    def clean(self, *args, **kwargs):
        print(self.cleaned_data)
        id_ciudad = self.cleaned_data.get("ciudad")
        self.cleaned_data.update({"ciudad": Ciudad.objects.get(pk=id_ciudad)})
        print(self.cleaned_data)

    # propietario = models.ForeignKey(
