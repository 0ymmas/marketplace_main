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

<img width="540" height="462" alt="image" src="https://github.com/user-attachments/assets/b0becd2c-7565-4a8d-aec3-d01bcedaf8e3" />



---

# **Archivos y Funciones**

## **Forms.py**

En el archivo forms.py del apartado store lo que hago es definir los formularios que se usan para que los usuarios puedan iniciar sesión y registrarse, en  vez de crear todo desde cero, aprovechó los formularios que Django ya trae para autenticación y registro, y simplemente los personalizo para que se vean mejor en mi proyecto, él lo que es el formulario (Login Form),  cambio los campos de usuario y contraseña para agregarles placeholders y clases de Bootstrap, así los inputs se ven más ordenados y con diseño moderno, no modificó la lógica del inicio de sesión, solo la apariencia.

Por otra parte el formulario de registro (Signup Form), hago algo parecido, usó el formulario estándar de Django para crear usuarios, pero ajustó los campos para que tengan el estilo que quiero y también agrego placeholders que sirve como una pequeña guía o pista para indicar qué debe escribirse ahí, además, especificó que este formulario trabaja con el modelo “User” y los campos que quiero mostrar. En otras palabras, este archivo se encarga de darle estilo y mejorar la presentación de los formularios de login y registro, manteniendo la funcionalidad original que Django ya provee, es básicamente la capa que hace que los formularios se vean bien y sean más cómodos de usar.

``` python
from django import forms
from django.contrib.auth.forms import \
    UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Item

class LoginForm(AuthenticationForm):
    username = \
        forms.CharField(widget=forms.TextInput(
            attrs={
                'placeholder': 'Tu usuario',
                'class': 'form-control'
            }
        ))

    password = \
        forms.CharField(widget=forms.PasswordInput())
```
<img width="346" height="774" alt="image" src="https://github.com/user-attachments/assets/a1ae3e1f-bd02-4ea9-bd3b-2ffd1aa75d89" />
<br>
<img width="344" height="562" alt="image" src="https://github.com/user-attachments/assets/d4009b13-b051-49de-b1fa-1f3487e0a5a6" />

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

<img width="475" height="332" alt="image" src="https://github.com/user-attachments/assets/0517fcba-4028-47e7-ba62-ec5d02f1ccc9" />
<br>
<img width="489" height="373" alt="image" src="https://github.com/user-attachments/assets/4200df05-8fbe-4075-8331-00b05fda71fa" />
<br>
<img width="455" height="385" alt="image" src="https://github.com/user-attachments/assets/9fc3f797-e81d-4ac7-8409-d56db28f349a" />
<br>
<img width="539" height="171" alt="image" src="https://github.com/user-attachments/assets/dcac8342-ba27-4725-aecd-bcd81ada80e9" />
<br>
<img width="537" height="321" alt="image" src="https://github.com/user-attachments/assets/b1352fac-dfd9-44fb-8a03-fe5cca87a99b" />

– Actualización 

El archivo settings.py sirve para guardar toda la configuración principal de un proyecto hecho con Django. Básicamente es el archivo donde se definen las reglas que el proyecto necesita para funcionar bien.

La primera actualización del código fue esta: Sirve para que Django sepa donde guardar la información de la base de datos. 
<img width="539" height="63" alt="image" src="https://github.com/user-attachments/assets/321cba15-640e-4cf8-8f11-6073b76250d2" />
<br>
<img width="541" height="63" alt="image" src="https://github.com/user-attachments/assets/44369098-9704-4f52-88ff-d39a5dcfa096" />

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
En la actualización se agregó la parte de templates:Sirve para que podamos buscar y usar archivos HTML desde las aplicaciones o desde carpetas personalizadas.
<img width="538" height="289" alt="image" src="https://github.com/user-attachments/assets/a7c55a9c-c1aa-408c-be76-3c51e9d50fc8" />

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
<img width="542" height="21" alt="image" src="https://github.com/user-attachments/assets/b1b2db1d-267d-4874-ab45-7ac60c7d2bb4" />

