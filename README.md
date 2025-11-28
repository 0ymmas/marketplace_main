# **Práctica Evaluatoria – Parcial 3**

**Centro de Bachillerato Tecnológico Industrial y de Servicios No. 116**
**Materia:** Construye Aplicaciones Web
**Profesor:** José Christian Romero Hernández
**Grupo:** 5 AMPG
**Fecha:** 28 de noviembre de 2025

**Integrantes:**

* Gutiérrez Morales Mayte
* Montiel Rueda Francisco Ezequiel
* Ontiveros Castillo Janneth
* Ortega Robles Madeline Michelle
* Torres Peña Ángeles

---

# **Índice**

1. [Introducción](#introducción)
2. [Comandos](#comandos)
3. [Diagrama](#diagrama)
4. [Archivos y Funciones](#archivos-y-funciones)

   * Forms.py
   * Settings.py
   * Urls.py
   * Models.py
   * Views.py
   * Decorador @login_required
   * Templates (Item.html, Login.html, Signup.html, Navigation.html, Form.html)
5. [Ejecución del Proyecto](#ejecución-del-proyecto)
6. [Conclusiones](#conclusiones)

---

# **Introducción**

En el desarrollo de nuestra aplicación web, utilizar Django como herramienta es algo nuevo para nosotros. Sin embargo, nos pareció una herramienta muy acertada ya que nos proporciona todo lo que necesitamos y nos facilita la ejecución y la comprensión del código.

Django es una herramienta bastante completa para nuestro trabajo en equipo y bastante funcional en base a lo que hemos estado creando. Esta parte del proyecto nos demostró la funcionalidad de Django y como aprovecharla lo mejor posible, ya que es la herramienta ideal para aprender y crear aplicaciones web reales, funcionales y bien estructuradas

— 

En esta fase del proyecto continuamos trabajando con Django, aprovechando la experiencia que ya teníamos para realizar mejoras significativas en nuestra aplicación web. El objetivo principal fue ampliar la funcionalidad del sitio, optimizando rutas, vistas, formularios y plantillas para que la plataforma funcionará de manera más completa y organizada. Esto nos permitió reforzar conocimientos previos y profundizar en cómo se interconectan los distintos componentes de Django.

Durante el desarrollo realizamos actualizaciones importantes, como la incorporación de rutas para el registro, inicio y cierre de sesión, y la publicación de productos. También trabajamos en la personalización de formularios y la gestión de modelos, lo que nos ayudó a entender mejor cómo Django maneja los datos y cómo estos se muestran al usuario. Cada cambio realizado contribuyó a que la aplicación se acercara más a un marketplace funcional y atractivo.

Además, la experiencia de trabajar en equipo fue clave para implementar estas mejoras. Compartir documentos con comandos, códigos y explicaciones nos permitió mantener un flujo de trabajo organizado y resolver problemas más rápido. Gracias a esta etapa, reforzamos nuestras habilidades en Django y adquirimos más confianza para desarrollar proyectos web más complejos y completos en el futuro.

---

# **Comandos**

```text
1. cd + documents                -> abrir documentos
2. md + nombre_carpeta           -> crear carpeta
3. cd + nombre_carpeta           -> abrir carpeta
4. python -m venv venv           -> crear ambiente virtual
5. venv\Scripts\activate         -> activar ambiente virtual
6. pip install django            -> instalar Django
7. pip list                      -> verificar instalación
8. django-admin startproject     -> crear proyecto
9. django-admin startproject marketplace_main
10. python manage.py migrate     -> crear tablas
11. python manage.py createsuperuser -> crear superusuario
12. python manage.py runserver   -> levantar servidor
```

---

# **Diagrama**

![Diagrama de flujo](img/diagrama.png)

---

# **Archivos y Funciones**

## **Forms.py**

En el archivo forms.py del apartado store lo que hago es definir los formularios que se usan para que los usuarios puedan iniciar sesión y registrarse, en  vez de crear todo desde cero, aprovechó los formularios que Django ya trae para autenticación y registro, y simplemente los personalizo para que se vean mejor en mi proyecto, él lo que es el formulario (Login Form),  cambio los campos de usuario y contraseña para agregarles placeholders y clases de Bootstrap, así los inputs se ven más ordenados y con diseño moderno, no modificó la lógica del inicio de sesión, solo la apariencia.

Por otra parte el formulario de registro (Signup Form), hago algo parecido, usó el formulario estándar de Django para crear usuarios, pero ajustó los campos para que tengan el estilo que quiero y también agrego placeholders que sirve como una pequeña guía o pista para indicar qué debe escribirse ahí, además, especificó que este formulario trabaja con el modelo “User” y los campos que quiero mostrar. En otras palabras, este archivo se encarga de darle estilo y mejorar la presentación de los formularios de login y registro, manteniendo la funcionalidad original que Django ya provee, es básicamente la capa que hace que los formularios se vean bien y sean más cómodos de usar.

### **Código:**

```
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Item


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Tu usuario',
            'class': 'form-control'
        }
    ))


    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password',
            'class': 'form-control'
        }
    ))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Tu Usuario',
            'class': 'form-control'
        }
    ))


    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Tu Email',
            'class': 'form-control'
        }
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password',
            'class': 'form-control'
        }
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Repite Password',
            'class': 'form-control'
        }
    ))

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)

        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'height: 100px'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }

```

---

## **Settings.py**

El archivo settings.py sirve para guardar toda la configuración principal de un proyecto hecho con Django. Básicamente, es el archivo donde se definen las reglas que el proyecto necesita para funcionar bien. 
Dentro de este archivo se pueden cambiar muchas cosas, por ejemplo:

**La base de datos:** que es donde se guarda la información del proyecto. Ahí se indica si se va a usar SQLite, MySQL u otra. 
**Las aplicaciones instaladas:** son las partes o módulos del proyecto que Django necesita para trabajar. 
**El idioma y la zona horaria:** para adaptar el proyecto al país o idioma que queramos usar. 
**Los archivos estáticos:** como las imágenes, los estilos (CSS) o los scripts (JavaScript). 
**Temas de seguridad:** como la clave secreta (SECRET_KEY) o los dominios que pueden acceder al proyecto.

![Codigo Pt1](img/imagen1.png)
![Codigo Pt2](img/imagen2.png)
![Codigo Pt3](img/imagen3.png)
![Codigo Pt4](img/imagen4.png)
![Codigo Pt5](img/imagen5.png)

– Actualización 

El archivo settings.py sirve para guardar toda la configuración principal de un proyecto hecho con Django. Básicamente es el archivo donde se definen las reglas que el proyecto necesita para funcionar bien.

La primera actualización del código fue esta: Sirve para que Django sepa donde guardar la información de la base de datos. 

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
En la actualización se agregó la parte de templates:Sirve para que podamos buscar y usar archivos HTML desde las aplicaciones o desde carpetas personalizadas.
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

En la actualización se agregó este código: Sirve para conectar a Django con servidores web 
```
WSGI_APPLICATION = 'marketplace_main.wsgi.application'
```

En la actualización se agregó este código: Sirve para controlar a donde se manda al usuario al estar registrado, o cuando inicia o cierra sesión
```
ALLOWED_HOSTS = []
LOGIN_URL = '/store/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

---

## **Urls.py**

La actualización del archivo urls.py añadió varias rutas nuevas que mejoran bastante cómo funciona el sitio, especialmente en todo lo que tiene que ver con usuarios y productos. Ahora existen rutas para registrarse, iniciar sesión, cerrar sesión y agregar un nuevo artículo, mientras que la ruta para ver el detalle de un producto sigue igual. Con estos cambios, el proyecto ya cuenta con un sistema más completo para manejar cuentas y publicaciones.
La ruta de registro permite que cualquier persona cree su cuenta, y la de inicio de sesión sirve para que los usuarios entren a la suya sin problema. También se agregó la opción de cerrar sesión, que es importante para mantener la seguridad de cada cuenta. Además, la posibilidad de agregar productos es clave para que los usuarios puedan publicar lo que quieran vender dentro del marketplace.
En conjunto, estas mejoras son necesarias para que la plataforma funcione realmente como un marketplace seguro y fácil de usar. Contar con la gestión de usuarios y productos ayuda a que cada persona pueda manejar su información, comprar, vender y controlar todo desde su cuenta. Gracias a estas rutas, la navegación del sitio queda más organizada y completa, cubriendo todo lo que un usuario necesita para interactuar con la página.

![](img/imagen6.png)
![](img/imagen7.png) 

— Actualización

Con las recientes modificaciones en urls.py, se añadieron varias rutas nuevas que mejoran la funcionalidad de la plataforma:
- La ruta register/ permite a los usuarios crear una cuenta nueva.
- La ruta login/ utiliza la vista de autenticación de Django con un formulario personalizado (LoginForm) para que los usuarios puedan iniciar sesión.
- La ruta logout/ cierra la sesión del usuario, asegurando que la información personal quede protegida.
- La ruta add_item/ permite a los usuarios registrados publicar nuevos productos en el marketplace.
- La ruta detail/<int:pk>/ sigue mostrando los detalles de un producto específico.
- La ruta contact/ muestra la página de contacto para consultas o sugerencias.

Gracias a estas actualizaciones, el archivo urls.py permite que la aplicación funcione de manera más completa, organizada y segura. Contar con rutas claras para la gestión de usuarios y productos facilita la navegación, mejora la experiencia del usuario y asegura que cada acción se procese correctamente según el tipo de solicitud. En conjunto, estas mejoras son clave para que el marketplace funcione como un sitio dinámico y confiable.
```
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import contact, detail, register, logout_user, add_item
from .forms import LoginForm

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='store/login.html',
        authentication_form=LoginForm
    ), name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_item/', add_item, name='add_item'),
    path('detail/<int:pk>/', detail, name='detail'),
]
```

## **Models.py**

En lo que hemos estado trabajando usando Django, el archivo models.py es el que se encarga de definir cómo se va a guardar toda la información que estamos usando. No se guardan los datos directamente ahí como tal pero sí se explica qué tipo de datos van a estar y cómo se van a organizar. Básicamente, cada clase que se crea ahí dentro es como una tabla en la base de datos, y cada. El atributo dentro de esa clase es una columna que guarda un tipo de información.

En el código que tenemos existen dos modelos: "Category" e "Item". El modelo Category representa las categorías que pueden tener los artículos. Solo tiene un campo llamado name, que guarda el nombre de cada categoría. Después está Item, que representa los artículos o productos que estarán dentro de las categorías. Desde el nombre del artículo, precio, descripción, etc.

También uso algo llamado "llave foránea" que básicamente conecta una tabla con otra. En este caso, el campo Category dentro del modelo Item conecta cada artículo con su categoría, y en el campo "create_by" hace que se nos permita seleccionar al usuario o la persona que creo o agrego el artículo.Otra cosa que me gusta de este archivo es que no tengo que crear las tablas manualmente y que es más fácil y rápido hacer todo eso porque Django se encarga de eso con los comandos como lo son "makemigrations" y "migrate" Y ya solo definimos las clases y los campos en models.py, y las convierte en tablas reales dentro de la base de datos.

![](img/imagen8.png)
![](img/imagen9.png)

—Actualización

En nuestro proyecto tenemos dos modelos principales: Category e Item. El modelo Category guarda el nombre de cada categoría y Django organiza automáticamente estas categorías alfabéticamente gracias a la configuración interna del modelo. Por su parte, el modelo Item representa los artículos o productos, incluyendo datos como el nombre, una descripción opcional, el precio, la posibilidad de subir una imagen, si ya fue vendido y la fecha de creación, que Django registra automáticamente, además, Item utiliza llaves foráneas para relacionarse con otros modelos: la primera, category, conecta cada artículo con su categoría; la segunda, created_by, relaciona cada artículo con el usuario que lo creó.
Lo mejor de trabajar con Django es que solo necesitamos definir estas clases y sus campos, y luego el framework se encarga de crear las tablas reales en la base de datos usando los comandos makemigrations y migrate, lo que simplifica enormemente la gestión de la información sin necesidad de escribir SQL manualmente.
```
from django.contrib.auth.models import User
from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)  # <-- minúscula
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)  # <-- nombre corregido
    created_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.name
```

---

## **Views.py**

El archivo views.py es un componente en Django que está diseñado para gestionar la lógica de presentación y controlar el flujo de información entre el usuario y el sistema. El propósito principal de views.py es definir 'vistas', que son funciones o clases que se encargan de recibir lo que pide el usuario por internet y devolverle una respuesta.
El archivo nos permite implementar la lógica de negocio relacionada con la presentación de datos, manejar la interacción del usuario, procesar formularios y controlar el acceso a diferentes recursos. Estas vistas que se contienen en este archivo son las encargadas de determinar qué información se muestra al usuario
y bajo qué condiciones. 
Funciona en coordinación con otros componentes de Django: recibe las solicitudes que salen por el sistema de URLs, interactúa con los modelos para
acceder a los datos, y utiliza las plantillas para estructurar la presentación final. Si se implementa de forma correcta, es decir mucha ayuda ya que permite crear
aplicaciones web dinámicas y responsive, facilitando el mantenimiento del código y la escalabilidad del proyecto.Lo que hace es juntar en un solo lugar todo lo que
se necesita de la aplicación para entender lo que el usuario está pidiendo y armarle una respuesta que tenga sentido y vaya concorde al tema.

![](img/imagen10.png)
![](img/imagen10.png)

— Actualización  

En nuestro caso nos funcionó para cosas necesarias como las siguientes:

![](img/imagen10.png)

Ese código es la vista home() de Django y sirve para cargar la página principal de la tienda: obtiene de la base de datos todos los productos que no están vendidos y todas las categorías, mete esa información en un contexto y luego la envía al template home.html para mostrarla al usuario.

![](img/imagen10.png)

Ese código define la vista contact(), y su función es simplemente mostrar la página de contacto.
Crea un contexto con un mensaje ('Quieres otros productos contactame!') y lo envía al template contact.html, para que ese texto se muestre allí cuando el usuario abra la página.

![](img/imagen10.png)

Esa vista detail() sirve para mostrar la página de detalle de un producto.
Primero busca el producto con el pk dado (o muestra 404 si no existe). Luego obtiene hasta 3 productos relacionados que sean de la misma categoría y que no estén vendidos, excluyendo el actual. Finalmente envía al template item.html tanto el producto como sus relacionados para mostrarlos en la página.

![](img/imagen10.png)

Esa vista register() maneja el registro de nuevos usuarios.
Si el usuario envía el formulario (método POST), crea un SignupForm con los datos, lo valida y, si es correcto, guarda al nuevo usuario y redirige a la página de login.
Si es una visita normal (GET), simplemente muestra un formulario vacío.
Al final, siempre envía el formulario al template signup.html para mostrarlo en la página.

![](img/imagen10.png)

Esa vista logout_user() cierra la sesión del usuario.
Llama a logout(request) para desconectarlo y luego lo redirige a la página principal (home).

![](img/imagen10.png)

Esa vista add_item(), protegida con @login_required, permite que solo usuarios logueados puedan agregar productos.
Si el usuario envía el formulario (POST), crea un NewItemForm, valida los datos, asigna el producto al usuario que lo creó (created_by), lo guarda y luego redirige a la página de detalle del nuevo item.
Si es una visita normal (GET), muestra un formulario vacío.
Finalmente manda el formulario y un título al template form.html para que se muestre en pantalla.

---

## **Decorador @login_required**

El decorador **@login_required** es una función proporcionada por Django que se utiliza para garantizar que una vista (función o método) solo sea accesible para los usuarios que están autenticados en el sistema. Esto es especialmente útil en aplicaciones donde algunas acciones deben estar restringidas solo a usuarios que hayan iniciado sesión, como agregar un nuevo artículo o acceder a información privada.

**Funcionamiento:**
Cuando aplicamos **@login_required** sobre una vista, Django verifica si el usuario está autenticado antes de permitirle el acceso a la vista. Si el usuario no está autenticado, Django lo redirige automáticamente a la página de inicio de sesión, para que inicie sesión antes de acceder a esa vista.
Si el usuario está autenticado, entonces Django procesa la vista normalmente y el usuario puede realizar la acción correspondiente.

-**Decorador @login_required**
En la primera línea, se importa el decorador **@login_required** de Django:
from django.contrib.auth.decorators import login_required
Este decorador se aplica sobre la vista **add_item** para asegurarse de que solo los usuarios que han iniciado sesión puedan acceder a la funcionalidad de agregar un nuevo artículo. Si un usuario no está autenticado, Django lo redirige automáticamente a la página de inicio de sesión.

-**La Vista add_item**
La función **add_item** es la vista encargada de manejar el proceso de agregar un nuevo artículo al sistema. Esta vista recibe un objeto **request**, que contiene la información de la solicitud HTTP realizada por el usuario.
```
@login_required
def add_item(request):
```
-**Procesamiento del Formulario (Método POST)**
Si la solicitud es POST, se crea una instancia del formulario NewItemForm usando los datos enviados en la solicitud (request.POST y request.FILES):
```
if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
```
Después, se valida el formulario con form.is_valid(). Si el formulario es válido, significa que los datos proporcionados cumplen con los requisitos del formulario.
   ```
 if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
```

El artículo se guarda en la base de datos, y se asocia al usuario que está autenticado (es decir, el que ha iniciado sesión). Esto se hace con:
```
item.created_by = request.user
```
Una vez guardado el artículo, el usuario es redirigido a la página de detalles del artículo recién creado:
```
    return redirect('detail', pk=item.id)
```
-**Mostrar el Formulario (Método GET)**
Si la solicitud no es POST, significa que el usuario está viendo el formulario para agregar un nuevo artículo. En este caso, se crea un formulario vacío y se prepara el contexto para mostrarlo en la plantilla:
```
 else:
        form = NewItemForm()
        context = {
            'form': form,
            'title': 'New Item'
        }
Finalmente, el formulario vacío se renderiza dentro de la plantilla store/form.html, y se pasa el contexto con el formulario y el título de la página:
  return render(request, 'store/form.html', context)
```

---

## **Templates/store**
La carpeta templates/store guarda los archivos que definen el diseño de la tienda en línea, es como el "molde" que determina cómo se ven las páginas, como la de inicio o el carrito de compras.
Su función principal es dar un diseño uniforme y profesional, las plantillas permiten personalizar fácilmente la apariencia sin afectar la funcionalidad, además, es útil para cambiar el aspecto de toda la tienda sin complicaciones, especialmente en plataformas como shopify o woocommerce y lo mejor es que reutiliza elementos, como botones o encabezados, para que sea más fácil mantener el sitio actualizado.

![](img/imagen10.png)

Es la página donde se muestra un producto individual de tu tienda. Cuando alguien da click en un artículo, Django carga este template y aquí se ve todo: la imagen, el precio, la descripción e inclusive otros productos parecidos 
Usa tu plantilla base (base.html) para mantener el estilo. Muestra la imagen del producto (o una imagen por defecto si no tiene). Enseña el nombre, precio y descripción. Abajo pone una sección de “productos relacionados” que vienen de la misma categoría. Tiene un botón arriba para regresar a la lista de productos.
Básicamente, es la página de detalle del producto, justo como en cualquier tienda online.

**Código:**
```
{% extends 'store/base.html' %}
{% block title %} {{ item.name }} | {% endblock %}
{% block content %}
<div class="container my-4">
    <a href="{% url 'home' %}" class="btn btn-secondary mb-3">&larr; Volver a Productos</a>


    <div class="row">
        <div class="col-md-6">
            {% if item.image %}
            <img src="{{ item.image.url }}" class="img-fluid rounded shadow" alt="{{ item.name }}">
            {% else %}
            <img src="https://via.placeholder.com/500x400?text=Sin+Imagen" class="img-fluid rounded shadow" alt="{{ item.name }}">
            {% endif %}
        </div>
        <div class="col-md-6">
            <h2>{{ item.name }}</h2>
            <p class="h4 text-primary">{{ item.price }} USD</p>
            <p>{{ item.description|default:"No hay descripción" }}</p>


            {% if related_items %}
            <h5 class="mt-4">Productos relacionados</h5>
            <div class="d-flex flex-wrap gap-2">
                {% for r in related_items %}
                <a href="{% url 'detail' r.pk %}" class="btn btn-outline-primary btn-sm">{{ r.name }}</a>
                {% endfor %}
            </div>
            {% endif %}
        </div>
    </div>
</div>
{% endblock %}
```
---
##**Login.html:**
El archivo login.html dentro de templates/store tiene funciones específicas que están relacionadas con el flujo de autenticación y la experiencia del usuario cuando intenta iniciar sesión en la aplicación. Su función principal es proporcionar la interfaz de usuario para el inicio de sesión, gestionar los datos enviados y, en última instancia, permitir que los usuarios autenticados accedan a las funcionalidades protegidas de marketplace.
El archivo login.html se encarga de renderizar un formulario de inicio de sesión que solicita al usuario su nombre de usuario y contraseña. Estos datos se envían al servidor para ser validados. En el proceso de autenticación, si el usuario introduce credenciales correctas, se le permite acceder a la plataforma y utilizar las funcionalidades como agregar productos, hacer compras, o gestionar su perfil. Si las credenciales son incorrectas, la plantilla maneja los errores y los muestra al usuario de manera clara para que pueda corregirlos.
La plantilla también es responsable de garantizar que el diseño y la experiencia de usuario sean consistentes con el resto del sitio, ya que extiende la plantilla base base.html. Esto asegura que el formulario de inicio de sesión se vea y funcione de manera coherente con el resto de las páginas del marketplace.
Finalmente, el archivo login.html es importante para la redirección dentro de la aplicación. Una vez que el usuario se autentica correctamente, es redirigido a la página que había intentado acceder originalmente, como lo es la  página principal.

**Código:**

```
% extends 'store/base.html' %}
{% block title %}Login| {% endblock %}
{% block content %}
<div class="row p-4">
    <div class="col-6 bg-light p-4">
        <h4 class="mb-6 text-center">Registro</h4>
        <hr>
        <form action="." method="POST">
            {% csrf_token %}
            <div class="form-floating mb-3">
                <h6>Username:</h6>
                {{form.username}}
            </div>
            <div class="form-floating mb-3">
                <h6>Password:</h6>
                {{form.password}}
            </div>
        </form>
    </div>
    {% if form.errors or form.non_field_errors %}
    <div class="mb-4 p-6 bg-danger">
        {% for field in form %}
            fiels.errors
        {% endfor %}
        {{ form.non_field_errors }}
    </div>
    {% endif %}
</div>
<button class="btn btn-primary mb-6">Login</button>
{% endblock %}
```
---
##**Signup.html:**
El archivo signup.html es una plantilla de Django utilizada para gestionar el registro de nuevos usuarios en un sitio web. Su propósito principal es proporcionar una interfaz visual en la que los usuarios puedan crear una cuenta para acceder a las funcionalidades del sitio. En el contexto de un proyecto de tipo marketplace, como el que parece ser markentplace_main, el formulario de registro es una parte fundamental del proceso de creación de cuentas, lo que permite a los usuarios registrarse, acceder a su perfil, y realizar transacciones o agregar productos a la plataforma.
En nuestro proyecto, el archivo signup.html tiene la función de interactuar con el formulario de registro del sistema, procesando las solicitudes de los usuarios que desean crear una cuenta. El formulario solicita datos básicos como el nombre de usuario, correo electrónico, y una contraseña (con su confirmación), los cuales se validan antes de proceder con la creación de la cuenta. 
El uso del {% csrf_token %} dentro del formulario es una medida de seguridad que protege al sitio contra ataques de tipo CSRF, asegurando que los datos solo sean enviados desde el mismo sitio web. Además, se manejan los errores de validación, de modo que si los usuarios cometen algún error, como escribir contraseñas que no coinciden, el sistema les proporciona retroalimentación para corregirlo.

**Formulario de Registro:**

```
<form action="." method="POST">
    {% csrf_token %}
    <div class="form-floating mb-3">
        <h6>Username:</h6>
        {{ form.username }}
    </div>
    <div class="form-floating mb-3">
        <h6>Email:</h6>
        {{ form.email }}
    </div>
    <div class="form-floating mb-3">
        <h6>Password:</h6>
        {{ form.password1 }}
    </div>
    <div class="form-floating mb-3">
        <h6>Repite Password:</h6>
        {{ form.password2 }}
    </div>
   
    {% if form.errors or form.non_field_errors %}
        <div class="mb-4 p-6 bg-danger">
            {% for field in form %}
                fields.errors
            {% endfor %}
            {{ form.non_field_errors }}
        </div>
    {% endif %}
   
    <button class="btn btn-primary mb-6">Register</button>
</form>
```

**Código:**
```
{% extends 'store/base.html' %}
{% block title %}Registro| {% endblock %}
{% block content %}
<div class="row p-4">
    <div class="col-6 bg-light p-4">
        <h4 class="mb-6 text-center">Registro</h4>
        <hr>
        <form action="." method="POST">
            {% csrf_token %}
            <div class="form-floating mb-3">
                <h6>Username:</h6>
                {{form.username}}
            </div>
            <div class="form-floating mb-3">
                <h6>Email:</h6>
                {{form.email}}
            </div>
            <div class="form-floating mb-3">
                <h6>Password:</h6>
                {{form.password1}}
            </div>
            <div class="form-floating mb-3">
                <h6>Repite Password:</h6>
                {{form.password2}}
            </div>


            {% if form.errors or form.non_field_errors %}
                <div class="mb-4 p-6 bg-danger">
                    {% for field in form %}
                        fields.errors
                    {% endfor %}
                    {{ form.non_field_errors }}
                </div>
            {% endif %}


            <button class="btn btn-primary mb-6">Register</button>
        </form>
    </div>
</div>
{% endblock %}
```
---
##**Navigation.html:** 

El archivo navigation.html en un repositorio de GitHub es un archivo HTML que contiene el código para la barra o menú de navegación de un sitio web. No es un archivo especial para GitHub en sí mismo, sino un archivo estándar utilizado en el desarrollo web.

En nuestro proyecto el documento de navigation.html tiene la función de crear una barra de navegación en HTML usando bootstrap como guía y base; Al usar bootstrap para esta parte también nos ayuda a que al momento de usar nuestra página completa en diferentes dispositivos (computadora/teléfono/tablet/etc) esta barra se adapte al tamaño del dispositivo en cuestión, además de que en dispositivos pequeños se pueda expandir o minimizar según sea el caso.  

Además cuenta con un botón que te redirige a la pantalla home directamente, un apartado de contacto que te lleva directamente a la página de contacto. Si el usuario está registrado se muestra el apartado de “add item” para agregar un articulo nuevo, si está registrado y quiere salir también se muestra el botón “logout” para salir de esa sesión, en caso contrario, si no ha iniciado sesión seleccionando el botón de “login” o “register”. 

```
<nav class="navbar navbar-expand-lg bg-dark" data-bs-theme="dark">
    <div class="container-fluid">
        <a href="{% url 'home' %}" class="navbar-brand">Marketplace</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-control="navBarNav" aria-expanded="false" aria-label="Toggle Navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a href="" class="nav-link active">
                        Home
                    </a>
                </li>
                <li class="nav-item">
                    <a href="{% url 'contact' %}" class="nav-link active">
                        Contact
                    </a>
                </li>
               
                {% if request.user.is_authenticated %}
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'add_item'%}">Add Item</a>
                    </li>
                    <li class="nav-item">
                        <a href="{% url 'logout' %}" class="nav-link active">
                            Logout
                        </a>
                    </li>
                {% else %}
                    <li class="nav-item">
                        <a href="{% url 'login' %}" class="nav-link active">
                            Login
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="{% url 'register' %}" class="nav-link active">
                            Register
                        </a>
                    </li>
                {% endif %}
            </ul>
        </div>
    </div>
