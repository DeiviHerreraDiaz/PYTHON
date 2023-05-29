# CUARTO EJERCICIO

num_obreros = int(input("¿Cuantos obreros hay?\n"))

for i in range (num_obreros):
    
    horas = 0 
    totalhoras = 0 
    dineroExtra = 0 
    total = 0 
    
    
    print(f"{i+1} obrero")
    horas = int(input("Cuantas horas trabaja?\n"))
    
    if horas <= 40:
        totalhoras = horas * 20
        print(f"Se le pagara $20 por cada hora que hizo, osea el valor total por sus horas es {totalhoras}")
    elif horas > 40:
        
        primerasHoras = 40 * 20
        diferencia = horas - 40
        dineroExtra = diferencia * 25
        
        total = primerasHoras + dineroExtra
        
        print(f"Se le pagara {primerasHoras} por las primeras 40 horas que hizo, y de horas extra se le proporcionara un valor de {dineroExtra}, dando un total de {total}")