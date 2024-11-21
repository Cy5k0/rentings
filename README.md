# Proyecto: Sitio Web para Arriendo de Inmuebles

#### [Ir a Hito 1](#hito-1) - [Ir a Hito 1/2](#hito-2) - [Ir a Hito 2/2](#hito-2-segunda-parte)

## Hito 1

Este proyecto tiene como objetivo desarrollar un sitio web para una empresa dedicada al arriendo de inmuebles, permitiendo a los usuarios revisar viviendas disponibles. El sistema utiliza **Django** como framework web y **PostgreSQL** como base de datos.

---

## Características del Proyecto

### 1. Instalación y Configuración del Ambiente de Desarrollo

- **PostgreSQL**: Configuración como sistema de base de datos.
- **Ambiente virtual de Python**: Aislamiento del entorno de desarrollo.
- **Paquetes necesarios**: Instalación de dependencias para trabajar con Django.
- **Aplicación Django**: Implementación de la lógica del sitio web.

### 2. Modelo de Datos

- **Modelo relacional**: Diseño de tablas relacionadas para inmuebles y sus atributos.
- **Conexión a PostgreSQL**: Configuración de la base de datos en `settings.py`.
- **Llaves primarias y foráneas**: Implementación para garantizar integridad referencial.

### 3. Operaciones CRUD en Django

- **Crear**: Añadir nuevos registros de inmuebles.
- **Leer**: Listar registros almacenados.
- **Actualizar**: Modificar información existente.
- **Eliminar**: Borrar registros específicos.

## Importante:

En el archivo **[hito1.pdf](hito1.pdf)** se encuentran los pantallazos solicitados en el hito 1

---

## Hito 2

# Gestión de Inmuebles - Panel Administrativo Django

## 📋 Descripción del Proyecto

Sistema de administración para empresa de arriendo de inmuebles, enfocado en gestionar eficientemente datos de inmuebles, regiones y comunas.

## 🎯 Objetivos

- Se crea panel de administración personalizado
- Se registra modelos de Inmueble, Región y Comuna, entre otros.
- Optimización de visualización y gestión de datos

## 📝 Requerimientos

### 1. Creación de Superusuario

- Generación de superusuario para acceso al panel
- Configurar:
- Nombre de usuario
- Correo electrónico
- Contraseña segura

### 2. Registro de Modelos en Admin

- Registrar en `admin.py`:
- Modelo Inmueble
- Modelo Región
- Modelo Comuna
- Método: `admin.site.register()`

### 3. Personalización del Panel

- Implementación configuraciones:
- `list_display`
- `search_fields`
- `list_filter`

### 4. Documentación

- Documentación proceso de configuración
- Incluir capturas de pantalla

**[Ver documento PDF](hito2.pdf)**

## 🛠️ Configuración del Proyecto

### Requisitos

- Python 3.x
- Django
- Entorno virtual

### Instalación

1. Clonar repositorio
2. Crear entorno virtual
3. Instalar dependencias
4. Realizar migraciones
5. Crear superusuario
6. Iniciar servidor de desarrollo

---

## Hito 2 (segunda parte)

# Sistema de Autenticación de Usuarios - Arriendo de Inmuebles

## 📌 Descripción del Proyecto

Sistema de autenticación para empresa de arriendo de inmuebles con funcionalidades de:

- Registro de usuarios
- Inicio y cierre de sesión
- Gestión de permisos y grupos

## 🛠 Requisitos Técnicos

### 1. Configuración de Autenticación

- Incluir en `INSTALLED_APPS`:
- `django.contrib.auth`
- `django.contrib.contenttypes`
- Configurar URLs de autenticación
- Crear superusuario

### 2. Vista de Registro

- Usar `UserCreationForm`
- Crear template HTML de registro
- Validar registro de usuarios

### 3. Vistas de Sesión

- Implementar `LoginView`
- Implementar `LogoutView`
- Crear templates de login/logout

### 4. Gestión de Permisos

- Configurar permisos por usuario
- Crear grupos con permisos específicos

## 🚀 Configuración Inicial

```bash
# Instalar dependencias
pip install django

# Migrar base de datos
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser
```

**[🖥️ Ver documento PDF](Hito2b.pdf)**

## 👥Integrantes:

- [Francisco Colomer](https://github.com/Cy5k0)
- [Arlenis González](https://github.com/agonzalezr92)
- [Francisco Monroy](https://github.com/fmonroy75)
