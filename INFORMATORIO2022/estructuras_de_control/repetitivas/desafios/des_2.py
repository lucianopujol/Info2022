"""
DESAFIO 2

Se inicia una campaña de recolección de colillas
de cigarrillos en los barrios.

Realizá un programa que permita registrar cantidad
de colillas recolectadas por un número determinado
de personas. Luego obtener estadísticas al respecto
informando porcentaje de personas que han encontrado
menos de 100 colillas, más de 100 y menos de 200, más
de 200 colillas.
"""

parar = "0"
mas = 0
men = 0
med = 0
per = 0

while parar == "0":
	cant = int(input("Ingrese la cantidad de colillas recolectadas: "))
	per = per	+ 1

	if 0 < cant < 100:
		men = men + 1
	elif 100 <= cant < 200:
		med = med + 1
	elif cant >= 200:
		mas = mas + 1
	else:
		print("ERROR")