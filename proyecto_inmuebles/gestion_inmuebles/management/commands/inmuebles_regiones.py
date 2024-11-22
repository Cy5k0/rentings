# Consultar listado de inmuebles para arriendo separado por regiones en un script
# python que se conecta a la DB usando DJango y SQL guardando los resultados en un
# archivo de texto.

from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = "Consulta listado de inmuebles para arriendo separado por provincias usando SQL raw"

    def handle(self, *args, **options):
        # Consulta SQL raw para obtener inmuebles agrupados por provincia
        query = """
            SELECT 
                i.nombre,
                i.descripcion,
                p.nombre as provincia_nombre
            FROM gestion_inmuebles_inmueble i
            INNER JOIN gestion_inmuebles_ciudad c ON i.ciudad_id = c.id
            INNER JOIN gestion_inmuebles_estadoprovincia p ON c.estado_provincia_id = p.id
            ORDER BY p.nombre, i.nombre
        """

        with connection.cursor() as cursor:
            cursor.execute(query)
            inmuebles = cursor.fetchall()

            with open("inmuebles_por_provincias.txt", "w", encoding="utf-8") as archivo:
                provincia_actual = None
                for inmueble in inmuebles:
                    nombre, descripcion, provincia = inmueble

                    if provincia_actual != provincia:
                        provincia_actual = provincia
                        if (
                            provincia_actual != inmuebles[0][2]
                        ):  # compara con la primera provincia
                            archivo.write("\n")
                        archivo.write(f"PROVINCIA {provincia_actual.upper()}\n")
                        archivo.write("═" * 50 + "\n")

                    archivo.write(f"► {nombre}\n")
                    archivo.write(f"  {descripcion}\n\n")

        self.stdout.write(
            self.style.SUCCESS(
                "Listado de inmuebles guardado en inmuebles_por_provincias.txt"
            )
        )
