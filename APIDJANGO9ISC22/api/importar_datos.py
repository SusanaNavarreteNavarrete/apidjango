import pandas as pd
from .models import DatosCSV 

def importar_datos_desde_csv(ruta_csv):
    df = pd.read_csv(ruta_csv)

    for index, row in df.iterrows():
        datos = DatosCSV(
            Marca_temporal=row['Marca temporal'],
            correo=row['Dirección de correo electrónico'],
            pregunta1=row['¿Qué tipo de información adicional te gustaría ver para cada componente?'],
            pregunta2=row['¿Qué es lo mas importante para usted en un catalogo de componentes electrónicos?'],
            pregunta3=row['¿Qué método de navegación refieres para encontrar componentes específicos?'],
            pregunta4=row['¿Cómo le gustaría que se organizara el catalogo?'],
            pregunta5=row['¿Qué funcionalidad adicional seria valiosa para facilitar la toma de decisiones de compra? '],
            pregunta6=row['¿Qué tan probable es que compre componentes electrónicos de un catalogo digital?'],
            pregunta7=row['¿Qué estilo de diseño preferiría para el catalogo?'],
            pregunta8=row['¿Qué es lo mas importante para ti al comprar componentes electrónicos?'],
            pregunta9=row['¿Qué tipos de recursos adicionales consideras útiles para complementar la información de los componentes?'],
            pregunta10=row['¿Nos permitirías mandar nuevas encuestas a tu correo  en el futuro?'],
            
            
        )
        datos.save()