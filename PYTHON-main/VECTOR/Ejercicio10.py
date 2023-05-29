#Diseñe un algoritmo que lea dos vectores A y B de 20 elementos cada uno y multiplique el
#primer elemento de A con el último elemento de B y luego el segundo elemento de A por
#el diecinueveavo elemento de B y así sucesivamente hasta llegar al veinteavo elemento de
#A por el primer elemento de B. El resultado de la multiplicación almacenarlo en un vector C.
import random
A=[]
B=[]
C=[]
for i in range(0, 5):
    A.append(random.randrange(0,10))
    B.append(random.randrange(0,10))

# Creamos un contador que recorra desde la última posición a la primera del arreglo
bIndex=len(A)-1

for i in range (len(A)):
    a = int(A[i])
    b= int(B[bIndex])
    resultado = int(a*b)
    C.append(resultado)
    bIndex-=1
# Imprimimos resultados
print(A)
print(B)
print(C)