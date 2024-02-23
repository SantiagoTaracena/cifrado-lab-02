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

El inciso 7 del laboratorio tiene como enunciado "Investigar por qué al aplicar XOR con una llave de texto la imagen se corrompe". La respuesta es que la corrupción de la imagen al aplicar XOR con una llave de texto ocurre debido a discrepancias en la longitud de la llave y la imagen, así como a la presencia de caracteres incompatibles en la llave. Es esencial que la llave tenga la misma longitud y formato adecuado para evitar esta corrupción.

El inciso 8 del laboratorio indica que se debe investigar cómo obtener el XOR de dos imágenes. La respuesta es que para aplicar XOR a dos imágenes, primero se deben representar las imágenes en forma de matrices de píxeles binarios y luego realizar la operación XOR elemento por elemento entre las matrices. Los principales inconvenientes que pueden surgir incluyen asegurarse de que las imágenes tengan la misma resolución y profundidad de bits, así como el manejo de diferentes formatos de color. Además, es esencial considerar la interpretación correcta de los resultados, ya que la operación XOR combina los bits en cada píxel, devolviendo 1 si los bits son diferentes y 0 si son iguales, lo que puede afectar la apariencia visual de la imagen resultante.

Finalmente, el contenido del inciso 9 se encuentra en el archivo `./src/main.ipynb`.
