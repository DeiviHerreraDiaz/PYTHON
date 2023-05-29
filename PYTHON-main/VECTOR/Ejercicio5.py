# Ejercicio 5: Almacenar 300 números en un vector, imprimir cuantos son ceros, cuantos son negativos,
# cuantos positivos. Imprimir además la suma de los negativos y la suma de los positivos.


import random

primer_vector = []
 

for i in range(0,20):
    
    elementos = random.randint(-50,50)
    primer_vector.append(elementos)


neutros = 0
negativos = 0 
positivos = 0  
suma = 0   
suma2 = 0                       


for valor in primer_vector:
    
    if valor == 0:
        neutros += 1

        
    elif valor < 0:
        negativos += 1
        suma += valor
        
    elif valor > 0:
        positivos += 1
        suma2 += valor
    
    
    
print(f"El primer vector esta compuesto por: {primer_vector}")
print(f"NEGATIVOS {negativos} y la suma de sus números es: {suma}")
print(f"POSITIVOS {positivos} y la suma de sus números es: {suma2}")
print(f"NEUTROS {neutros}")