"""
En un supermercado se hace una promoción, mediante la cual
el cliente obtiene un descuento dependiendo de un número que
se escoge al azar. Si el número escogido es menor que 50 el
descuento es del 15% sobre el total de la compra, si es mayor o
igual a 50 el descuento es del 20%. Obtener cuánto dinero se le descuenta.
"""

import random

parar = 0

while parar == 0:
	precio = float(input("Ingrese el total de su compra: $"))
	num = random.randint(0, 100)
	print(f"El número que le ha tocado es: {num}")

	if num < 50:
		compra = 0.85 * precio
		descuento = precio - compra
	elif num >= 50:
		compra = 0.80 * precio
		descuento = precio - compra

	print(f"El total de su compra es ${compra} y se hizo un descuento de ${descuento}")
	salir = input("¿Desea salir? (s/n): ").lower()

	if salir == "s":
		parar = 1
		print("PROGRAMA TERMINADO")