</nav>          
```


##**Form.html:**
El archivo form.html en un repositorio de GitHub es un archivo que contiene código HTML para crear un formulario en una página web. GitHub es una plataforma para alojar código de programación y este archivo puede ser parte de un proyecto que muestra un formulario de contacto, registro, o cualquier otro tipo de formulario, y puede estar destinado a usarse con servicios externos para procesar los envíos, ya que GitHub no puede procesar datos de formularios por sí mismo.
En este proyecto la función de nuestro archivo llamado “form.html” es el poder tener un formulario de registro (register), esta página se encarga de mostrar un formulario HTML para el registro de usuarios con validación y manejo de errores, extendiendo la plantilla del documento base.html donde esta nuestra estructura base de la página en general. 

```
{% extends 'store/base.html' %}
{% block title %} {{ title }} {% endblock %}
{% block content%}
    <h4 class="mb-4 mt-4">{{ title }}</h4>
    <hr>
    <form action="." method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        <div>
       
            {{ form.as_p }}
        </div>

        {% if form.errors or form.non_field_errors %}
            <div class="mb-4 p-6 bg-danger">
                {% for field in form %}
                    {{ field.errors }}
                {% endfor %}

                {{ form.non_field_errors }}
            </div>
        {% endif %}

        <button class="btn btn-primary mb-6">Register</button>
    </form>
{% endblock%}
```

Settings.py
El archivo settings.py sirve para guardar toda la configuración principal de un proyecto hecho con Django. Básicamente, es el archivo donde se definen las reglas que el proyecto necesita para funcionar bien. 
Dentro de este archivo se pueden cambiar muchas cosas, por ejemplo:
La base de datos: que es donde se guarda la información del proyecto. Ahí se indica si se va a usar SQLite, MySQL u otra. 
Las aplicaciones instaladas:son las partes o módulos del proyecto que Django necesita para trabajar. 
El idioma y la zona horaria: para adaptar el proyecto al país o idioma que queramos usar. 
Los archivos estáticos: como las imágenes, los estilos (CSS) o los scripts (JavaScript). 
Temas de seguridad: como la clave secreta (SECRET_KEY) o los dominios que pueden acceder al proyecto.

– Actualización 

El archivo settings.py sirve para guardar toda la configuración principal de un proyecto hecho con Django. Básicamente es el archivo donde se definen las reglas que el proyecto necesita para funcionar bien.

La primera actualización del código fue esta: Sirve para que Django sepa donde guardar la información de la base de datos. 

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

En la actualización se agregó la parte de templates:Sirve para que podamos buscar y usar archivos HTML desde las aplicaciones o desde carpetas personalizadas.
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

En la actualización se agregó este código: Sirve para conectar a Django con servidores web 
```
WSGI_APPLICATION = 'marketplace_main.wsgi.application'
```

En la actualización se agregó este código: Sirve para controlar a donde se manda al usuario al estar registrado, o cuando inicia o cierra sesión

```
ALLOWED_HOSTS = []
LOGIN_URL = '/store/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```
---

