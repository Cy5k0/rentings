import csv
from django.core.management.base import BaseCommand
from gestion_inmuebles.models import TipoInmueble


#para ejecutarlo, es en la terminal python manage.py load_tiposinmuebles

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open('data/tiposinmuebles.csv', 'r')
        reader = csv.reader(archivo, delimiter=';')
        #next(reader) # Se salta la primera linea
        for fila in reader:
                TipoInmueble.objects.create(nombre=fila[0])