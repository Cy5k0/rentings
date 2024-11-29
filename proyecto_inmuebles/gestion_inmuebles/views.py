from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)  # get_object_or_404 para filtrar un elemento

from .models import PerfilUsuario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect
from .models import ContactForm
from .forms import (
    ContactFormForm,
    UserUpdateForm,
    PerfilUpdateForm,
    FotoInmuebleForm,
    InmuebleUpdateForm,
)

from django.contrib import messages
from .forms import RegistroForm
from django.contrib.auth import login

# from .forms import RegistroUser

# buscador
from django.http import JsonResponse
from .models import (
    Inmueble,
    Ciudad,
    ImagenInmueble,
    TipoInmueble,
    EstadoProvincia,
    Solicitud,
)
from django.http import JsonResponse
from .models import PerfilUsuario


# Create your views here.
def indice(request):
    inmuebles = Inmueble.objects.filter(disponible=True).order_by("?")[
        :6
    ]  # Selecciona 4 inmuebles aleatorios

    # fotos del inmueble
    inmuebles_con_imagenes = []
    for inmueble in inmuebles:
        imagen = ImagenInmueble.objects.filter(
            propiedad=inmueble
        ).first()  # Obtener solo la primera imagen
        inmuebles_con_imagenes.append(
            {
                "inmueble": inmueble,
                "imagen": imagen,
                "ciudad": inmueble.ciudad.nombre,
                "descripcion": inmueble.descripcion,
            }
        )

    context = {
        "inmuebles_con_imagenes": inmuebles_con_imagenes,
        # "ciudades": Ciudad.objects.all(),  # Para mostrar las ciudades en el menú desplegable
    }
    if request.user.is_authenticated:
        perfil = PerfilUsuario.objects.get(user=request.user)

        # Gurda el nombre de usuario y tipo de usuario en la sesion
        request.session["usuario"] = request.user.username
        request.session["tipo_usuario"] = perfil.tipo_usuario.tipo
        tipo_usuario = request.session.get("tipo_usuario")
        print(tipo_usuario)
        context = {
            "inmuebles_con_imagenes": inmuebles_con_imagenes,
            "usuario": request.session.get("usuario"),
            "tipo_usuario": tipo_usuario,
            # "ciudades": Ciudad.objects.all(),  # Para mostrar las ciudades en el menú desplegable
        }
        return render(
            request,
            "index.html",
            context,
            # {"usuario": request.session.get("usuario"), "tipo_usuario": tipo_usuario},
        )

        # return render(request, 'index.html', {'usuario': request.session.get('usuario'), 'tipo_usuario':tipo_usuario })

    return render(request, "index.html", context)


def contacto(request):
    if request.method == "GET":
        form = ContactFormForm()
    else:
        # para el formulario normal
        form = ContactFormForm(request.POST)
        # para el formulario modal
        # form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect("/exito/")

    return render(request, "contactoM.html", {"form": form})


def exito(request):
    return render(request, "exito.html")


