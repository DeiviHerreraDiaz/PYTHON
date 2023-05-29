# EJERCICIO 2

num_Hectareas = int(input("¿Cuantas hectareas esta compuesto la superficie?\n"))

PROCESO = num_Hectareas * 10000

if PROCESO > 1000000:
    
    # PORCENTAJES
    
    print("1")
 
 
    pino = PROCESO * 0.70
    oyamel = PROCESO * 0.20
    cedro = PROCESO * 0.10
    
    print(f"Buenas tardes, el total de metros cuadrados que hay es de {PROCESO}, el cual se va a sembrar de la siguiente manera:\nPino: {pino}\nOyamel: {oyamel}\nCedro: {cedro}")
    
elif PROCESO <= 1000000:
    
    
    print("2")
    
    pino = PROCESO * 0.50
    oyamel = PROCESO * 0.30
    cedro = PROCESO * 0.20
    
    print(f"Buenas tardes, el total de metros cuadrados que hay es de {PROCESO}, el cual se va a sembrar de la siguiente manera:\nPino: {pino}\nOyamel: {oyamel}\nCedro: {cedro}")