# **Ejecución del Proyecto**

![](img/imagen10.png)
Al correr el servidor con el codigo python manage.py runserver, nos proporcionó un link que al copiar y pegarlo en el buscador de Google y agregarle al link “/admin/”, nos llevó a un apartado de inicio de sesión de Django.

![](img/imagen10.png)
Después de iniciar sesión nos llevó a otro apartado donde nos mostró toda nuestra actividad de Store: “Categories” e “Items” (Archivos codificados en Visual Studio Code).

![](img/imagen10.png)
Agregamos tres categorías: “ropa”, “videojuegos” y “zapatos” en la sección de Categories, luego en la sección de Items agregamos desde Actions estas categorías. A cada categoría le completamos la información que nos solicitaba.

![](img/imagen10.png)
![](img/imagen10.png)
![](img/imagen10.png)

![](img/imagen10.png)
Corrimos de nuevo el servidor, y copiamos el link, lo pegamos pero esta vez sin agregar el “/admin/”, al ponerlo nos llevó a un apartado donde se muestra nuestros productos que habíamos puesto en Categories e Items.

![](img/imagen10.png)
En Visual Studio Code agregamos el archivo de Contact y lo codificamos, al guardarlo y correr el servidor, CMD nos brindo un link que al pegarlo y agregar a lado del link “/store/contact/” o dando click a la sección “Contact” en la barra negra, nos llevó a un apartado donde el usuario puede poner sus datos y un mensaje.

