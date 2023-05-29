# ESTRUCTURAS DE DATOS:


# LISTAS

# lista = ["Pedro", "Pablo"]
# print(lista)

# segunda_lista = list("Pedro", "Pablo", "Ariza", "Brayan")
# print(segunda_lista)

# lista_con_elementos = [1,2,True,"Hola",5.8]


# lista_con_elementos[1] = 10
# print(lista_con_elementos)

# # IMPRIMIR POSICIONES 

# mi_lista = ["Juan", "Pedro", "Laura", "Carmen"]

# print(mi_lista[0])
# print(mi_lista[1])
# print(mi_lista[2])
# print(mi_lista[3])

# # prueba

# print("--------")

# print(mi_lista[-4])


# CICLO FOR

# edades = [20,41,6,18,23]

# edades.append(60)

# # for indice in range(5):
    
# #     # end="" : Linea de seguido
# #     print(edades[indice],end="")
    
# # Recorriendo los elementos

# for edad in edades: 
#     print(edad)
    
    
    
# # RECORRIENDO INDICES

# for i in range (len(edades)):
#     print(edades[i])



# print("La longitud de la lista:", len(edades))

# print("------------")

# # Con while y los indices

# indice = 0

# while indice < len(edades):
#     print(edades[indice])
    
#     indice+= 1

# print("-------------")

# POSICIONES


# letras = ["a","b","c","d","e","f","g","h","i","j"]


# # # PRIMER CASO
# print(letras[1:4])
# # # SEGUNDO CASO
# print(letras[2:7:2])
# # # TERCER CASO
# print(letras[7:])
# # # CUARTO CASO
# print(letras[:5:3])
# # # QUINTO CASO
# print(letras[:2:2])
# # # SEXTO CASO
# print(letras[::-1])



# RELLENAR UN VECTOR CON UN CiCLO (CON NÚMEROS)

# numeros = []

# for i in range (0,10):
#     numeros.append(i+1)
#     print(numeros[i])

# print("----------------")

# # RELLENAR VECTOR CON UN INPUT

# Hola = []

# for i in range (0,10,1):
#     n = int(input("Ingrese un número: "))
#     Hola.append(n)

# print(Hola)

# print("------------------")

# UNIR LISTAS

# a = [12,13,14]
# b = ["Hola","como","estas"]

# union = a + b

# print(union)

# print("---------------")

# palabras = ["Hola","Hello","ola"]

# palabras.pop(0)
# palabras.remove()

# print(palabras)


# EJERCICIO:
# numeros = []
# par = []
# impar = []


# for i in range (0,101):
#     numeros.append(i)


# for i in range (len(numeros)):
    
#     if numeros[i] %2 == 0:
#         par.append(i)
#     else:
#         impar.append(i)

# print("Pares",par)
# print("impares", impar)


# SEGUNDO EJERCICIO


A = [5,9,8,30,9,13]
B = []
# for i in range(len(A)):
    
#     if A[i] > 3:
#         if A[i] %2 == 1:
#             print(A[i])
            
# OTRA FORMA

for i in range (len(A)):
    if i > 3 & i %2 != 0:
        print(i)