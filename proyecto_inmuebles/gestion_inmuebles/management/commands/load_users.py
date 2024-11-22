import csv
from django.core.management.base import BaseCommand

from gestion_inmuebles.services import create_user

# Se ejecuta usando python manage.py test_client
#username;first_name;last_name;email;password;password_confirm;direccion;telefono;tipo_usuario
#12345678-9;Michael;Wittman;fmercury@mail.com;1234;1234;123 Queen St.;5555555;1
#username, password, email, id_nacional, nombre, apellido_paterno, direccion, telefono, tipo_usuario_id
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open('data/users.csv', 'r')
        reader = csv.reader(archivo, delimiter=';')
        next(reader) # Se salta la primera linea
        for fila in reader:
            create_user(fila[0], fila[4], fila[3], fila[0], fila[1], fila[2], fila[6],fila[7],fila[8])
            
            
