# Se tienen almacenados en la memoria dos vectores M y N de cien elementos cada uno.
# Hacer un algoritmo que escriba la palabra “Iguales” si ambos vectores son iguales y
# “Diferentes” si no lo son.
# Serán iguales cuando en la misma posición de ambos vectores se tenga el mismo valor para todos los elementos.
import  random
N = []
M = []
iguales = bool()
# Rellenamos los dos arreglos con valores aleatorios o con un valor para verificar
# la funcionalidad del ejercicio
for i in range (0, 99):
# for i in range (0):
    N.append(random.randrange(0, 100))
    #N.append(1)
for i in range (0,99):
# for i in range (0):
    M.append(random.randrange(0, 100))
    #M.append(1)
for i in range (len(N)):
    if N[i]!=M[i]:
        iguales=False 
    else:
        iguales=True
# Usamos operador ternario para informar si los arreglos son o no iguales
igualdad = ("Desiguales", "Iguales")[iguales]
print(f'Los arreglos son {igualdad}')