```
WSGI_APPLICATION = 'marketplace_main.wsgi.application'
```

En la actualización se agregó este código: Sirve para controlar a donde se manda al usuario al estar registrado, o cuando inicia o cierra sesión
<img width="540" height="73" alt="image" src="https://github.com/user-attachments/assets/965a7fea-7846-455f-a04b-b9e75a35846c" />

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

<img width="541" height="183" alt="image" src="https://github.com/user-attachments/assets/37b70de6-4953-4d9a-b377-be00893cc0f3" />
<br>
<img width="514" height="163" alt="image" src="https://github.com/user-attachments/assets/c5aae77d-c2e5-438e-8524-d819238633b3" />


— Actualización

Con las recientes modificaciones en urls.py, se añadieron varias rutas nuevas que mejoran la funcionalidad de la plataforma:
- La ruta register/ permite a los usuarios crear una cuenta nueva.
- La ruta login/ utiliza la vista de autenticación de Django con un formulario personalizado (LoginForm) para que los usuarios puedan iniciar sesión.
- La ruta logout/ cierra la sesión del usuario, asegurando que la información personal quede protegida.
- La ruta add_item/ permite a los usuarios registrados publicar nuevos productos en el marketplace.
- La ruta detail/<int:pk>/ sigue mostrando los detalles de un producto específico.
- La ruta contact/ muestra la página de contacto para consultas o sugerencias.

Gracias a estas actualizaciones, el archivo urls.py permite que la aplicación funcione de manera más completa, organizada y segura. Contar con rutas claras para la gestión de usuarios y productos facilita la navegación, mejora la experiencia del usuario y asegura que cada acción se procese correctamente según el tipo de solicitud. En conjunto, estas mejoras son clave para que el marketplace funcione como un sitio dinámico y confiable.
<img width="664" height="20" alt="image" src="https://github.com/user-attachments/assets/45470cf2-c675-4c7a-b9e7-a80c4dace17f" />
<br>
<img width="600" height="264" alt="image" src="https://github.com/user-attachments/assets/9c98b8b9-fbf2-48bc-b9b0-4feddeebddb6" />

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

<img width="598" height="200" alt="image" src="https://github.com/user-attachments/assets/bf6e7c81-e3f1-402f-b350-9a52a007dcf4" />
<br>
<img width="599" height="182" alt="image" src="https://github.com/user-attachments/assets/5c8e823a-05b6-412b-b267-dde4d063945f" />

—Actualización

En nuestro proyecto tenemos dos modelos principales: Category e Item. El modelo Category guarda el nombre de cada categoría y Django organiza automáticamente estas categorías alfabéticamente gracias a la configuración interna del modelo. Por su parte, el modelo Item representa los artículos o productos, incluyendo datos como el nombre, una descripción opcional, el precio, la posibilidad de subir una imagen, si ya fue vendido y la fecha de creación, que Django registra automáticamente, además, Item utiliza llaves foráneas para relacionarse con otros modelos: la primera, category, conecta cada artículo con su categoría; la segunda, created_by, relaciona cada artículo con el usuario que lo creó.
Lo mejor de trabajar con Django es que solo necesitamos definir estas clases y sus campos, y luego el framework se encarga de crear las tablas reales en la base de datos usando los comandos makemigrations y migrate, lo que simplifica enormemente la gestión de la información sin necesidad de escribir SQL manualmente.
<img width="598" height="274" alt="image" src="https://github.com/user-attachments/assets/86e21cbb-e4bf-4e83-9770-1a135aa3ebd8" />
<br>
<img width="598" height="636" alt="image" src="https://github.com/user-attachments/assets/b9fb5182-48ae-4b2e-bfba-8407b4a1d82a" />

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

