"""
Crea una tupla con los factores que más afectan a los mares.
Luego para jugar con niños y niñas, aprendiendo sobre contaminación
del agua crea un programa que pida números, si el numero esta entre
1 y la longitud máxima de la tupla, muestra el contenido de esa posición
sino muestra un mensaje de error.

El programa termina cuando el usuario introduce un cero.
"""

factores = ("", "Aguas residuales",
	"Sustancias químicas tóxicas",
	"Aguas pluviales",
	"Vertido de plásticos",
	"Vertidos de petroleo",
	"Actividad minera",
	"Cambio climático")

while True:
	numero = int(input("Ingrese un número: "))
	if numero == 0:
		break
	elif 1 <= numero < len(factores):
		print(factores[numero])
	else:
		print("ERROR")