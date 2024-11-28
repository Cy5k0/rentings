# Proyecto: Sitio Web para Arriendo de Inmuebles

# Start of Selection
#### [Ir a Hito 1](#hito-1) - [Ir a Hito 2.1](#hito-2) - [Ir a Hito 2.2](#hito-2-segunda-parte) - [Ir a Hito 3](#hito-3) - [Ir a Hito 4.1](#hito-41)

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

## Hito 3

## Descripción del Proyecto

Aplicación web para revisar inmuebles disponibles para arriendo, desarrollada para una empresa especializada en administración de propiedades.

## Requerimientos del Proyecto

### 1. Migraciones de Base de Datos

- Poblar base de datos con:
  - Regiones y comunas de Chile
  - Tipos de inmuebles
  - Inmuebles de ejemplo
  - Usuarios de ejemplo

### 2. Scripts de Consulta

#### Consulta de Inmuebles por Comuna

- Script Python para:
  - Conectarse a la base de datos usando Django y SQL
  - Recuperar campos "nombre" y "descripción" de inmuebles
  - Guardar resultados en archivo de texto

#### Consulta de Inmuebles por Región

- Script Python para:
  - Conectarse a la base de datos usando Django y SQL
  - Recuperar inmuebles agrupados por región
  - Guardar resultados en archivo de texto

## Tecnologías Utilizadas

- Python
- Django
- SQL
- Base de datos (especificada en el proyecto)

## Instrucciones de Instalación

1. Clonar repositorio
2. Configurar entorno virtual
3. Instalar dependencias
4. Configurar base de datos
5. Ejecutar migraciones
6. Poblar datos iniciales

**[🖥️ Ver documento PDF](Hito3.pdf)**

## Hito 4.1


Este proyecto tiene como objetivo desarrollar un sitio web basado en el patrón de diseño MVC que permita a los usuarios revisar inmuebles disponibles para arriendo y gestionar sus datos personales. El enfoque principal es implementar operaciones CRUD sobre un modelo previamente definido, integrando una capa de acceso a datos y construyendo vistas tanto para los usuarios como para la administración.

---

## Descripción del Proyecto

Una empresa dedicada al arriendo de inmuebles necesita un sitio web donde los usuarios puedan:

1. Consultar inmuebles disponibles para arriendo.
2. Registrarse, iniciar sesión y gestionar su información personal.
3. Modificar sus datos personales según corresponda.

---

## Requerimientos

### 1. Desarrollo de Vistas para Usuarios

- **Template básico**: Crear una página personalizada para Arrendatarios y Arrendadores que sirva como panel de control personal.
- **Vista de Login**: Crear una vista que permita a los usuarios iniciar sesión.
- **Vista de Registro**: Crear un formulario de registro de usuarios.
- **Redireccionamiento de URLs**: Implementar una funcionalidad que redirija a los usuarios según sus acciones (inicio de sesión, registro, etc.).
- **Visualización de datos**: Mostrar los datos personales del usuario en su página personalizada.

### 2. Modificación de Datos Personales

- Agregar funcionalidad para que tanto Arrendatarios como Arrendadores puedan editar sus datos personales desde sus páginas personalizadas.

---

## Tecnologías Utilizadas

- **Backend**: Implementación de operaciones CRUD mediante el patrón MVC.
- **Frontend**: Desarrollo de vistas personalizadas utilizando HTML, CSS y/o frameworks de diseño.
- **Base de Datos**: Uso de un modelo previamente diseñado y poblado con datos relevantes.
- **Framework**: Django.

---

## Instrucciones de Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/Cy5k0/rentings.git
   ```

2. Instalar dependencias:

```bash
  pip install -r requirements.txt
```

3. Iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

**[🖥️ Ver documento PDF](Hito4p1.pdf)**



## 👥Integrantes:

- [Francisco Colomer](https://github.com/Cy5k0)
- [Arlenis González](https://github.com/agonzalezr92)
- [Francisco Monroy](https://github.com/fmonroy75)
