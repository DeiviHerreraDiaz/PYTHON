print("CRONOMETRO DE TIEMPOS :D")


# TIEMPOS

lunes = int(input("Ingrese el tiempo del dia lunes:"))
miercoles = int(input("Ingrese el tiempo del dia miercoles:"))
viernes = int(input("Ingrese el tiempo del dia viernes:"))

# PROCESO

pro = (lunes+miercoles+viernes) / 3

print("El promedio entre los tiempos de los 3 dias es:",int(pro))


if lunes == 100:
    print("SI ES")
else: 
    print("No es")