<img width="560" height="199" alt="image" src="https://github.com/user-attachments/assets/47b841f3-4c28-490f-a691-512b3352901c" />
<br>
<img width="571" height="223" alt="image" src="https://github.com/user-attachments/assets/aa8e832f-8356-4172-8df1-7417e9a7c497" />

— Actualización  

En nuestro caso nos funcionó para cosas necesarias como las siguientes:

<img width="478" height="181" alt="image" src="https://github.com/user-attachments/assets/6c728c73-ef62-464f-9e1f-69d7e6d947f5" />


Ese código es la vista home() de Django y sirve para cargar la página principal de la tienda: obtiene de la base de datos todos los productos que no están vendidos y todas las categorías, mete esa información en un contexto y luego la envía al template home.html para mostrarla al usuario.

<img width="456" height="105" alt="image" src="https://github.com/user-attachments/assets/58a6b4eb-77e6-459f-bc2f-ba81fb62a6f2" />


Ese código define la vista contact(), y su función es simplemente mostrar la página de contacto.
Crea un contexto con un mensaje ('Quieres otros productos contactame!') y lo envía al template contact.html, para que ese texto se muestre allí cuando el usuario abra la página.

<img width="669" height="140" alt="image" src="https://github.com/user-attachments/assets/7f490e73-ccc7-4085-8408-fc5f6394f6d3" />


Esa vista detail() sirve para mostrar la página de detalle de un producto.
Primero busca el producto con el pk dado (o muestra 404 si no existe). Luego obtiene hasta 3 productos relacionados que sean de la misma categoría y que no estén vendidos, excluyendo el actual. Finalmente envía al template item.html tanto el producto como sus relacionados para mostrarlos en la página.

<img width="462" height="267" alt="image" src="https://github.com/user-attachments/assets/83cf8e40-3ab4-45f6-b1d7-e286b27dae3c" />


Esa vista register() maneja el registro de nuevos usuarios.
Si el usuario envía el formulario (método POST), crea un SignupForm con los datos, lo valida y, si es correcto, guarda al nuevo usuario y redirige a la página de login.
Si es una visita normal (GET), simplemente muestra un formulario vacío.
Al final, siempre envía el formulario al template signup.html para mostrarlo en la página.

<img width="279" height="70" alt="image" src="https://github.com/user-attachments/assets/2eaa01e8-12a8-4783-a842-836a4129f936" />


Esa vista logout_user() cierra la sesión del usuario.
Llama a logout(request) para desconectarlo y luego lo redirige a la página principal (home).

<img width="519" height="382" alt="image" src="https://github.com/user-attachments/assets/0054ffa7-ffd4-434f-8504-77abfe4771fb" />


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
<img width="425" height="47" alt="image" src="https://github.com/user-attachments/assets/febba2c9-9e43-4524-9865-2e339eb5c9b5" />

```
@login_required
def add_item(request):
```
-**Procesamiento del Formulario (Método POST)**
Si la solicitud es POST, se crea una instancia del formulario NewItemForm usando los datos enviados en la solicitud (request.POST y request.FILES):
<img width="423" height="24" alt="image" src="https://github.com/user-attachments/assets/b3e8142d-3dcb-4d60-8c32-2e4b3a580f0e" />
<br>
<img width="423" height="46" alt="image" src="https://github.com/user-attachments/assets/4705a25d-4dbb-49be-be5d-e37f306c59b6" />

```
if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
```
Después, se valida el formulario con form.is_valid(). Si el formulario es válido, significa que los datos proporcionados cumplen con los requisitos del formulario.
<img width="222" height="25" alt="image" src="https://github.com/user-attachments/assets/64dcb18c-213c-4990-9032-aaf1f85f0be6" />
<br>
<img width="480" height="82" alt="image" src="https://github.com/user-attachments/assets/36b4d4ce-8a30-4843-a461-2a895fc5ba6b" />

   ```
 if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
```

El artículo se guarda en la base de datos, y se asocia al usuario que está autenticado (es decir, el que ha iniciado sesión). Esto se hace con:
<img width="471" height="26" alt="image" src="https://github.com/user-attachments/assets/91ad01cd-7648-4a7a-a34a-d79d4f4225e0" />

