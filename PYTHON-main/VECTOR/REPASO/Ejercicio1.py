# 1. Calcular el promedio de 50 valores almacenados en un vector. Determinar, además
# cuantos son mayores que el promedio, imprimir el promedio, el número de datos mayores
# que el promedio y una lista de valores mayores que el promedio.

valores = [30, 30, 30, 50]
mayores_promedio = []
promedio = 0

for i in range (len(valores)):
    promedio += valores[i]

promedio = (promedio / (len(valores)))

for i in range (len(valores)):
    if valores[i]>promedio:
        mayores_promedio.append(valores[i])

print('El promedio es de: ', promedio)
print('El total de los números mayores al promdedio es de:', len(mayores_promedio))
print('y fueron: ' , mayores_promedio)