def register(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("indice")
    else:
        form = RegistroForm()
    return render(
        request, template_name="registration/register.html", context={"form": form}
    )


def buscar_ciudades(request):
    query = request.GET.get("q", "")

    # Filtrar las ciudades con inmuebles disponibles
    if query:
        # inmuebles disponibles
        ciudades = Ciudad.objects.filter(
            nombre__icontains=query, inmueble__disponible=True
        ).distinct()
    else:
        ciudades = []

    # Construir la lista de resultados con la jerarquía de Ciudad -> Estado -> País
    resultados = [
        {
            "nombre": ciudad.nombre,
            "estado": ciudad.estado_provincia.nombre,
            "pais": ciudad.estado_provincia.pais.nombre,
            "id": ciudad.id,
        }
        for ciudad in ciudades
    ]

    return JsonResponse({"resultados": resultados})


def buscar_inmuebles(request):
    ciudad_id = request.GET.get("ciudad_id")

    if ciudad_id:
        # Filtrar inmuebles disponibles en la ciudad seleccionada
        inmuebles = Inmueble.objects.filter(ciudad_id=ciudad_id, disponible=True)
    else:
        inmuebles = Inmueble.objects.filter(
            disponible=True
        )  # listado de inmuebles de la ciudad seleccionada

    # fotos del inmueble
    inmuebles_con_imagenes = []
    for inmueble in inmuebles:
        imagenes = ImagenInmueble.objects.filter(propiedad=inmueble)
        inmuebles_con_imagenes.append({"inmueble": inmueble, "imagenes": imagenes})

    context = {
        "inmuebles_con_imagenes": inmuebles_con_imagenes,
        "ciudades": Ciudad.objects.all(),  # Para mostrar las ciudades en el menú desplegable
    }

    return render(request, "arriendos.html", context)


def arriendos(request):
    tusuario = request.session.get("tipo_usuario")
    if not tusuario:
        # Si no hay usuario en la sesión, redirigir al login
        return redirect("login")
    return render(request, "arriendos.html")


# actualizar datos del perfil
def misdatos(request):
    perfil = PerfilUsuario.objects.get(user=request.user)
    TIPOS_USUARIO = (
        # ("0", "Nulo"),
        ("1", "Arrendador"),
        ("2", "Arrendatario"),
        # ("3", "Administrador"),
    )
    # se envia por parametro los 2 modelos
    context = {
        "user": request.user,  # Datos del user de django
        "perfil": perfil,  # Datos perfilusuario
        # ,'tipo_usuario': tipousuario
    }
    return render(request, "misdatos.html", context)


@login_required
def update_profile(request):
    # Obtener o crear el perfil del usuario si no existe
    perfil, created = PerfilUsuario.objects.get_or_create(user=request.user)

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        perfil_form = PerfilUpdateForm(request.POST, instance=perfil)

        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            messages.success(request, "Tu perfil ha sido actualizado.")
            return redirect("misdatos")
            # return redirect("update_profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        perfil_form = PerfilUpdateForm(instance=perfil)

    context = {"user_form": user_form, "perfil_form": perfil_form}
    return render(request, "update_profile.html", context)


def mostrar_inmuebles(request):

    inmuebles = Inmueble.objects.filter(propietario=request.user)

    # fotos del inmueble
    inmuebles_con_imagenes = []
    for inmueble in inmuebles:
        print(inmueble.pk)
        imagenes = ImagenInmueble.objects.filter(propiedad=inmueble)
        tipoinmueble = inmueble.tipo_inmueble
        # tipoinmueble = TipoInmueble.objects.filter(TipoInmueble =inmuebles.tipo_inmueble)
        inmuebles_con_imagenes.append(
            {"inmueble": inmueble, "imagenes": imagenes, "tipoinmueble": tipoinmueble}
        )

    context = {
        "inmuebles_con_imagenes": inmuebles_con_imagenes,
        #        'ciudades': Ciudad.objects.all()  # Para mostrar las ciudades en el menú desplegable
    }

    return render(request, "propiedades.html", context)


def add_inmuebles(request):
    if request.method == "POST":
        print(request.POST)
        print("request")

        # <QueryDict: {'csrfmiddlewaretoken': ['jAozsiNu8dx7lnLzDfb3xRg9w2grR04JeFQ8zPvmG6vFEgABW0KbBI9QXtezhzkw'], 'nombre': ['propiedadX'], 'descripcion': ['x'], 'm2_construidos': ['56'], 'm2_totales': ['456'], 'n_estacionamientos': ['2'], 'n_habitaciones': ['2'], 'n_baños': ['1'], 'precio': ['23432432'], 'moneda': ['USD'], 'calle': ['gncbcbncv'], 'numero': ['54'], 'pais': ['5'], 'estado_provincia': ['1833'], 'ciudad': ['565420'], 'codigo_postal': ['5635653'], 'tipo_inmueble': ['1'], 'data_submit': ['']}>

        # {'nombre': "['propiedadX']", 'descripcion': "['X']", 'calle': "['por ahi']", 'numero': "['77']", 'codigo_postal': "['5310144']"}

        formInmueble = InmuebleUpdateForm(request.POST)
        # print(formInmueble)
        if formInmueble.is_valid():

            inmueble = formInmueble.save(commit=False)
            inmueble.propietario = request.user
            # Asegurando de que los campos estén correctamente asignados Probando fix
            inmueble.ciudad = formInmueble.cleaned_data["ciudad"]
            inmueble.estado_provincia = formInmueble.cleaned_data["estado_provincia"]
            inmueble.pais = formInmueble.cleaned_data["pais"]
            inmueble.save()
            # print("graba")
            messages.success(request, "Tu inmueble ha sido actualizado.")
            return redirect("dashboard_prop")
        else:
            print(formInmueble.errors)
            messages.error(request, "Hay errores en los datos")
    else:
        # formInmueble = InmuebleUpdateForm(instance=request.user)
        formInmueble = InmuebleUpdateForm()
    #  return redirect("dashboard_prop")
    context = {"formInmueble": formInmueble}
    return render(request, "add_propiedad.html", context)


def cargar_estados(request):
    pais_id = request.GET.get("pais_id")
    estados = EstadoProvincia.objects.filter(pais_id=pais_id).order_by("nombre")
    return JsonResponse(list(estados.values("id", "nombre")), safe=False)


def cargar_ciudades(request):
    estado_id = request.GET.get("estado_id")
    ciudades = Ciudad.objects.filter(estado_provincia_id=estado_id).order_by("nombre")
    return JsonResponse(list(ciudades.values("id", "nombre")), safe=False)


def mostrar_un_inmuebles(request, inmueble_id):

    inmuebles = get_object_or_404(Inmueble, pk=inmueble_id, propietario=request.user)

    if request.method == "POST":
        if "foto_submit" in request.POST:
            form = FotoInmuebleForm(request.POST, request.FILES)
            files = request.FILES["imagen"]

            if form.is_valid():

                imagen = form.cleaned_data["imagen"]
                ImagenInmueble.objects.create(propiedad=inmuebles, imagen=imagen)
                messages.success(request, "La foto se ha agregado correctamente.")
                return redirect("dashboard_prop")
                # return redirect(
                #     "mostrar_un_inmuebles", inmueble_id=inmueble_id
                # )  # Redirigir a mostrar detalles
            else:
                messages.error(request, "Hubo un error al intentar guardar la imagen.")

        elif "data_submit" in request.POST:
            form = InmuebleUpdateForm(request.POST, instance=inmuebles)
            if form.is_valid():
                print("entro")
                form.save()
                messages.success(request, "Tu perfil ha sido actualizado.")
                return redirect("mostrar_un_inmuebles", inmueble_id=inmueble_id)
            else:
                messages.error(request, "Hay errores en los datos")
    else:
        form = FotoInmuebleForm()

    # fotos del inmueble
    print(inmuebles.pk)
    imagenes = ImagenInmueble.objects.filter(propiedad=inmuebles)
    tipoinmueble = inmuebles.tipo_inmueble
    form = FotoInmuebleForm()
    formInmueble = InmuebleUpdateForm(instance=inmuebles)

    # tipoinmueble = TipoInmueble.objects.filter(TipoInmueble =inmuebles.tipo_inmueble)
    context = {
        "inmueble": inmuebles,
        "imagenes": imagenes,
        "tipoinmueble": tipoinmueble,
        "form": form,
        "formInmueble": formInmueble,
    }

    return render(request, "add_fotoinmueble.html", context)


# ----solicitudes


def request_property(request, id_propiedad):
    usuario = request.user
    propiedad = Inmueble.objects.get(id=id_propiedad)

    if request.method == "POST":
        nueva_solicitud = Solicitud.objects.create(inmueble=propiedad, usuario=usuario)

        return redirect("/my_requests")

    else:
        return redirect("/my_requests")


def my_requests(request):
    usuario = request.user
    solicitudes = Solicitud.objects.filter(usuario=usuario)

    return render(
        request=request,
        template_name="my_requests.html",
        context={"solicitudes": solicitudes},
    )


def delete_request(request, solicitud_id):
    if request.method == "POST":
        solicitud = Solicitud.objects.get(id=solicitud_id)
        solicitud.delete()
        return redirect("/my_requests")
    else:
        return redirect("/my_requests")


# arrendador


def my_requests_owner(request):
    # Obtener el usuario logueado
    usuario = request.user

    # Filtrar las solicitudes donde el propietario del inmueble es el usuario logueado
    solicitudes = Solicitud.objects.filter(inmueble__propietario=usuario)

    # Pasar la información al contexto para renderizar la página
    context = {
        "solicitudes": solicitudes,
    }

    return render(request, "my_requests_owner.html", context)


def accept_request(request, solicitud_id):
    if request.method == "POST":
        solicitud = Solicitud.objects.get(id=solicitud_id)
        solicitud.estado = "aceptada"
        solicitud.save()

        inmueble = solicitud.inmueble
        inmueble.disponible = False
        inmueble.save()

        # messages.success(request, 'Solicitud eliminada correctamente.')
        return redirect("/my_requests_owner")
    else:
        return redirect("/my_requests_owner")


def reject_request(request, solicitud_id):
    if request.method == "POST":
        solicitud = Solicitud.objects.get(id=solicitud_id)
        solicitud.estado = "rechazada"
        solicitud.save()
        # messages.success(request, 'Solicitud eliminada correctamente.')
        return redirect("/my_requests_owner")
    else:
        return redirect("/my_requests_owner")


def habilitar_request(request, inmueble_id):
    if request.method == "POST":
        solicitud = Solicitud.objects.get(inmueble_id=inmueble_id, estado="aceptada")
        solicitud.estado = "Finalizada"
        solicitud.save()

        inmueble = solicitud.inmueble
        inmueble.disponible = True
        inmueble.save()

        # messages.success(request, 'Solicitud eliminada correctamente.')
        return redirect("/dashboard_prop")
    else:
        return redirect("/dashboard_prop")


# -------------------------------------------------------------
