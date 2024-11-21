import csv
from django.core.management.base import BaseCommand
from gestion_inmuebles.models import EstadoProvincia, Pais


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open("data/provincias.csv", "r")
        # archivo = open("../proyecto_inmuebles/data/provincias.csv", "r") para linux
        reader = csv.reader(archivo, delimiter=";")
        next(reader)  # Se salta la primera linea
        for fila in reader:
            pais = Pais.objects.get(id=fila[1])
            EstadoProvincia.objects.create(id=fila[0], pais=pais, nombre=fila[2])
