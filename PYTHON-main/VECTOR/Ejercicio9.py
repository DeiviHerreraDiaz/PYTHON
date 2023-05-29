#Diseñe un algoritmo que lea un número cualquiera y lo busque en el vector X, el cual tiene
#almacenados 80 elementos. Escribir la posición donde se encuentra almacenado el
#número en el vector o el mensaje “NO” si no lo encuentra. Búsqueda secuencial.

import random
numeros = []
encontrado= bool()
numero_a_buscar= int(input('Ingresa el número a buscar en el arreglo \n'))

#Llenamos el arreglo con valores aleatorios
for i in range (0, 80):
    #numeros.append(1)
    numeros.append(random.randrange(0, 100))
print(numeros)
# Evaluamos el requerimiento
for i in range (0, 80):
    if numeros[i]==numero_a_buscar:
        encontrado=True
        print(f'{[i]}')
if encontrado==False:
    print('NO')