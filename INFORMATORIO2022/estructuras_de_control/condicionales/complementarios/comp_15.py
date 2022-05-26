"""
Un obrero necesita calcular su salario semanal, el cual se
obtiene de la siguiente manera:

i. Si trabaja 40 horas o menos se le paga $16 por hora

ii. Si trabaja más de 40 horas se le paga $16 por cada una
de las primeras 40 horas y $20 por cada hora extra.
"""

horas = int(input("Ingrese horas trabajadas: "))

if horas < 0:
	print("No se pueden ingresar números negativos.")
elif horas <= 40:
	salario = horas*16
elif horas > 40:
	base = 40*16
	salario = base + (horas - 40)*20

print(f"Su salario es de ${salario}")