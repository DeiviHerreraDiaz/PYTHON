# Ejercicio 1: Calcular el promedio de 50 valores almacenados en un vector. Determinar, además
# cuantos son mayores que el promedio, imprimir el promedio, el número de datos mayores
# que el promedio y una lista de valores mayores que el promedio.

import random

lista = []
numeros_mayores = []
contador = 0


for i in range (0,50):
    
    elemento = random.randint(1,100)
    lista.append(elemento)

promedio = sum(lista) / len(lista)


for valor in lista:
    
    if valor > promedio:
        
        numeros_mayores.append(valor)
        
        contador += 1
        
        
print(f"EL PROMEDIO ES {promedio}")
print(F"EL NÚMERO DE DATOS MAYORES AL PROMEDIO ES {contador}")
print(f"La lista de valores mayores al promedio es {numeros_mayores}")


        
