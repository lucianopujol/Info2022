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

personas = int(input("Ingrese la cantidad de personas: "))
menos_100 = 0
mas_100_menos_200 = 0
mas_200 = 0

for i in range(personas):

	colillas = int(input("Cantidad de colillas recolectadas: "))

	if colillas < 100:
		menos_100 += 1
	elif 100 <= colillas < 200:
		mas_100_menos_200 += 1
	elif colillas >= 200:
		mas_200 += 1

print(f"{menos_100 * 100 / personas}% encontraron menos de 100 colillas")
print(f"{mas_100_menos_200 * 100 / personas}% encontraron mas de 100 y menos de 200 colillas")
print(f"{mas_200 * 100 / personas}% encontraron más de 200 colillas")