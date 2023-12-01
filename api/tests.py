from django.test import TestCase

# Create your tests here.

import pytest
from .models import Usuario, DatosCSV

@pytest.mark.django_db
def test_crear_datos_csv():
    # Crear datos CSV
    datos_csv = DatosCSV.objects.create(
        Marca_temporal='2023-11-24 12:00:00',
        correo='correo@example.com',
        pregunta1='Respuesta1',
        pregunta2='Respuesta2',
        pregunta3='Respuesta3',
        pregunta4='Respuesta4',
        pregunta5='Respuesta5',
        pregunta6='Respuesta6',
        pregunta7='Respuesta7',
        pregunta8='Respuesta8',
        pregunta9='Respuesta9',
        pregunta10='Respuesta10',
        # Agregar más campos según sea necesario
    )

    # Asegurarse de que los datos CSV se hayan creado correctamente
    assert DatosCSV.objects.count() == 1
    assert datos_csv.Marca_temporal == '2023-11-24 12:00:00'
    assert datos_csv.correo == 'correo@example.com'
    assert datos_csv.pregunta1 == 'Respuesta1'
    assert datos_csv.pregunta2 == 'Respuesta2'
    assert datos_csv.pregunta3 == 'Respuesta3'
    assert datos_csv.pregunta4 == 'Respuesta4'
    assert datos_csv.pregunta5 == 'Respuesta5'
    assert datos_csv.pregunta6 == 'Respuesta6'
    assert datos_csv.pregunta7 == 'Respuesta7'
    assert datos_csv.pregunta8 == 'Respuesta8'
    assert datos_csv.pregunta9 == 'Respuesta9'
    assert datos_csv.pregunta10 == 'Respuesta10'
    # Agregar más aserciones según sea necesario
    
@pytest.mark.django_db
def test_crear_usuario():
    # Crear un usuario
    usuario = Usuario.objects.create(
        nombre='John',
        email='john.doe@example.com',
        password='password123',
        confirm_password='password123'
    )

    # Asegurarse de que el usuario se haya creado correctamente
    assert Usuario.objects.count() == 1
    assert usuario.nombre == 'John'
    assert usuario.email == 'john.doe@example.com'
    assert usuario.password == 'password123'
    assert usuario.confirm_password == 'password123'