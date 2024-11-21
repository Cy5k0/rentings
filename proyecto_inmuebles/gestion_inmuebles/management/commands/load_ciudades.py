# id, estado_provincia_id , nombre
import csv
from django.core.management.base import BaseCommand
from gestion_inmuebles.models import Ciudad


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open("data/ciudades.csv", "r")
        # archivo = open("../proyecto_inmuebles/data/ciudades.csv", "r") para linux
        reader = csv.reader(archivo, delimiter=";")
        next(reader)  # Se salta la primera linea

        for numero_fila, fila in enumerate(reader, start=2):
            try:
                if len(fila) < 3:
                    self.stdout.write(
                        self.style.WARNING(
                            f"Fila {numero_fila}: Datos incompletos, se omite: {fila}"
                        )
                    )
                    continue

                Ciudad.objects.create(
                    id=fila[0], estado_provincia_id=fila[1], nombre=fila[2]
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Error en fila {numero_fila}: {str(e)}")
                )

        archivo.close()
