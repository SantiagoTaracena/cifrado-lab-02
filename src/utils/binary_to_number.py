"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 2 - Base64

Miembros del equipo de trabajo:
- Gabriel Alejandro Vicente Lorenzo (20498)
- Santiago Taracena Puga (20017)
"""

# Función binary_to_number, que convierte un binario a listado de números.
def binary_to_number(binary: list[str]) -> list[int]:

    # Listado de números a retornar.
    number_list: list[int] = list()

    # Iteración de los binarios del listado.
    for binary_number in binary:

        # Número traducido de binario a decimal.
        number_result: int = int()

        # Ciclo que itera en cada caracter del binario.
        for index, char in enumerate(binary_number):

            # Conversión multiplicando por 2 a la potencia del índice.
            int_char = int(char) * (2 ** (len(binary_number) - (index + 1)))
            number_result += int_char

        # Agregación del número obtenido.
        number_list.append(number_result)

    # Retorno del listado de números obtenido.
    return number_list