```
item.created_by = request.user
```
Una vez guardado el artículo, el usuario es redirigido a la página de detalles del artículo recién creado:
<img width="483" height="24" alt="image" src="https://github.com/user-attachments/assets/9c5d1c17-f5cc-4a73-bd38-794c52659bfc" />

```
    return redirect('detail', pk=item.id)
```
-**Mostrar el Formulario (Método GET)**
Si la solicitud no es POST, significa que el usuario está viendo el formulario para agregar un nuevo artículo. En este caso, se crea un formulario vacío y se prepara el contexto para mostrarlo en la plantilla:
<img width="483" height="163" alt="image" src="https://github.com/user-attachments/assets/1f305300-8e9e-4009-b6e0-1d7264ca3d15" />

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
<img width="480" height="55" alt="image" src="https://github.com/user-attachments/assets/94ec01fa-71c1-4266-bf85-b54fd80cd850" />

---

## **Templates/store**
La carpeta templates/store guarda los archivos que definen el diseño de la tienda en línea, es como el "molde" que determina cómo se ven las páginas, como la de inicio o el carrito de compras.
Su función principal es dar un diseño uniforme y profesional, las plantillas permiten personalizar fácilmente la apariencia sin afectar la funcionalidad, además, es útil para cambiar el aspecto de toda la tienda sin complicaciones, especialmente en plataformas como shopify o woocommerce y lo mejor es que reutiliza elementos, como botones o encabezados, para que sea más fácil mantener el sitio actualizado.

<img width="327" height="200" alt="image" src="https://github.com/user-attachments/assets/b17a0bb9-d1d7-4170-ba74-22a8c9c37be0" />


Es la página donde se muestra un producto individual de tu tienda. Cuando alguien da click en un artículo, Django carga este template y aquí se ve todo: la imagen, el precio, la descripción e inclusive otros productos parecidos 
Usa tu plantilla base (base.html) para mantener el estilo. Muestra la imagen del producto (o una imagen por defecto si no tiene). Enseña el nombre, precio y descripción. Abajo pone una sección de “productos relacionados” que vienen de la misma categoría. Tiene un botón arriba para regresar a la lista de productos.
Básicamente, es la página de detalle del producto, justo como en cualquier tienda online.

**Código:**
<img width="483" height="120" alt="image" src="https://github.com/user-attachments/assets/b16c715a-488f-4c01-965b-9b08a9602231" />
<br>
<img width="290" height="629" alt="image" src="https://github.com/user-attachments/assets/aa3cd3fe-bf2c-4906-9e41-3a8fc0e5496f" />


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
<img width="310" height="207" alt="image" src="https://github.com/user-attachments/assets/acc22a22-ce65-4a9d-905c-6f007dba0d1e" />
<br>
<img width="307" height="448" alt="image" src="https://github.com/user-attachments/assets/1f837b62-d8ed-4acc-abbe-ba8a97587762" />

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
<img width="309" height="263" alt="image" src="https://github.com/user-attachments/assets/13f9a2ed-4bdc-4e9e-904c-b2aa28b2dbcb" />
<br>
<img width="307" height="283" alt="image" src="https://github.com/user-attachments/assets/d567e604-a51a-4500-b4ad-f4d312d68e01" />

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
<img width="311" height="365" alt="image" src="https://github.com/user-attachments/assets/3c90cff3-6f88-4377-8f06-1e6b2a823467" />
<br>
<img width="308" height="448" alt="image" src="https://github.com/user-attachments/assets/7d427742-789b-4947-822a-8b610003895a" />

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
<img width="464" height="310" alt="image" src="https://github.com/user-attachments/assets/1bf89ae6-ac26-4aec-81a0-e2e39ea9eaaf" />
<br>
<img width="470" height="608" alt="image" src="https://github.com/user-attachments/assets/67d115b5-5604-45eb-adfa-2b1c78642a40" />

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

