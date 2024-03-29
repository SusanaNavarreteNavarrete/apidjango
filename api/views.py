from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.views import APIView
from .models import Usuario
from .forms import RegistroForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth import authenticate, login


class Home (APIView):
    template_name = 'index.html',
    def get(self, request):
        return render(request,self.template_name)
class Login (APIView):
    template_login = 'login.html',
    def get(self, request):
        return render(request,self.template_login)
class Form (APIView):
    template_form = 'form.html',
    def get(self, request):
        return render(request,self.template_form)
class Inicio (APIView):
    template_inicio = 'inicio.html',
    def get(self, request):
        return render(request,self.template_inicio)

class ProcesarRegistroView(APIView):
    template_name = 'registro.html'

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Componer el mensaje de correo electrónico
            subject = 'Confirmación de Registro'
            message = '¡Gracias por registrarte en nuestro sitio web! Tus detalles de registro son:'
            message += f'\nNombre: {user.nombre}'
            message += f'\nCorreo electrónico: {user.email}'
            # Puedes agregar otros detalles de registro aquí

            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.email]  # Usar el correo proporcionado por el usuario

            # Enviar el correo electrónico
            send_mail(
                subject, message, from_email, recipient_list,
                fail_silently=False,
            )

            return redirect('login')

        return render(request, self.template_name, {'form': form})

class LoginView(APIView):
    template_name = 'login.html'  # Reemplaza 'login.html' con el nombre de tu plantilla de inicio de sesión

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('user')
        password = request.POST.get('password')

        # Consulta la base de datos para encontrar un usuario con los datos ingresados
        try:
            user = Usuario.objects.get(email=email, password=password)
        except Usuario.DoesNotExist:
            user = None

        if user is not None:
            # Las credenciales son válidas
            # Realiza las acciones necesarias aquí
            return redirect('inicio')  # Cambia 'catalogo' al nombre de tu página de destino
        else:
            # Las credenciales son incorrectas
            # Realiza las acciones necesarias aquí
            return render(request, self.template_name, {'error_message': 'Credenciales incorrectas'})

from rest_framework.response import Response
from django.shortcuts import render
from .models import DatosCSV

class Graficas(APIView):
    def get(self, request):
        datos = DatosCSV.objects.all()

        # Procesa los datos para contar las respuestas a "pregunta1"
        respuestas_pregunta1 = {}
        for dato in datos:
            respuesta = dato.pregunta1
            if respuesta in respuestas_pregunta1:
                respuestas_pregunta1[respuesta] += 1
            else:
                respuestas_pregunta1[respuesta] = 1

        # Procesa los datos para contar las respuestas a "pregunta2"
        respuestas_pregunta2 = {}
        for dato in datos:
            respuesta = dato.pregunta2
            if respuesta in respuestas_pregunta2:
                respuestas_pregunta2[respuesta] += 1
            else:
                respuestas_pregunta2[respuesta] = 1
        # Procesa los datos para contar las respuestas a "pregunta3"
        respuestas_pregunta3 = {}
        for dato in datos:
            respuesta = dato.pregunta3
            if respuesta in respuestas_pregunta3:
                respuestas_pregunta3[respuesta] += 1
            else:
                respuestas_pregunta3[respuesta] = 1
        # Procesa los datos para contar las respuestas a "pregunta4"
        respuestas_pregunta4 = {}
        for dato in datos:
            respuesta = dato.pregunta4
            if respuesta in respuestas_pregunta4:
                respuestas_pregunta4[respuesta] += 1
            else:
                respuestas_pregunta4[respuesta] = 1
        # Procesa los datos para contar las respuestas a "pregunta5"
        respuestas_pregunta5 = {}
        for dato in datos:
            respuesta = dato.pregunta5
            if respuesta in respuestas_pregunta5:
                respuestas_pregunta5[respuesta] += 1
            else:
                respuestas_pregunta5[respuesta] = 1
        # Procesa los datos para contar las respuestas a "pregunta6"
        respuestas_pregunta6 = {}
        for dato in datos:
            respuesta = dato.pregunta6
            if respuesta in respuestas_pregunta6:
                respuestas_pregunta6[respuesta] += 1
            else:
                respuestas_pregunta6[respuesta] = 1
        # Procesa los datos para contar las respuestas a "pregunta7"
        respuestas_pregunta7 = {}
        for dato in datos:
            respuesta = dato.pregunta7
            if respuesta in respuestas_pregunta7:
                respuestas_pregunta7[respuesta] += 1
            else:
                respuestas_pregunta7[respuesta] = 1
        # Procesa los datos para contar las respuestas a "pregunta8"
        respuestas_pregunta8 = {}
        for dato in datos:
            respuesta = dato.pregunta8
            if respuesta in respuestas_pregunta8:
                respuestas_pregunta8[respuesta] += 1
            else:
                respuestas_pregunta8[respuesta] = 1
        # Procesa los datos para contar las respuestas a "pregunta9"
        respuestas_pregunta9 = {}
        for dato in datos:
            respuesta = dato.pregunta9
            if respuesta in respuestas_pregunta9:
                respuestas_pregunta9[respuesta] += 1
            else:
                respuestas_pregunta9[respuesta] = 1
        # Procesa los datos para contar las respuestas a "pregunta10"
        respuestas_pregunta10 = {}
        for dato in datos:
            respuesta = dato.pregunta10
            if respuesta in respuestas_pregunta10:
                respuestas_pregunta10[respuesta] += 1
            else:
                respuestas_pregunta10[respuesta] = 1

        # Prepara los datos en un formato adecuado para los gráficos
        labels_pregunta1 = list(respuestas_pregunta1.keys())
        data_pregunta1 = list(respuestas_pregunta1.values())

        labels_pregunta2 = list(respuestas_pregunta2.keys())
        data_pregunta2 = list(respuestas_pregunta2.values())

        labels_pregunta3 = list(respuestas_pregunta3.keys())
        data_pregunta3 = list(respuestas_pregunta3.values())

        labels_pregunta4 = list(respuestas_pregunta4.keys())
        data_pregunta4 = list(respuestas_pregunta4.values())

        labels_pregunta5 = list(respuestas_pregunta5.keys())
        data_pregunta5 = list(respuestas_pregunta5.values())

        labels_pregunta6 = list(respuestas_pregunta6.keys())
        data_pregunta6 = list(respuestas_pregunta6.values())

        labels_pregunta7 = list(respuestas_pregunta7.keys())
        data_pregunta7 = list(respuestas_pregunta7.values())

        labels_pregunta8 = list(respuestas_pregunta8.keys())
        data_pregunta8 = list(respuestas_pregunta8.values())

        labels_pregunta9 = list(respuestas_pregunta9.keys())
        data_pregunta9 = list(respuestas_pregunta9.values())

        labels_pregunta10 = list(respuestas_pregunta10.keys())
        data_pregunta10 = list(respuestas_pregunta10.values())

        # Puedes repetir el proceso para las otras preguntas

        return render(request, 'graficas.html', {
            'labels_pregunta1': labels_pregunta1,
            'data_pregunta1': data_pregunta1,

            'labels_pregunta2': labels_pregunta2,
            'data_pregunta2': data_pregunta2,

            'labels_pregunta3': labels_pregunta3,
            'data_pregunta3': data_pregunta3,

            'labels_pregunta4': labels_pregunta4,
            'data_pregunta4': data_pregunta4,

            'labels_pregunta5': labels_pregunta5,
            'data_pregunta5': data_pregunta5,

            'labels_pregunta6': labels_pregunta6,
            'data_pregunta6': data_pregunta6,

            'labels_pregunta7': labels_pregunta7,
            'data_pregunta7': data_pregunta7,

            'labels_pregunta8': labels_pregunta8,
            'data_pregunta8': data_pregunta8,

            'labels_pregunta9': labels_pregunta9,
            'data_pregunta9': data_pregunta9,

            'labels_pregunta10': labels_pregunta10,
            'data_pregunta10': data_pregunta10,
            # Agrega aquí las variables para las otras preguntas
        })

