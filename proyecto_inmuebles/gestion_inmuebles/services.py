from django.contrib.auth.models import User
from .models import PerfilUsuario, TipoUsuario

#username;first_name;last_name;email;password;password_confirm;direccion;tipo_usuario
def create_user(username, password, email, id_nacional, nombre, apellido_paterno, direccion, telefono, tipo_usuario_id):
    # Primero, crea el usuario básico del modelo `User` de Django
    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=nombre,
        last_name=apellido_paterno
    )

    # Intenta recuperar el `TipoUsuario` usando el `tipo_usuario_id`
    try:
        tipo_usuario = TipoUsuario.objects.get(id=tipo_usuario_id)
    except TipoUsuario.DoesNotExist:
        tipo_usuario = None  # Si no se encuentra el tipo, lo deja como `None`

    # Crea el perfil asociado al usuario recién creado
    perfil_usuario = PerfilUsuario.objects.create(
        user=user,
        id_nacional=id_nacional,
        telefono=telefono,
        direccion=direccion,
        tipo_usuario=tipo_usuario
    )

    return perfil_usuario



def get_user_x_id(id_nacional):
    # Buscar un usuario por su id_nacional en el modelo PerfilUsuario
    try:
        perfil = PerfilUsuario.objects.get(id_nacional=id_nacional)
        return perfil  # Devuelve el perfil encontrado
    except PerfilUsuario.DoesNotExist:
        return None  # O manejar el error de alguna otra manera


def update_user(id_nacional, nombre=None, apellido_paterno=None, apellido_materno=None, direccion=None, telefono=None, tipo_usuario=None):
    # Buscar el perfil de usuario por id_nacional
    try:
        perfil = PerfilUsuario.objects.get(id_nacional=id_nacional)
        user = perfil.user  # Accede al objeto User relacionado
        
        # Actualizar campos del perfil y del usuario
        if nombre:
            user.first_name = nombre
        if apellido_paterno or apellido_materno:
            user.last_name = f"{apellido_paterno or ''} {apellido_materno or ''}".strip()
        if direccion:
            perfil.direccion = direccion
        if telefono:
            perfil.telefono = telefono
        if tipo_usuario:
            perfil.tipo_usuario_id = tipo_usuario  # Asegúrate de pasar un ID válido para tipo_usuario
        
        # Guardar cambios en el usuario y perfil
        user.save()
        perfil.save()
        return perfil
    except PerfilUsuario.DoesNotExist:
        return None  


def eliminar_usuario(id_nacional):
    # Buscar y "eliminar" (desactivar) al usuario
    try:
        perfil = PerfilUsuario.objects.get(id_nacional=id_nacional)
        user = perfil.user
        
        # En lugar de eliminar, desactivamos al usuario estableciendo is_active en False
        user.is_active = False
        user.save()
        return True  # Usuario desactivado correctamente
    except PerfilUsuario.DoesNotExist:
        return False  # El usuario no existe