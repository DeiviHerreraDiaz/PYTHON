# QUINTO EJERCICIO

edad = int(input("¿Cual es la edad del cliente?\n"))

boleta = 10000

if edad >= 5 and edad <= 14:
    descuento1 = boleta * 0.35
    print(f"Categoria 1\nEl teatro deja de percibir {descuento1} sobre el valor de la boleta actual")
    
if edad >= 15 and edad <= 19:
    descuento2 = boleta * 0.25
    print(f"Categoria 2\nEl teatro deja de percibir {descuento2} sobre el valor de la boleta actual")
    
if edad >= 20 and edad <= 45:
    descuento3 = boleta * 0.10
    print(f"Categoria 3\nEl teatro deja de percibir {descuento3} sobre el valor de la boleta actual")
    
if edad >= 46 and edad <= 65:
    descuento4 = boleta * 0.25
    print(f"Categoria 4\nEl teatro deja de percibir {descuento4} sobre el valor de la boleta actual")
    
if edad >= 66:
    descuento5 = boleta * 0.35
    print(f"Categoria 5\nEl teatro deja de percibir {descuento5} sobre el valor de la boleta actual")