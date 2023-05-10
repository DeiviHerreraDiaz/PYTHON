# SEGUNDO EJERCICIO

# En una tienda de descuento las personas que van a pagar el importe de su compra llegan a
# la caja y sacan una bolita de color, que les dirá que descuento tendrán sobre el total de su
# compra. Determinar la cantidad que pagara cada cliente desde que la tienda abre hasta
# que cierra.
#  Se sabe que, si el color de la bolita es rojo, el cliente obtendrá un 40% de
# descuento; si es amarilla un 25% y si es blanca no obtendrá descuento.
import random


print("Buenas tardes señor/a, el dia de hoy estamos haciendo la promoción de que pueda sacar una pelota y dependiendo de ello le haremos un descuento, ")

palabras = ['roja', 'amarilla', 'blaca']

num_productos = int(input("Cuantos productos compró?\n"))
suma = 0

# CICLO

for i in range(1,num_productos+1):
    precio = int(input(f"Digite el precio del producto {i}\n"))
     
    suma += precio
    


# RAMDOM PARA LAS PELOTAS :D

palabra_aleatoria = random.choice(palabras)

if palabra_aleatoria.lower() == "roja":
    
    descuento = suma * 0.40
    total_con_descuento = suma - descuento
    
    print(f"El total de su compra fue de: {suma}, y usted tuvo la suerte de sacar una pelota de color roja que le dara un 40% de descuento, su precio final con el descuento adquerido es de {total_con_descuento}")

elif palabra_aleatoria.lower() == "amarilla":
    
    descuento = suma * 0.25
    total_con_descuento = suma - descuento 
    
    print(f"El total de su compra fue de: {suma}, y usted tuvo la suerte de sacar una pelota de color amarilla que le dara un 25% de descuento, su precio final con el descuento adquerido es de {total_con_descuento}")

elif palabra_aleatoria.lower() == "blanca":
    
    print(f"El total de su compra fue de: {suma}, y usted tuvo la mala suerte de sacar una pelota de color blanca la cual no cuenta con ningun descuento")

