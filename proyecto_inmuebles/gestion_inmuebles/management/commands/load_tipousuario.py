import csv
from django.core.management.base import BaseCommand
from gestion_inmuebles.models import TipoUsuario


#para ejecutarlo, es en la terminal python manage.py load_tipousuario

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open('data/tipousuario.csv', 'r')
        reader = csv.reader(archivo, delimiter=';')
        #next(reader) # Se salta la primera linea
        for fila in reader:
                TipoUsuario.objects.create(tipo=fila[0])