"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 2 - Base64
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para la parte 2 del laboratorio.
import sys
import base64

from utils.string_to_binary import string_to_binary
from utils.xor_cipher import xor_cipher
from utils.binary_to_string import binary_to_number

# Cantidad de argumentos del programa.
ARGUMENTS: int = 3

# Verificación de los argumentos del sistema del programa.
if (len(sys.argv) != ARGUMENTS):
    print(f"Uso: python {sys.argv[0]} <image-path> <key>")
    sys.exit(1)

# Path de la imagen a descifrar.
cipher_image_path: str = sys.argv[1]

# Transformación de la imagen al formato de bytes deseado.
cipher_image: bytes = open(cipher_image_path, "rb").read()
cipher_image_base64_encoded: str = base64.b64encode(cipher_image).decode("utf-8")
cipher_image_base64_decoded: bytes = base64.b64decode(cipher_image_base64_encoded)
cipher_image_bytes: list[str] = [format(cipher_image_base64_decoded[i], "08b") for i in range(len(cipher_image_base64_decoded))]

# Llave a utilizar para descifrar la imagen.
key: str = sys.argv[2]

# Recreación de la llave para igualar el tamaño de la imagen.
if (len(key) < len(cipher_image_base64_decoded)):
    key *= len(cipher_image_base64_decoded) // len(key) + 1
    key = key[: len(cipher_image_base64_decoded)]

# Llave pasada al formato de bytes deseado.
complete_key: list[str] = string_to_binary(key)

# Resultado del XOR entre la imagen y la llave.
xor_result: list[str] = xor_cipher(cipher_image_bytes, complete_key)

# Bytes a escribir de la imagen resultante.
decipher_image_result: bytes = bytes(binary_to_number(xor_result))

# Escritura de la imagen resultante.
with open("./out/result.png", "wb") as file:
    file.write(decipher_image_result)

# Impresión de que la imagen ha sido descifrada correctamente.
print("\n¡Imagen descifrada! Ver \"./out/result.png\"\n")
