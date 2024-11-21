#id, estado_provincia_id , nombre

import csv
from django.core.management.base import BaseCommand
from gestion_inmuebles.models import Ciudad



class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open('data/ciudades.csv', 'r')
        reader = csv.reader(archivo, delimiter=';')
        next(reader) # Se salta la primera linea
        for fila in reader:
                Ciudad.objects.create(id=fila[0],estado_provincia_id=fila[1], nombre=fila[2])