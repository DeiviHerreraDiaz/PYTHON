# EJERCICIO 1

# CONTEXTO: DINERO PRESTADO POR EL BANCO A CAMBIO DE HIPOTECAR SU CASA

valor_negocio = int(input("Digite el valor del negocio\n"))
valor_hipoteca = int(input("Digite el valor de la hipoteca\n"))

# CONDICIONAL

if valor_hipoteca < 1000000: 
    
    
    PROCESO = valor_negocio - valor_hipoteca
    PROCESO2 = PROCESO / 2 

    print(f"El valor de la hipoteca que nos brindaron fue de {valor_hipoteca}\nEl valor del negocio es de {valor_negocio} \n  Pienso invertir {PROCESO2} y mi compañero me ayuda con el resto que seria {PROCESO2}")
elif valor_hipoteca > 1000000:
    
    
    PROCESO = valor_negocio - valor_hipoteca
    
    print(f"El monto total de la hipoteca que nos brindaron fue de {valor_hipoteca} \nCon lo cual nos ayuda para repartirnos entre mi compañero y yo un total de {PROCESO}")