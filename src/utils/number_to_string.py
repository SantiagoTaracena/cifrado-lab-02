"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 2 - Base64

Miembros del equipo de trabajo:
- Gabriel Alejandro Vicente Lorenzo (20498)
- Santiago Taracena Puga (20017)
"""

# Función number_to_string que convierte un listado de números a un string.
def number_to_string(number: list[int]) -> str:

    # Instancia del string a devolver.
    string_result: str = str()

    # Agregación de cada caracter al resultado.
    for ascii_number in number:
        string_result += chr(ascii_number)

    # Retorno del resultado obtenido.
    return string_result