<img width="465" height="365" alt="image" src="https://github.com/user-attachments/assets/c11f274e-3b48-4380-8580-e19b3b6d46ef" />
<br>
<img width="640" height="42" alt="image" src="https://github.com/user-attachments/assets/2797d720-dfc2-47c6-a1a9-5ace5ea20e4c" />


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
---
##**Settings.py**
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

<img width="662" height="151" alt="image" src="https://github.com/user-attachments/assets/71cd1649-4ea3-465e-870f-61ae31da8ee0" />


```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

En la actualización se agregó la parte de templates:Sirve para que podamos buscar y usar archivos HTML desde las aplicaciones o desde carpetas personalizadas.

<img width="662" height="356" alt="image" src="https://github.com/user-attachments/assets/809766b6-0c1b-4b46-a105-89a2c74c8817" />

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
<img width="662" height="25" alt="image" src="https://github.com/user-attachments/assets/3db3b9d7-6868-4fa2-9aa7-e3c123b4c8ee" />

```
WSGI_APPLICATION = 'marketplace_main.wsgi.application'
```

En la actualización se agregó este código: Sirve para controlar a donde se manda al usuario al estar registrado, o cuando inicia o cierra sesión
<img width="660" height="94" alt="image" src="https://github.com/user-attachments/assets/5dc514bb-a57c-4eff-8339-4746271b5ba3" />

```
ALLOWED_HOSTS = []
LOGIN_URL = '/store/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```
---

# **Ejecución del Proyecto**

<img width="755" height="411" alt="image" src="https://github.com/user-attachments/assets/8475684b-3e84-4f1c-bc46-382caa0622f1" />

Al correr el servidor con el codigo python manage.py runserver, nos proporcionó un link que al copiar y pegarlo en el buscador de Google y agregarle al link “/admin/”, nos llevó a un apartado de inicio de sesión de Django.

<img width="748" height="283" alt="image" src="https://github.com/user-attachments/assets/755329cf-7a9a-43f7-a4b2-ae4ad1408964" />

Después de iniciar sesión nos llevó a otro apartado donde nos mostró toda nuestra actividad de Store: “Categories” e “Items” (Archivos codificados en Visual Studio Code).

<img width="753" height="388" alt="image" src="https://github.com/user-attachments/assets/7b0c60e7-af5f-4c19-bc5d-d0005aa57c77" />

Agregamos tres categorías: “ropa”, “videojuegos” y “zapatos” en la sección de Categories, luego en la sección de Items agregamos desde Actions estas categorías. A cada categoría le completamos la información que nos solicitaba.

<img width="753" height="368" alt="image" src="https://github.com/user-attachments/assets/94784fb5-941f-4d32-9d2f-0109f7e70aa7" />
<br>
<img width="753" height="385" alt="image" src="https://github.com/user-attachments/assets/4455ebac-27e9-4e01-9e14-b2d88d046d89" />
<br>
<img width="754" height="364" alt="image" src="https://github.com/user-attachments/assets/425af0e1-0849-4e37-be0c-562e35e40174" />


<img width="748" height="341" alt="image" src="https://github.com/user-attachments/assets/5fc66a56-6f89-439a-aa43-652335a0b765" />

Corrimos de nuevo el servidor, y copiamos el link, lo pegamos pero esta vez sin agregar el “/admin/”, al ponerlo nos llevó a un apartado donde se muestra nuestros productos que habíamos puesto en Categories e Items.

<img width="755" height="363" alt="image" src="https://github.com/user-attachments/assets/7884b22f-b41c-4b95-882d-2fd557f80c8a" />

En Visual Studio Code agregamos el archivo de Contact y lo codificamos, al guardarlo y correr el servidor, CMD nos brindo un link que al pegarlo y agregar a lado del link “/store/contact/” o dando click a la sección “Contact” en la barra negra, nos llevó a un apartado donde el usuario puede poner sus datos y un mensaje.

