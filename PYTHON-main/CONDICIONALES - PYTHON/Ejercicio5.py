# QUINTO EJERCICIO

# Leer tres números diferentes e imprimir el número mayor de los tres


print("PROGRAMA: DIGITARA 3 NÚMEROS Y COMO RESULTADO APARECERA EL NÚMERO MAYOR")

num1 = input("Digite el primer número:")
num2 = input("Digite el segundo número:")
num3 = input("Digite el tercer número:")


# CONDICIÓN

if num1 > num2 and num1 > num3: 
    print("El número mayor es:",num1)
elif num2 > num1 and num2 > num3:
    print("El número mayor es:",num2)
elif num3 > num1 and num3 > num2:
    print("El número mayor es:",num3)
else: 
    print("ERROR")


print("Hasta luego, vuelva pronto")
