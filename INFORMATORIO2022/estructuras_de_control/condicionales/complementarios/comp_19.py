"""
Una distribuidora de libros vende a librerías y a particulares.
Aplica bonificaciones por cantidad según el siguiente criterio:

i. a librerías: hasta 24 unidades, el 20%; más de 24 unidades, el 25%.

ii. a particulares: menos de 6 unidades, nada; desde 6 hasta 18 unidades,
el 5% y más de 18 unidades, el 10%.

El tipo de cliente está codificado así:

'L' para librerías
'P' para particular.

Dado el importe bruto de una compra de libros,
el tipo de cliente de que se trata y la cantidad total
pedida por el mismo, determinar el importe bruto bonificado.
"""

cant = int(input("Ingrese la cantidad de unidades: "))
imp = float(input("Ingrese el importe bruto: "))
cli = input("Tipo de cliente:\nL - librería\nP -particular\nIngrese opción (L-P): ").lower()


if imp > 0 and cant > 0:
	if cli == "l":
		if cant > 24:
			precio = imp*0.75
		elif 0 < cant <= 24:
			precio = imp*0.8
		else:
			print("La cantidad ingresada es inválida.")
		print(f"El importe bruto bonificado es ${precio}.")
	elif cli == "p":
		if 0 < cant <= 6:
			precio = imp
		elif 6 < cant <= 18:
			precio = imp*0.95
		elif cant > 18:
			precio = imp*0.9
		else:
			print("La cantidad ingresada es inválida.")
		print(f"El importe bruto bonificado es ${precio}.")
	else:
		print("El código de cliente es inválido.")
else:
	print("El importe/cantidad ingresado es inválido.")