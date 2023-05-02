# SEGUNDO EJERCICIO

print("Recuerde que las computadoras estan a un precio de 15.000 pesos\nSi usted compra menos de cinco computadoras le daremos un descuento de 10% al total de su compra\nSi usted compra más de cinco o igual a cinco y menores a 10 le otorgaremos un descuento de 20% al total de su compra\nSi usted compra 10 computadoras o más le otorgamos un descuento del 40% en el total de su compra")

num_computadoras = int(input("Cuantas computadoras desea comprar?:"))


# CONDICIÓN

if num_computadoras < 5:
    total = num_computadoras * 15000
    descuento_1 = total * 0.10
    total_descuento_1 = total - descuento_1
    print("El precio total de sus computadoras es:",int(total),"\nEl descuento del 10% a aplicar es:",int(descuento_1),"\nEL precio final junto al descuento es de:",int(total_descuento_1))
elif num_computadoras >= 5 and num_computadoras < 10:
    total = num_computadoras * 15000
    descuento_2 = total * 0.20
    total_descuento_2 = total - descuento_2
    print("El precio total de sus computadoras es:",int(total),"\nEl descuento del 20% a aplicar es:",int(descuento_2),"\nEL precio final junto al descuento es de:",int(total_descuento_2))
elif num_computadoras >= 10:
    total = num_computadoras * 15000
    descuento_3 = total * 0.40
    total_descuento_3 = total - descuento_3
    print("El precio total de sus computadoras es:",int(total),"\nEl descuento del 20% a aplicar es:",int(descuento_3),"\nEL precio final junto al descuento es de:",int(total_descuento_3)) 