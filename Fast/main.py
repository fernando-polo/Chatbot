from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def inicio():
    return {
        "mensaje": "¡Hola! Bienvenido a la pizzería. Selecciona una opción:",
        "opciones": ["1. Ver menú", "2. Realizar pedido", "3. Consultas generales", "4. Salir"]
    }

@app.get("/menu")
def ver_menu():
    return {
        "menu": [
            {"pizza": "Margarita", "precio": 100},
            {"pizza": "Pepperoni", "precio": 120},
            {"pizza": "Vegetariana", "precio": 110}
        ]
    }

@app.post("/pedido")
def realizar_pedido(tipo_pizza: str, tamano: str, adicionales: Optional[str] = None):
    precio = 100  # Calcula el precio con base en los datos
    return {
        "pedido": {
            "tipo": tipo_pizza,
            "tamano": tamano,
            "adicionales": adicionales,
            "precio": precio
        },
        "mensaje": "¡Gracias por tu pedido! Será entregado pronto."
    }
