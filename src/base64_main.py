"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 2 - Base64

Miembros del equipo de trabajo:
- Gabriel Alejandro Vicente Lorenzo (20498)
- Santiago Taracena Puga (20017)
"""

# Librerías necesarias para la realización del laboratorio.
import os
import sys

# Módulos necesarios para la realización del laboratorio.
from utils.string_to_number import string_to_number
from utils.number_to_binary import number_to_binary
from utils.binary_to_number import binary_to_number
from utils.number_to_string import number_to_string
from utils.binary_to_base64 import binary_to_base64
from utils.base64_to_string import base64_to_string

# Cantidad de argumentos del programa.
ARGUMENTS: int = 2

# Verificación de los argumentos del sistema del programa.
if (len(sys.argv) != ARGUMENTS):
    print(f"Uso: python {sys.argv[0]} <text-to-cipher>")
    sys.exit(1)

# Verificación del texto pasado, ya que puede ser un archivo o texto plano.
if (os.path.isfile(sys.argv[1])):
    text: str = open(sys.argv[1], encoding="utf-8").read()
else:
    text: str = sys.argv[1]

# Procedimiento de convertir de texto a Base64.
text_in_numbers: list[int] = string_to_number(text)
text_in_binary: list[str] = number_to_binary(text_in_numbers)
text_in_base64: str = binary_to_base64(text_in_binary)

# Escritura del archivo con el resultado.
with open("./out/encrypted-text.txt", "w", encoding="utf-8") as file:
    file.write(text_in_base64)

# Impresión de la finalización del proceso.
print("\nFinished!\n")

# # Traducción al texto original nuevamente.
# original_string: str = base64_to_string(text_in_base64)
# print("og", original_string)
