# CICLOS 5

num = 1 
pos = 0
nega = 0 
neu = 0


for i in range(5):
    
    numeros = int(input("Digite un número:"))
    
    if numeros == 0:
        neu+=1
    elif numeros >0:
        pos+=1
    elif numeros < 0:
        nega+=1    
    
    
print(f"Hay {pos} números positivos")
print(f"Hay {nega} números negativos")
print(f"Hay {neu} números neutros")