#Se tiene el vector A con 100 elementos almacenados. Diseñe un algoritmo que escriba “SI”
# si el vector esta ordenado ascendentemente o “NO” si el vector no está ordenado
import random
A = []
ascendete= True
#Llenamos el arreglo con valores aleatorios
for i in range (0, 100):
    # Este append se usa si queremos comprobar la efectividad del ejercicio
    #A.append(i)
    A.append(random.randrange(0, 100))
#Comparamos el orden de el arreglo
print(A)
for i in range(len(A)-1):
    if A[i+1]>A[i] and ascendete==True: 
        ascendete=True
    else:
        ascendete=False
# Usamos operador ternario para informar los resultados al usuario
ascendete = ("NO", "SI")[ascendete]
print(ascendete)