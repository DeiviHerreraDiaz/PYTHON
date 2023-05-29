# TERCER EJERCICIO

# El profesor de una materia desea conocer la cantidad de sus alumnos que no tienen
# derecho al examen de nivelación.

# Diseñe un algoritmo que lea las calificaciones obtenidas en las 5 materias por cada uno de
# los 40 alumnos y escriba la cantidad de ellos que no tienen derecho al examen de
# nivelación.


print("Sea bienvenido al algoritmo de notas")

print("Si el estudiante pasa con 40 o más en el total de sus materias fue aprobado \n Si el estudiante pasa con 30 o más pasa con un nivel muy bajo\n Si el estudiante obtiene 20 en adelante tiene derecho a recuperacion pero si el estudiante saca menos de eso no tendra derecho a un examen de nivelación")

contador = 0 

for i in range(40): 
    
    print(f"Estudiante #{i+1}\n")
    suma = 0 
    for j in range(5):
        
        nota = int(input(f"Digite la nota de la materia {j+1}\n"))
        
        suma += nota
        
        promedio = suma / 5
                    
    print(f"El promedio de las notas del estudiante es de {promedio}")
    if promedio >= 40:
        print("Fue aprobado con excelentes notas, felicidades")
    elif promedio >=30:
        print("El estudiante aprobó con un nivel academico promedio")
    elif promedio >= 20:
        print("Reprobó pero tiene derecho a presentar el examen de nivelación, animos")
    elif promedio < 20:
        print("Reprobó y no tiene derecho al examen de nivelación")
        contador+=1
        
print(f"El número de estudiantes que no pueden presentar el examen son {contador}")

        
        