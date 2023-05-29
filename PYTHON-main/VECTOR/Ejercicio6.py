#6. Almacenar 150 números en un vector, almacenarlos en otro vector en orden inverso al
# vector original e imprimir el vector resultante.
import  random
numeros = []
numeros_inversos = []

# Rellenamos el arreglo con números generados aleatoriamente
for i in range (0, 99):
    numeros.append(random.randrange(0, 100))

# Definimos un acumulador para leer el arrego al revés y guardar sus valoes en el arreglo numeros_inversos
acumulador_numeros_inversos=-1
for i in range (1):
    numeros_inversos.append(numeros[::acumulador_numeros_inversos])
    acumulador_numeros_inversos-=1

# Imprimimos los resultados
print(f'Arreglo inicial: {numeros}')
print(f'Arreglo incial ivertido{numeros_inversos}')