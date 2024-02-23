"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 2 - Base64
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para la parte 2 del laboratorio.
import base64

# Módulos necesarios para la parte 2 del laboratorio.
from utils.xor_cipher import xor_cipher
from utils.binary_to_number import binary_to_number

# Transformación de la imagen al formato de bytes deseado.
image_01: bytes = open("./data/image-01.png", "rb").read()
image_01_b64_encoded: str = base64.b64encode(image_01).decode("utf-8")
image_01_b64_decoded: bytes = base64.b64decode(image_01_b64_encoded)
image_01_bytes: list[str] = [format(image_01_b64_decoded[i], "08b") for i in range(len(image_01_b64_decoded))]

# Transformación de la imagen al formato de bytes deseado.
image_02: bytes = open("./data/image-02.png", "rb").read()
image_02_b64_encoded: str = base64.b64encode(image_02).decode("utf-8")
image_02_b64_decoded: bytes = base64.b64decode(image_02_b64_encoded)
image_02_bytes: list[str] = [format(image_02_b64_decoded[i], "08b") for i in range(len(image_02_b64_decoded))]

# Resultado del XOR de las dos imágenes.
xor_result: list[str] = xor_cipher(image_01_bytes, image_02_bytes)

# Bytes a escribir de la imagen resultante.
image_result: bytes = bytes(binary_to_number(xor_result))

# Escritura de la imagen resultante.
with open("./out/merge.png", "wb") as file:
    file.write(image_result)

# Impresión de que la imagen ha sido escrita correctamente.
print("\n¡Imágenes unificadas con XOR! Ver \"./out/merge.png\"\n")
