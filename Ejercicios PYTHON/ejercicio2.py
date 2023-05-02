sueldo_base = int(input("Ingrese su sueldo:"))


ven1 = float(input("Digite la primer venta del mes: "))
ven2 = float(input("Digite la primer venta del mes: "))
ven3 = float(input("Digite la primer venta del mes: "))

total = ven1 + ven2 + ven3

porcentaje = total *  0.10

sueldofinal = sueldo_base + porcentaje

print("Su sueldo base es de",sueldo_base,", el total de sus ventas es de ",int(total)," y tendra un extra de", int(porcentaje),"por esas ventas")
print("Nuestro sueldo total es de",int(sueldofinal))

