# Ejercicio 2: Llenar dos vectores A y B de 45 elementos cada uno, sumar el elemento uno del vector A
# con el elemento uno del vector B y así sucesivamente hasta 45, almacenar el resultado en
# un vector C, e imprimir el vector resultante.

# VECTORES:


import random 

A = []
B = []
C = []





# RELLENO DEL VECTOR A

for i in range(0,45):
    
    
    elementos = random.randint(1,100)
    A.append(elementos)
    
# RELLENO DEL VECTOR B

for i in range (0,45):
    
    elementos2 = random.randint(1,100)
    B.append(elementos)

# RELLENO DEL VECTOR C

for i in range (0,45):
    
    C.append(A[i] + B[i])
    
print(f"VECTOR A: {A}")
print(f"VECTOR B: {B}")
print(f"La suma de los vectores A y B es la siguiente: {C}")