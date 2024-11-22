import os
from django.core.management.base import BaseCommand
from gestion_inmuebles.models import Inmueble


class Command(BaseCommand):
    help = "Consulta listado de inmuebles para arriendo separado por comunas"

    def handle(self, *args, **options):
        inmuebles = (
            Inmueble.objects.all()
            .values("nombre", "descripcion", "ciudad__nombre")
            .distinct()
            .order_by("ciudad__nombre")
        )

        with open("inmuebles_por_comunas.txt", "w", encoding="utf-8") as archivo:
            comuna_actual = None
            for inmueble in inmuebles:
                if comuna_actual != inmueble["ciudad__nombre"]:
                    comuna_actual = inmueble["ciudad__nombre"]
                    if comuna_actual != inmuebles[0]["ciudad__nombre"]:
                        archivo.write("\n")
                    archivo.write(f"COMUNA {comuna_actual.upper()}\n")
                    archivo.write("═" * 50 + "\n")

                archivo.write(f"► {inmueble['nombre']}\n")
                archivo.write(f"  {inmueble['descripcion']}\n\n")
        self.stdout.write(
            self.style.SUCCESS(
                "Listado de inmuebles guardado en inmuebles_por_comunas.txt"
            )
        )
