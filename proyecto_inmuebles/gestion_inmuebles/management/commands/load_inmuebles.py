import csv
from django.core.management.base import BaseCommand
from gestion_inmuebles.models import Inmueble, Ciudad, TipoInmueble, User


class Command(BaseCommand):
    help = "Carga inmuebles desde un archivo CSV"

    def handle(self, *args, **kwargs):
        try:
            archivo = open("data/inmuebles.csv", "r", encoding="utf-8")
            reader = csv.reader(archivo, delimiter=";")
            next(reader)  # Salta la cabecera del CSV

            for fila in reader:
                # Obtener o crear las relaciones necesarias
                ciudad = Ciudad.objects.get(id=fila[12])
                tipo_inmueble = TipoInmueble.objects.get(id=fila[18])
                propietario = User.objects.get(id=fila[19])

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

            self.stdout.write(self.style.SUCCESS("Inmuebles cargados exitosamente"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error al cargar inmuebles: {str(e)}"))
