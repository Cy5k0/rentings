from .models import Usuario

def create_user(id_nacional, nombre, apellido_paterno, apellido_materno, direccion, telefono, tipo_usuario):

    usuario = Usuario.objects.create(
        id_nacional=id_nacional,
        nombre=nombre,
        apellido_paterno=apellido_paterno,
        apellido_materno=apellido_materno,
        direccion=direccion,
        telefono=telefono,
        tipo_usuario=tipo_usuario
    )
    return usuario

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
    