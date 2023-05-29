# CUARTO EJERCICIO



print("Bienvenido al juego de preguntas, si respondes bien las tres preguntas ganas, de lo contrario seras expulsado del juego")

print("1. ¿Colon descubrió América?")
eleccion = input("Escribe si o no\n")


# CONDICIÓN


if eleccion.lower() == "si":
    print("Respondiste de manera adecuada, puedes continuar con la siguiente pregunta")
    print("2. ¿La independencia de México fue en el año 1810?")
    eleccion = input("Escribe si o no\n")
    if eleccion.lower() == "si":
        print("Respondiste bien la segunda pregunta")
        print("3. ¿The Doors fue un grupo de rock americano?")
        eleccion = input("Escribe si o no\n")
        if eleccion.lower() == "si":
            print("Respondiste bien la tercer pregunta, acabas de ganar el juego :D")
        else: 
            print("Lo siento, respondiste mal la tercera pregunta")     
    else:
        print("Lo siento, respondiste mal la segunda pregunta")    
else: 
    print("Lo siento, respondiste mal la primer pregunta")