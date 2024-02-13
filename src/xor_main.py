from utils.string_to_number import string_to_number
from utils.number_to_binary import number_to_binary
from utils.xor_cipher import xor_cipher

text = "hello world"
key = "admin times"

print(xor_cipher(number_to_binary(string_to_number(text)), number_to_binary(string_to_number(key))))
