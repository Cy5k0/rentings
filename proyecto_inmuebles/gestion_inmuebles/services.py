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
    # Buscar un usuario por su id_nacional
    try:
        usuario = Usuario.objects.get(id_nacional=id_nacional)
        return usuario
    except Usuario.DoesNotExist:
        return None  # O manejar el error de alguna otra manera
    
def update_user(id_nacional, nombre=None, apellido_paterno=None, apellido_materno=None, direccion=None, telefono=None, tipo_usuario=None):
    # Buscar el usuario 
    try:
        usuario = Usuario.objects.get(id_nacional=id_nacional)
        
        if nombre:
            usuario.nombre = nombre
        if apellido_paterno:
            usuario.apellido_paterno = apellido_paterno
        if apellido_materno:
            usuario.apellido_materno = apellido_materno
        if direccion:
            usuario.direccion = direccion
        if telefono:
            usuario.telefono = telefono
        if tipo_usuario:
            usuario.tipo_usuario = tipo_usuario
        
        # Guardar 
        usuario.save()
        return usuario
    except Usuario.DoesNotExist:
        return None  
    
def eliminar_usuario(id_nacional):
    # Buscar y eliminar el usuario
    try:
        usuario = Usuario.objects.get(id_nacional=id_nacional)
        usuario.estado = False
        usuario.save()
        return True  # Usuario eliminado 
    except Usuario.DoesNotExist:
        return False  # El usuario no existe    
    