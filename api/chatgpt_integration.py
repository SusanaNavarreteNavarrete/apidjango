# En chatgpt_integration.py
import openai

def obtener_respuesta_chatgpt(pregunta):
    openai.api_key = 'APIDJANGO9ISC22/settings.py'
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=pregunta,
        max_tokens=150
    )
    return response['choices'][0]['text']
