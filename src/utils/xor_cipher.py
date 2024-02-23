"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 2 - Base64
Santiago Taracena Puga (20017)
"""

# Función xor_cipher, que obtiene el resultado de aplicar XOR a dos números binarios.
def xor_cipher(binary_text: list[str], binary_key: list[str], str_format: bool = False) -> list[str] | str:

    # Instancia del resultado final del XOR como lista.
    xor_cipher_result: list[str] = list()

    # Ciclo que itera el texto y la llave de las cuales obtener el XOR.
    for text_number, key_number in zip(binary_text, binary_key):

        # Instancia inicial del resultado del XOR de dos caracteres.
        xor_number: str = str()

        # Ciclo que itera el caracter actual del texto y la llave.
        for text_char, key_char in zip(text_number, key_number):

            # El resultado del XOR es cero si los números son iguales y uno si no.
            xor_number += "0" if (text_char == key_char) else "1"

        # Agregación del resultado parcial al resultado final.
        xor_cipher_result.append(xor_number)

    # Retorno del resultado del XOR en formato de string.
    if (str_format):
        xor_cipher_result_str_format: str = str().join(xor_cipher_result)
        return xor_cipher_result_str_format

    # Retorno del resultado del XOR.
    return xor_cipher_result
