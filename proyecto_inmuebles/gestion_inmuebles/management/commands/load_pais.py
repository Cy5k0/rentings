import csv
from django.core.management.base import BaseCommand
from gestion_inmuebles.models import Pais


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open("/data/paises.csv", "r")
        # archivo = open("../proyecto_inmuebles/data/paises.csv", "r") Para Linux
        reader = csv.reader(archivo, delimiter=";")
        next(reader)  # Se salta la primera linea
        for fila in reader:
            Pais.objects.create(id=fila[0], nombre=fila[1])