![](img/imagen10.png)
Por último, agregamos otro archivo “detail” en Visual Studio Code, donde al correr de nuevo el servidor y agregar a lado del link “/store/detail/2/”, nos llevó al apartado de los créditos.

![](img/imagen10.png)
En la página principal lo que se agregó fue el botón de ver detalles,la posición en como estaba adjunta, junto a la paleta de colores que se usaron, para las cosas

![](img/imagen10.png)
Se agregó, donde el usuario podrá meter registro dentro de la página y se guardará.

![](img/imagen10.png)
Aquí se actualizó, donde aparte de poder meter algún tipo de registro,podría agregar una contraseña para que los datos se mantuvieran más seguros.

![](img/imagen10.png)
En la página, se hizo este espacio, donde el usuario podrá ingresar, sus datos, para poder contactar o hablar directamente, sobre los productos en venta, de igual forma, si hay algo que sugerir.

![](img/imagen10.png)
Por ultimo, al momento de presionar, ver detalles, automáticamente, te mandara, donde puedan ver con más claridad las cosas que contiene el producto.

---

# **Conclusiones**

Durante el transcurso de estas semanas donde hemos podido trabajar con el proyecto pudimos aprender multiples cosas nuevas las cuales no teniamos noción de ellas antes, un ejemplo clave es el cómo podemos crear una página de manera tan fácil y sencilla sin necesidad de programar tanto con el simple hecho de usar django, el cual es una herramienta muy útil al momento de realizar trabajos como este.

