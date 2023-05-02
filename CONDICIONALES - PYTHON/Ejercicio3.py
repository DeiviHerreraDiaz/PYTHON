# TERCER EJERCICIO

num_llantas = int(input("Dependiendo del número de llantas que compre estas tendran un precio en especial\nSi compra menos de 5 su precio ronda por los 500 c/u\nSi compra de 5 a 10 llantas el precio rondara por los 250 c/u\nSi compra de 10 llantas en adelante su precio sera solamente de 200 c/u\nCuantas llantas desea comprar?\n"))


# CONDICIÓN

if num_llantas < 5:
    precio_llantas = 300
    precio_final = num_llantas * precio_llantas
    print("El precio que tendra cada llanta es de:",precio_llantas)
    print("El precio final que tendran todas las llantas es de:",precio_final)
elif num_llantas >= 5 and num_llantas < 10:
    precio_llantas = 250
    precio_final = num_llantas * precio_llantas
    print("El precio que tendra cada llanta es de:",precio_llantas)
    print("El precio final que tendran todas las llantas es de:",precio_final)
elif num_llantas > 10:
    precio_llantas = 200
    precio_final = num_llantas * precio_llantas
    print("El precio que tendra cada llanta es de:",precio_llantas)
    print("El precio final que tendran todas las llantas es de:",precio_final)
    
    
print("Hasta luego, vuelva pronto!")