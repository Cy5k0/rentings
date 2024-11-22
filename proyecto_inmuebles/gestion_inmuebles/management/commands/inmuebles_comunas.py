import os
from django.core.management.base import BaseCommand
from gestion_inmuebles.models import Inmueble


class Command(BaseCommand):
    help = "Consulta listado de inmuebles para arriendo separado por comunas"

    def handle(self, *args, **options):
        inmuebles = Inmueble.objects.all().values(
            "nombre", "descripcion", "ciudad__nombre"
        )
        with open("inmuebles_por_comunas.txt", "w", encoding="utf-8") as archivo:
            for inmueble in inmuebles:
                archivo.write(
                    f"Nombre: {inmueble['nombre']}, Descripción: {inmueble['descripcion']}, Comuna: {inmueble['ciudad__nombre']}\n"
                )
        self.stdout.write(
            self.style.SUCCESS(
                "Listado de inmuebles guardado en inmuebles_por_comunas.txt"
            )
        )
