"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 2 - Base64

Miembros del equipo de trabajo:
- Gabriel Alejandro Vicente Lorenzo (20498)
- Santiago Taracena Puga (20017)
"""

# Función string_to_number, que convierte un string a caracteres numéricos ASCII.
def string_to_number(string: str) -> list[int]:

    # Instancia inicial de la lista de números ASCII.
    number_result: list[int] = list()

    # Ciclo que convierte cada caracter del string a un número ASCII.
    for char in string:
        number_result.append(ord(char))

    # Retorno del listado de caracteres numéricos ASCII.
    return number_result
