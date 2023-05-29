# CICLOS 6

num = int(input("Digite el numero que desea saber la tabla de multiplicar:"))
print(f"TABLA DE MULTIPLICAR DEL NUMERO {num}")

for i in range(10+1): 
    
    resultado = num * i 
    print(f"{num}*{i}={resultado}")
