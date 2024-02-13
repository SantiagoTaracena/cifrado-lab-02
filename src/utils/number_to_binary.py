"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 2 - Base64
Santiago Taracena Puga (20017)
"""

# Función string_to_number, que convierte un listado de números a su representación binaria.
def number_to_binary(number: list[int]) -> list[str]:

    # Instancia inicial del resultado de números binarios.
    binary_result: list[str] = list()

    # Ciclo que itera cada dígito ASCII para convertirlo a binario.
    for digit in number:

        # String donde se almacenará el dígito en binario.
        string_digit_result: str = str()

        # Ciclo que obtiene cada dígito binario mientras el número sea mayor a cero.
        while (digit > 0):

            # El dígito es el residuo entre el dígito y 2.
            string_digit_result += str(digit % 2)

            # El proceso continua con la división exacta entre el número y 2.
            digit //= 2

        # El binario generado se debe invertir, porque comienza desde el dígito mayor hasta el menor.
        string_digit_result = string_digit_result[::-1]

        # Verificación de que existe un octeto como último caracter de la cadena.
        if (len(string_digit_result) < 8):

            # Relleno de ceros para alcanzar los ocho caracteres.
            string_digit_result = "0" * (8 - len(string_digit_result)) + string_digit_result

        # Agregación del dígito al número binario.
        binary_result.append(string_digit_result)

    # Retorno del binario.
    return binary_result
