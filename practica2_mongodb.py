# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 23:18:44 2023

@author: david
"""

import pymongo

# Conexión a MongoDB (ajusta esta URL según tu configuración)
client = pymongo.MongoClient("mongodb+srv://antiantichambing:Cuandonaci2001.@cluster0.cjblkgk.mongodb.net/?retryWrites=true&w=majority")  
database = client.practicasSE  # Reemplaza "mi_base_de_datos" con el nombre de tu base de datos
practica2 = database["practica2"]


# Base de datos de respuestas predefinidas (puedes llenarla con respuestas por defecto)
respuestas_predefinidas = {
    "hola": "¡Hola! Estoy aquí para ayudarte. ¿Cómo estás?",
    "¿como estas?": "Estoy funcionando perfectamente, gracias. ¿En qué puedo ayudarte?",
    "de qué te gustaría hablar?": "Podemos hablar sobre muchos temas. ¿Qué te interesa?",
    "ETC...": "¡Claro! Continúa la conversación o pregúntame algo específico."
}

# Función para obtener respuestas personalizadas desde MongoDB
def obtener_respuesta_personalizada(pregunta):
    respuestas_personalizadas = practica2
    resultado = respuestas_personalizadas.find_one({"pregunta": pregunta})
    if resultado:
        return resultado["respuesta"]
    else:
        return None
    
# Función para manejar preguntas no reconocidas y guardar respuestas personalizadas en MongoDB
def manejar_pregunta_desconocida(pregunta):
    respuesta = input("Lo siento, no entiendo tu pregunta. ¿Puedes proporcionar una respuesta para aprender de ello? (o escribe 'cancelar' para continuar): ")
    if respuesta.lower() != 'cancelar':
        respuestas_predefinidas[pregunta] = respuesta
        print("¡Entendido! Gracias por tu respuesta. Ahora puedo aprender de ello.")
        # Guardar la respuesta personalizada en MongoDB
        respuestas_personalizadas = practica2
        data = {"pregunta": pregunta, "respuesta": respuesta}
        respuestas_personalizadas.insert_one(data)

# Resto del código del chat
def chat():
    print("¡Hola! Soy un asistente de chat. Escribe 'salir' para terminar la conversación.")
    while True:
        entrada = input("Tú: ")
        if entrada.lower() == 'salir':
            print("Hasta luego. ¡Que tengas un buen día!")
            break

        respuesta = respuestas_predefinidas.get(entrada, None)

        if respuesta:
            print("Asistente: " + respuesta)
        else:
            respuesta_personalizada = obtener_respuesta_personalizada(entrada)
            if respuesta_personalizada:
                print("Asistente: " + respuesta_personalizada)
            else:
                manejar_pregunta_desconocida(entrada)



if __name__ == "__main__":
    chat()

"""
db = client.practicasSE

practica2 = db["practica2"]

practica2.insert_one(
    {"dos": 2
     
     }
    
    )
"""