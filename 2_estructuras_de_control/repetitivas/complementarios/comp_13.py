"""
Un grupo de 100 estudiantes presentan un exámen de Física. Diseñe un diagrama
que lea por cada estudiante la calificación obtenida y calcule e imprima:

A.- La cantidad de estudiantes que obtuvieron una calificación menor a 50.

B.- La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 80.

C.- La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80.

D. La cantidad de estudiantes que obtuvieron una calificación de 80 o más.
"""

print("BIENVENIDO!")
estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
menor_50 = 0
mas_50_menor_80 = 0
mas_70_menor_80 = 0
mas_80 = 0

for alumno in range(estudiantes):
	calificacion = int(input("Ingrese la calificación: "))

	if calificacion > 100 or calificacion < 0:
		print("Calificación inválida")
	if calificacion >= 80:
		mas_80 += 1
	elif 70 <= calificacion < 80:
		mas_70_menor_80 += 1
	elif 50 <= calificacion < 80:
		mas_50_menor_80 += 1
	elif calificacion < 50:
		menor_50 += 1

print(f"-------------------------------------\nLa cantidad de estudiantes que obtuvieron una calificación:\n\nmenor a 50: ---> {menor_50}\n50 o más pero menor que 80: ---> {mas_50_menor_80}\n70 o más pero menor que 80: ---> {mas_70_menor_80}\n80 o más: ---> {mas_80}")