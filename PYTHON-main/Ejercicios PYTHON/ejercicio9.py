# CICLOS 3

num = int(input("Digite el numero que desea saber la tabla de multiplicar:"))
i = 1
print(f"TABLA DE MULTIPLICAR DEL NUMERO {num}")
while i <= 10: 
    resultado = num * i 
    print(f"{num}*{i}={resultado}")
    i=i+1