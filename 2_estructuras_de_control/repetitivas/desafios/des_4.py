"""
Escriba un programa que permita imprimir un tablero Ecológico (verde y blanco)
de acuerdo al tamaño indicado. Por ejemplo el gráfico a la izquierda es el resultado de un tamaño: 8x6
"""

filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))
tablero = ""

for row in range(filas):
	if row % 2 == 0:
		for column in range(columnas):
			if column % 2 == 0:
				tablero += "[V]"
			else:
				tablero += "[B]"
	else:
		for column in range(columnas):
			if column % 2 == 0:
				tablero += "[B]"
			else:
				tablero += "[V]"

	print(tablero)
	tablero = ""