Al realizar este proyecto pudimos familiarizarnos respecto a múltiples formas de realizar distintas cosas que nos podrían servir para poder realizar el diseño de la página en la que trabajabamos, gracias a la implementación de django nuestro enfoque al programar fue más hacia el diseño de cómo quedaría una vez implementado el código, desde crear la carpeta templates donde guardabamos los distintos diseños para cada página hasta el poder aprender a llamar de una página a otra para que se pudieran redirigir entre sí.

–
En esta etapa del proyecto logramos fortalecer nuestro conocimiento de Django al implementar actualizaciones importantes en la aplicación. Mejoramos rutas, vistas, formularios y plantillas, lo que nos permitió entender mejor cómo se conectan los distintos componentes de un proyecto web para que funcione de manera completa y organizada. Estas mejoras hicieron que nuestra aplicación se acercara más a un marketplace funcional.
Las actualizaciones realizadas, como el registro de usuarios, inicio y cierre de sesión, así como la publicación de productos, nos ayudaron a comprender la importancia de la experiencia del usuario y cómo cada funcionalidad impacta en la interacción dentro de la plataforma. Además, trabajar con formularios personalizados y modelos relacionados nos permitió ver de forma práctica cómo Django gestiona los datos y la lógica interna de la aplicación.
Finalmente, el trabajo en equipo fue esencial para avanzar con estas mejoras. Mantener documentos compartidos con comandos, código y explicaciones nos permitió resolver problemas más rápido y mantener un ritmo de trabajo organizado. Esta experiencia nos dejó más confianza para seguir desarrollando aplicaciones más complejas con Django y aprovechar mejor su estructura para futuros proyectos.



