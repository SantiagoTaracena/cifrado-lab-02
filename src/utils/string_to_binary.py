"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 2 - Base64
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para el desarrollo de la función string_to_binary.
from utils.string_to_number import string_to_number
from utils.number_to_binary import number_to_binary

# Función string_to_binary, que convierte un string a binario.
def string_to_binary(text: str, str_format: bool = False) -> list[str] | str:

    # Etapas de la conversión a binario.
    text_to_number: list[int] = string_to_number(text)
    binary_number: list[str] = number_to_binary(text_to_number)

    # Retorno del binario obtenido en formato de string.
    if (str_format):
        binary_number_str_format = str().join(binary_number)
        return binary_number_str_format

    # Retorno del binario obtenido.
    return binary_number
