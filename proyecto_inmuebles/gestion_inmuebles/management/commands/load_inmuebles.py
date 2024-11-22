import csv
from django.core.management.base import BaseCommand
from django.db.models import Q
from gestion_inmuebles.models import (
    Inmueble,
    Ciudad,
    TipoInmueble,
    User,
    PerfilUsuario,
    TipoUsuario,
)


class Command(BaseCommand):
    help = "Carga inmuebles desde un archivo CSV"

    def handle(self, *args, **options):
        try:
            # Obtener lista de arrendadores (tipo_usuario = 2 u 7) a través de PerfilUsuario
            arrendadores = set(
                User.objects.filter(perfil__tipo_usuario=7).values_list(
                    "username", flat=True
                )
            )
            print("Arrendadores encontrados:", arrendadores)

            contador = 0
            with open("data/inmuebles.csv", "r", encoding="utf-8") as archivo:
                filas = csv.reader(archivo, delimiter=";")
                next(filas)  # Saltar la cabecera

                for fila in filas:
                    propietario_id = fila[19].strip()
                    if propietario_id not in arrendadores:
                        raise Exception(
                            f"El usuario {propietario_id} no es un arrendador válido"
                        )

                    # Obtener o crear las relaciones necesarias
                    try:
                        ciudad = Ciudad.objects.get(id=fila[12])
                        tipo_inmueble = TipoInmueble.objects.get(id=fila[18])
                        propietario = User.objects.get(username=propietario_id)
                    except (
                        Ciudad.DoesNotExist,
                        TipoInmueble.DoesNotExist,
                        User.DoesNotExist,
                    ) as e:
                        raise Exception(f"Error al obtener relaciones: {str(e)}")

                    # Crear el inmueble
                    Inmueble.objects.create(
                        nombre=fila[0],
                        descripcion=fila[1],
                        m2_construidos=int(fila[2]),
                        m2_totales=int(fila[3]),
                        n_estacionamientos=int(fila[4]),
                        n_habitaciones=int(fila[5]),
                        n_baños=int(fila[6]),
                        precio=float(fila[7]),
                        moneda=fila[8],
                        calle=fila[10],
                        numero=fila[11],
                        ciudad=ciudad,
                        codigo_postal=fila[13],
                        latitud=float(fila[14]) if fila[14] else None,
                        longitud=float(fila[15]) if fila[15] else None,
                        disponible=bool(fila[16]),
                        tipo_inmueble=tipo_inmueble,
                        propietario=propietario,
                    )
                    contador += 1

            self.stdout.write(
                self.style.SUCCESS(f"Se cargaron {contador} inmuebles exitosamente")
            )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error al cargar inmuebles: {str(e)}"))
        finally:
            if "archivo" in locals():
                archivo.close()
