"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 2 - Base64

Miembros del equipo de trabajo:
- Gabriel Alejandro Vicente Lorenzo (20498)
- Santiago Taracena Puga (20017)
"""

# Inciso 1: String a bytes.

print("\nInciso 1: String a bytes.\n")

from utils.string_to_number import string_to_number
from utils.number_to_binary import number_to_binary

string_to_binary = lambda string: "".join(number_to_binary(string_to_number(string)))

example_text_1_1: str = "Hello, world!"
example_text_1_2: str = "The quick brown fox jumps over the lazy dog."

print(f"\nTexto de prueba 1: {example_text_1_1}\nResultado en binario: {string_to_binary(example_text_1_1)}\n")
print(f"\nTexto de prueba 2: {example_text_1_2}\nResultado en binario: {string_to_binary(example_text_1_2)}\n")

# Inciso 2: Bytes a string.

print("\nInciso 2: Bytes a string.\n")

from utils.binary_to_number import binary_to_number
from utils.number_to_string import number_to_string

binary_to_string = lambda string: number_to_string(binary_to_number(string))

example_binary_2_1: list[str] = ["01001000", "01100101", "01101100", "01101100", "01101111", "00101100", "00100000", "01110111", "01101111", "01110010", "01101100", "01100100", "00100001"]
example_binary_2_2: list[str] = ["01010100", "01101000", "01100101", "00100000", "01110001", "01110101", "01101001", "01100011", "01101011", "00100000", "01100010", "01110010", "01101111", "01110111", "01101110", "00100000", "01100110", "01101111", "01111000", "00100000", "01101010", "01110101", "01101101", "01110000", "01110011", "00100000", "01101111", "01110110", "01100101", "01110010", "00100000", "01110100", "01101000", "01100101", "00100000", "01101100", "01100001", "01111010", "01111001", "00100000", "01100100", "01101111", "01100111", "00101110"]

print(f"\nTexto de prueba 1: {example_binary_2_1}\nResultado en binario: {binary_to_string(example_binary_2_1)}\n")
print(f"\nTexto de prueba 2: {example_binary_2_2}\nResultado en binario: {binary_to_string(example_binary_2_2)}\n")

# Inciso 3: String a Base64.

print("\nInciso 3: String a Base64.\n")

from utils.binary_to_base64 import binary_to_base64

string_to_base64 = lambda string: binary_to_base64(number_to_binary(string_to_number(string)))

example_text_3_1: str = "Hello, world!"
example_text_3_2: str = "The quick brown fox jumps over the lazy dog."

print(f"\nTexto de prueba 1: {example_text_3_1}\nResultado en binario: {string_to_base64(example_text_3_1)}\n")
print(f"\nTexto de prueba 2: {example_text_3_2}\nResultado en binario: {string_to_base64(example_text_3_2)}\n")

# Inciso 4: Base64 a string.

print("\nInciso 4: Base64 a string.\n")

from utils.base64_to_string import base64_to_string

example_base64_4_1: str = "SGVsbG8sIHdvcmxkIB"
example_base64_4_2: str = "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZyO"

print(f"\nTexto de prueba 1: {example_base64_4_1}\nResultado en binario: {base64_to_string(example_base64_4_1)}\n")
print(f"\nTexto de prueba 2: {example_base64_4_2}\nResultado en binario: {base64_to_string(example_base64_4_2)}\n")