from django.shortcuts import render
from django.views import View
import wikipedia

class ComponentDetailView(View):
    template_name = 'component_detail.html'

    def get(self, request, *args, **kwargs):
        component_name = kwargs.get('component_name')

        try:
            page_summary = wikipedia.summary(component_name, sentences=1)
            description_wikipedia = page_summary
        except wikipedia.exceptions.DisambiguationError as e:
            # En caso de ambigüedad en la búsqueda, manejarlo de acuerdo a tus necesidades
            description_wikipedia = f"Error de ambigüedad: {e}"
        except wikipedia.exceptions.PageError:
            description_wikipedia = "No se encontró información en Wikipedia."

        context = {
            'nombre_componente': component_name,
            'descripcion_wikipedia': description_wikipedia,
            # Otros datos necesarios para tu plantilla
        }

        return render(request, self.template_name, context)
    
    
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from reportlab.pdfgen import canvas
from django.http import FileResponse
import os

def download_pdf(request, component_name):
    # Obtener la información del componente según tu lógica
    try:
        page_summary = wikipedia.summary(component_name, sentences=1)
        description_wikipedia = page_summary
    except wikipedia.exceptions.DisambiguationError as e:
        # Manejar ambigüedad en la búsqueda según tus necesidades
        description_wikipedia = f"Error de ambigüedad: {e}"
    except wikipedia.exceptions.PageError:
        description_wikipedia = "No se encontró información en Wikipedia."

    component_info = {
        'nombre_componente': component_name,
        'descripcion_wikipedia': description_wikipedia,
        'precio': '$XX.XX',
        # Otros datos necesarios
    }

    # Renderizar el contenido del PDF sin la imagen
    pdf_content = render_to_string('pdf_template.html', component_info)

    # Crear el objeto de respuesta para el archivo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{component_name}.pdf"'

    # Crear el archivo PDF y escribir el contenido
    p = canvas.Canvas(response)
    p.drawString(100, 800, f"Nombre del Componente: {component_info['nombre_componente']}")
    p.drawString(100, 780, f"Descripción: {component_info['descripcion_wikipedia']}")
    p.drawString(100, 760, f"Precio: {component_info['precio']}")
    # Agregar más información si es necesario
    image_path = os.path.join(settings.BASE_DIR, 'static', 'img', f'{component_name}.jpg')

    # Verificar si la imagen existe antes de intentar agregarla
    if os.path.exists(image_path):
        # Agregar la imagen al PDF
        p.drawImage(image_path, 100, y_position - line_height, width=200, height=150)

    
    p.showPage()
    p.save()

    return response