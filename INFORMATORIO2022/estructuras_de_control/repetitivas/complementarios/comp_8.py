"""
Diseñar un programa que permita calcular el total de una compra,
ingresando cantidad y precio de los productos. El programa debe
estar preparado para que el ingreso de los datos se produzca hasta que el usuario lo desee
"""

parar = 0
total = 0

while parar == 0:
	c = float(input("Ingrese la cantidad del producto: "))
	p = float(input("Ingrese precio del producto: "))

	resultado = c * p
	total += resultado

	quit = input("¿Desea continuar? (s/n): ").lower()

	if quit == "n":
		parar = 1


print(f"El total de la compra es ${total}.")