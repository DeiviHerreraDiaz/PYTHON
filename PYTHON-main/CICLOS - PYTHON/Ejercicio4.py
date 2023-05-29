# CUARTO EJERCICIO

# Diseñe un diagrama que lea los 2,500,000 votos otorgados a los 3 candidatos a
# gobernador e imprima el número del candidato ganador y su cantidad de votos.

import random

print("PROGRAMA DE VOTOS REFERENTES A LOS CANDIDATOS A GOBERNADOR")

voto_can1 = 0

voto_can2 = 0

voto_can3 = 0



for i in range(2500000):
    voto = int(input("Ingrese el número del candidato por el cual desea votar (1, 2, 3)\n"))
    if voto == 1:
        voto_can1 += 1
    elif voto == 2:
        voto_can2 += 1
    elif voto == 3:
        voto_can3 += 1
    else:
        print("Voto invalido")


if voto_can1 > voto_can2 and voto_can1 > voto_can3:
    print(f"El ganador es el candidato número 1 con un numero de {voto_can1}")
elif voto_can2 > voto_can1 and voto_can2 > voto_can3:
    print(f"El ganador es el candidato número 2 con un numero de {voto_can2}")
elif voto_can3 > voto_can2 and voto_can3 > voto_can1 :
    print(f"El ganador es el candidato número 3 con un numero de {voto_can3}")

print("Hasta luego, vuelva pronto")


