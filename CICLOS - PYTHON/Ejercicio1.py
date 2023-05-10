# PRIMER EJERCICIO

# Una compañía de seguros tiene contratados a n vendedores. Cada uno hace tres ventas a
# la semana. Su política de pagos es que un vendedor recibe un sueldo base y un 10% extra
# por comisiones de sus ventas. El gerente de su compañía desea saber cuánto dinero
# obtendrá en la semana cada vendedor por concepto de comisiones por las tres ventas
# realizadas, y cuánto gana tomando en cuenta su sueldo base y sus comisiones.

num_vendedores = int(input("Cuantos trabajadores tiene a cargo\n"))

sueldo_base = 1000000
valor = 0 
total_venta = 0


for i in range(num_vendedores):

    num_ventas = int(input("Digite el numero de ventas:\n"))
    total_venta = 0
    
    for j in range(num_ventas):
        valor = int(input("Digite el valor de la venta:\n"))
        total_venta += valor
    
    total_comision = total_venta * 0.10
    total = sueldo_base + total_comision
        
    
    print(f"El total de ventas fue de {total_venta}, y el concepto de comision por ellas fue de {total_comision}; teniendo como un sueldo final de {total}\n")
    
    