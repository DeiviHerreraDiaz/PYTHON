# Ejercicio 3: Llenar un vector de 20 elementos, imprimir la posición y el valor del elemento mayor
# almacenado en el vector. Suponga que todos los elementos del vector son diferentes.


# RELLENAR CON 20 ELEMENTOS 


import random 


elementos = []

for i in range(0,20):
    
    numero = random.randint(1,100)
    elementos.append(numero)

numeroMayor = elementos[0]

posicion = 0 

for indice in range(len(elementos)):
    if elementos[indice] > numeroMayor:
        numeroMayor = elementos[indice]
        posicion = indice

print(f"El número mayor es {numeroMayor} y su posición es {posicion}")