cap = int(input("Digite el capital: "))
p_int = int(input("Digite el interes del banco"))

interes = cap * p_int/100

if interes>7000:
    capf = cap + interes
    print("El capital final es de: ",int(capf))
    print("Le recomiendo reinvertir")
else:
    print("No gano mucho interes, le recomiendo no reinvertir")


    