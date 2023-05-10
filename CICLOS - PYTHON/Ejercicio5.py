# QUINTO EJERCICIO

# Un grupo de 100 estudiantes presentan un examen de Física. Diseñe un diagrama que lea
# por cada estudiante la calificación obtenida y calcule e imprima:
#  La cantidad de estudiantes que obtuvieron una calificación menor a 50 en el área
# del Tecnólogo en Análisis y Desarrollo de Sistemas de Información.
#  La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero
# menor que 70.
#  La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero
# menor que 80.
#  La cantidad de estudiantes que obtuvieron una calificación de 80 o más.
contador1 = 0 
contador2 = 0 
contador3 = 0 
contador4 = 0

for i in range(100): 
    calificacion = int(input("Digite su calificación:\n"))
    if calificacion < 50:
        contador1 += 1
    if calificacion >= 50 and calificacion < 70:
        contador2 += 1
    if calificacion >= 70 and calificacion < 80:
        contador3 += 1
    if calificacion >= 80:
        contador4 += 1 



print(f"La cantidad de estudiantes que tuvieron su calificacion por debajo de 50 fueron {contador1}")
print(f"La cantidad de estudiantes que tuvieron su calificacion entre 50 y menor a 70 fueron  {contador2}")
print(f"La cantidad de estudiantes que tuvieron su calificacion entre 70 y menor a 80 fueron  {contador3}")
print(f"La cantidad de estudiantes que tuvieron su calificacion de 80 o más fueron {contador4}")