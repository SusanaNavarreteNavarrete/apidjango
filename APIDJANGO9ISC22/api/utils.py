from django.core.mail import send_mail

def enviar_correo_registro(email):
    asunto = 'Registro exitoso'
    mensaje = 'Gracias por tu registro'
    remitente = 'tu_email@gmail.com'
    destinatario = [email]
    
    send_mail(asunto, mensaje, remitente, destinatario)