# cifrado-lab-02

## Parte A

La parte A del presente laboratorio del curso de Cifrado consistió en realizar los ejercicios 1 a 4 que se encuentran en las instrucciones del laboratorio. Estos ejercicios consisten en una sección preliminar al "main event" que representa la parte B. Los ejercicios a resolver consisten en implementar funciones que sean capaces de transformar un string a binario y posteriormente a encoding Base64, y viceversa.

Para poder observar los resultados de la Parte A, ejecutar el siguiente comando:

```sh
python part_a_main.py
```

## Parte B

El primer inciso de la parte B consistió en desarrollar una función que haga el XOR, bit a bit, con dos cadenas de texto. Esta función se encuentra en `./src/utils/xor_cipher.py`. Posteriormente fue necesario descifrar una imagen dada con este método y con Base64. Para correr el programa que realiza este descifrado es necesario correr el siguiente comando:

```sh
python part_b_main.py "./data/image.png" "cifrados"
```
