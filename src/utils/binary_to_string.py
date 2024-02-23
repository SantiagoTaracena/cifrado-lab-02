"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 2 - Base64

Miembros del equipo de trabajo:
- Gabriel Alejandro Vicente Lorenzo (20498)
- Santiago Taracena Puga (20017)
"""

# Módulos necesarios para el desarrollo de la función binary_to_string.
from utils.binary_to_number import binary_to_number
from utils.number_to_string import number_to_string

# Función binary_to_string, que convierte un binario a string.
def binary_to_string(binary: list[str]) -> str:

    # Etapas de la conversión a string.
    number: list[int] = binary_to_number(binary)
    text_result: str = number_to_string(number)

    # Retorno del string obtenido.
    return text_result
