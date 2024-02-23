"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 2 - Base64

Miembros del equipo de trabajo:
- Gabriel Alejandro Vicente Lorenzo (20498)
- Santiago Taracena Puga (20017)
"""

# Librerías necesarias para la realización del laboratorio.
import sys

# Módulos necesarios para la realización del laboratorio.
from utils.string_to_number import string_to_number
from utils.number_to_binary import number_to_binary

# Cantidad de argumentos del programa.
ARGUMENTS: int = 2

# Verificación de los argumentos del sistema del programa.
if (len(sys.argv) != ARGUMENTS):
    print(f"Uso: python {sys.argv[0]} <text-to-binary>")
    sys.exit(1)

# Texto a pasar a binario.
text_to_binary: str = sys.argv[1]

# Procedimiento de convertir el texto a binario.
text_in_numbers: list[int] = string_to_number(text_to_binary)
text_in_binary: str = str().join(number_to_binary(text_in_numbers))

# Resultado obtenido de la conversión a binario.
print(f"\nTexto en binario: {text_in_binary}\n")
