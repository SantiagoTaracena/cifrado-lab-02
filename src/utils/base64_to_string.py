"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 2 - Base64
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para la realización del laboratorio.
from utils.number_to_binary import number_to_binary
from utils.binary_to_number import binary_to_number
from utils.number_to_string import number_to_string

# Alfabeto a utilizar para cifrar con Base64.
base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# Función base64_to_string, que convierte un texto cifrado en Base64 a string sin cifrar.
def base64_to_string(base64_string: str) -> str:

    # Instancia del string de Base64 a binario a utilizar.
    base64_to_binary: str = str()

    # Iteración para obtener el binario de cada caracter del texto cifrado.
    for base64_char in base64_string:
        binary_listed: list[str] = number_to_binary([base64_alphabet.index(base64_char)])
        base64_to_binary += binary_listed[0][2:]

    # Verificación de que el binario sea múltiplo de ocho caracteres.
    if (len(base64_to_binary) % 8 != 0):

        # Instancia de la pieza a arreglar, que son los últimos seis caracteres.
        piece_to_rearrange: str = base64_to_binary[-6:]

        # Arreglo de los casos en que el número tenga cuatro o dos ceros de más.
        if (piece_to_rearrange.startswith("0000")):
            rearranged_piece: str = piece_to_rearrange[4:]
        elif (piece_to_rearrange.startswith("00")):
            rearranged_piece: str = piece_to_rearrange[2:]

        # Caracter final arreglado.
        base64_to_binary = base64_to_binary[:-6] + rearranged_piece

    # Instancia del listado binario y el caracter a agregar.
    binary_list: list[str] = list()
    current_char: str = str()

    # Ciclo que convierte el Base64 a binario convertible a string.
    for index, char in enumerate(base64_to_binary):
        if (index and index % 8 == 0):
            binary_list.append(current_char)
            current_char = str()
        current_char += char

    # Agregación del caracter.
    binary_list.append(current_char)

    # Retorno del número binario convertido a string.
    return number_to_string(binary_to_number(binary_list))
