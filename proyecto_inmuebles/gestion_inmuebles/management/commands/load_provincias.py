import csv
from django.core.management.base import BaseCommand
from gestion_inmuebles.models import EstadoProvincia



class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open('data/provincias.csv', 'r')
        reader = csv.reader(archivo, delimiter=';')
        next(reader) # Se salta la primera linea
        for fila in reader:
                EstadoProvincia.objects.create(id=fila[0],pais=fila[1], nombre=fila[2])