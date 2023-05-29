# Ejercicio 4: Almacenar 500 números en un vector, elevar al cuadrado cada valor almacenado en el
# vector, almacenar el resultado en otro vector. Imprimir el vector original y el vector
# resultante.

import random

primer_vector = []

segundo_vector = []


for i in range(0,20):
    
    elementos = random.randint(0,50)
    primer_vector.append(elementos)


for i in range (0,20):

    segundo_vector.append(primer_vector[i] ** 2)
    
    
print(f"Vector original: {primer_vector}")
print(f"Vector anterior elevado al cuadrado {segundo_vector}")