<img width="750" height="327" alt="image" src="https://github.com/user-attachments/assets/64c00b3d-99f9-47b4-a31a-44170a5dbd88" />

Por último, agregamos otro archivo “detail” en Visual Studio Code, donde al correr de nuevo el servidor y agregar a lado del link “/store/detail/2/”, nos llevó al apartado de los créditos.

<img width="751" height="392" alt="image" src="https://github.com/user-attachments/assets/9a509505-44b3-4239-9fc4-19b3a1c1a641" />

En la página principal lo que se agregó fue el botón de ver detalles,la posición en como estaba adjunta, junto a la paleta de colores que se usaron, para las cosas

<img width="753" height="369" alt="image" src="https://github.com/user-attachments/assets/2b0946b2-d62f-40e1-944f-1fdb2b44aee8" />

Se agregó, donde el usuario podrá meter registro dentro de la página y se guardará.

<img width="723" height="329" alt="image" src="https://github.com/user-attachments/assets/395cc667-bce6-40b8-a73a-6e3c2edeb80e" />

Aquí se actualizó, donde aparte de poder meter algún tipo de registro,podría agregar una contraseña para que los datos se mantuvieran más seguros.

<img width="684" height="337" alt="image" src="https://github.com/user-attachments/assets/8f4d8367-7d5f-4fb6-9884-0b6cf248223c" />

En la página, se hizo este espacio, donde el usuario podrá ingresar, sus datos, para poder contactar o hablar directamente, sobre los productos en venta, de igual forma, si hay algo que sugerir.

<img width="750" height="218" alt="image" src="https://github.com/user-attachments/assets/82837c5c-e673-4559-8ded-8bfb9418518c" />

Por ultimo, al momento de presionar, ver detalles, automáticamente, te mandara, donde puedan ver con más claridad las cosas que contiene el producto.

---

# **Conclusiones**

Durante el transcurso de estas semanas donde hemos podido trabajar con el proyecto pudimos aprender multiples cosas nuevas las cuales no teniamos noción de ellas antes, un ejemplo clave es el cómo podemos crear una página de manera tan fácil y sencilla sin necesidad de programar tanto con el simple hecho de usar django, el cual es una herramienta muy útil al momento de realizar trabajos como este.

Al realizar este proyecto pudimos familiarizarnos respecto a múltiples formas de realizar distintas cosas que nos podrían servir para poder realizar el diseño de la página en la que trabajabamos, gracias a la implementación de django nuestro enfoque al programar fue más hacia el diseño de cómo quedaría una vez implementado el código, desde crear la carpeta templates donde guardabamos los distintos diseños para cada página hasta el poder aprender a llamar de una página a otra para que se pudieran redirigir entre sí.

–
En esta etapa del proyecto logramos fortalecer nuestro conocimiento de Django al implementar actualizaciones importantes en la aplicación. Mejoramos rutas, vistas, formularios y plantillas, lo que nos permitió entender mejor cómo se conectan los distintos componentes de un proyecto web para que funcione de manera completa y organizada. Estas mejoras hicieron que nuestra aplicación se acercara más a un marketplace funcional.
Las actualizaciones realizadas, como el registro de usuarios, inicio y cierre de sesión, así como la publicación de productos, nos ayudaron a comprender la importancia de la experiencia del usuario y cómo cada funcionalidad impacta en la interacción dentro de la plataforma. Además, trabajar con formularios personalizados y modelos relacionados nos permitió ver de forma práctica cómo Django gestiona los datos y la lógica interna de la aplicación.
Finalmente, el trabajo en equipo fue esencial para avanzar con estas mejoras. Mantener documentos compartidos con comandos, código y explicaciones nos permitió resolver problemas más rápido y mantener un ritmo de trabajo organizado. Esta experiencia nos dejó más confianza para seguir desarrollando aplicaciones más complejas con Django y aprovechar mejor su estructura para futuros proyectos.



