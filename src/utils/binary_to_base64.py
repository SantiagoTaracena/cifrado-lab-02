"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 2 - Base64

Miembros del equipo de trabajo:
- Gabriel Alejandro Vicente Lorenzo (20498)
- Santiago Taracena Puga (20017)
"""

# Módulos necesarios para la realización del laboratorio.
from utils.binary_to_number import binary_to_number

# Alfabeto a utilizar para cifrar con Base64.
base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# Función binary_to_base64 que cifra un binario en Base64.
def binary_to_base64(binary_number: list[str]) -> str:

    # Número binario mergeado en un sólo string.
    merged_binary_number: str = "".join(binary_number)

    # Instancia de los caracteres en binario de seis dígitos.
    base64_formatted_number: list[str] = list()

    # Caracter actual que se va a colocar.
    current_char: str = str()

    # Ciclo que obtiene cada caracter hasta tener seis dígitos en binario y de vuelta.
    for index, char in enumerate(merged_binary_number):
        if (index and index % 6 == 0):
            base64_formatted_number.append(current_char)
            current_char = str()
        current_char += char

    # Relleno del caracter final si no tiene seis dígitos.
    if (len(current_char) < 6):
        current_char = "0" * (6 - len(current_char)) + current_char

    # Conversión a número de cada caracter obtenido.
    base64_formatted_number.append(current_char)
    base64_result: str = str()
    actual_number = binary_to_number(base64_formatted_number)

    # Cifrado de todos los números que se encuentran en el texto.
    for number in actual_number:
        base64_result += str(base64_alphabet[number])

    # Retorno del resultado del proceso de cifrado.
    return base64_result
