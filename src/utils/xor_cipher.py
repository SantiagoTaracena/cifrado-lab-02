from utils.binary_to_number import binary_to_number
from utils.number_to_string import number_to_string

def xor_cipher(binary_text: list[str], binary_key: list[str]) -> str:
    xor_cipher_result: list[str] = list()
    for text_number, key_number in zip(binary_text, binary_key):
        xor_number: str = str()
        for text_char, key_char in zip(text_number, key_number):
            xor_number += "0" if (text_char == key_char) else "1"
        xor_cipher_result.append(xor_number)
    
    return number_to_string(binary_to_number(xor_cipher_result))
