# PRIMER EJERCICIO

num1 = int(input("Digite el primer número:"))
num2 = int(input("Digite el segundo número:"))


# CONDICIÓN

if num1 == num2:
    resultado = num1*num2
    print("El resultado de la mutiplicación es:",resultado)
elif num1 > num2:
    resultado = num1 - num2
    print("El resultado de la resta es:",resultado)
else:
    resultado = num1 + num2
    print("El resultado de la suma es:",resultado)
    
    