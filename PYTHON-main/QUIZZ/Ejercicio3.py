# EJERCICIO 3

niño = 0 
joven = 0 
Adulto = 0 
Viejo = 0

totalpesoNiños = 0 
totalpesoJovenes = 0 
totalpesoAdulto = 0 
totalpesoViejo = 0 

promedioniño = 0
promediojoven = 0
promedioadulto = 0
promedioviejo = 0
    

    
for i in range(5):
        
    edad = int(input(f"Hola persona {i+1}, digite su edad\n"))
    
    print("--------------")
    
    if edad >= 0 and edad <= 12:
        niño += 1
        print("Usted entra en la categoria de niños") 
        peso = int(input("Digite su peso en kg\n"))
        totalpesoNiños = totalpesoNiños + peso
        promedioniño = totalpesoNiños / niño 
        
    elif edad > 13 and edad <= 29:
        joven += 1
        print("Usted entra en la categoria de Jóvenes") 
        peso = int(input("Digite su peso en kg\n"))
        totalpesoJovenes = totalpesoJovenes + peso
        promediojoven = totalpesoJovenes / joven
        
        
    elif edad > 30 and edad <= 59:
        Adulto += 1 
        print("Usted entra en la categoria de Adultos") 
        peso = int(input("Digite su peso en kg\n"))
        totalpesoAdulto = totalpesoJovenes + peso
        promedioadulto = totalpesoAdulto / Adulto
        
    elif edad > 60:
        Viejo += 1
        print("Usted entra en la categoria de personas de la tercera edad") 
        peso = int(input("Digite su peso en kg\n"))
        totalpesoViejo = totalpesoViejo + peso
        promedioviejo = totalpesoViejo / Viejo
    
   
    
    
print(f"La cantidad de niños: {niño} \nLa edad promedio entre los niños es de {promedioniño}")
print(f"La cantidad de jóvenes: {joven} \nLa edad promedio entre los jovenes es de {promediojoven}")
print(f"La cantidad de adultos: {Adulto} \nLa edad promedio entre los adultos es de {promedioadulto}")
print(f"La cantidad de viejos: {Viejo} \nLa edad promedio entre los viejos es de {promedioviejo}")
    
