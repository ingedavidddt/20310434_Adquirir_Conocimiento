# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 22:57:54 2023

@author: david
"""


# Base de datos de respuestas predefinidas
respuestas_predefinidas = {
    "Hola": "¡Hola! Estoy aquí para ayudarte. ¿Cómo estás?",
    "¿Cómo estás?": "Estoy funcionando perfectamente, gracias. ¿En qué puedo ayudarte?",
    "De qué te gustaría hablar?": "Podemos hablar sobre muchos temas. ¿Qué te interesa?",
    "ETC...": "¡Claro! Continúa la conversación o pregúntame algo específico."
}

# Función para manejar preguntas no reconocidas
def manejar_pregunta_desconocida(pregunta):
    respuesta = input("Lo siento, no entiendo tu pregunta. ¿Puedes proporcionar una respuesta para aprender de ello? (o escribe 'cancelar' para continuar): ")
    if respuesta.lower() != 'cancelar':
        respuestas_predefinidas[pregunta] = respuesta
        print("¡Entendido! Gracias por tu respuesta. Ahora puedo aprender de ello.")

# Función principal del chat
def chat():
    print("¡Hola! Soy un asistente de chat. Escribe 'salir' para terminar la conversación.")
    while True:
        entrada = input("Tú: ")
        if entrada.lower() == 'salir':
            print("Hasta luego. ¡Que tengas un buen día!")
            break

        # Buscar una respuesta predefinida
        respuesta = respuestas_predefinidas.get(entrada, None)

        if respuesta:
            print("Asistente: " + respuesta)
        else:
            manejar_pregunta_desconocida(entrada)

if __name__ == "__main__":
    chat()
