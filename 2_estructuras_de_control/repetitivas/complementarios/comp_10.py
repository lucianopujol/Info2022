"""
Mostrar los perímetros de varios triángulos ingresados sus lados por teclado, hasta que ya no desee
"""

parar = 0

while parar == 0:
	l1 = float(input("Ingrese el lado 1: "))
	l2 = float(input("Ingrese el lado 2: "))
	l3 = float(input("Ingrese el lado 3: "))
	print(f"\nEl perímetro del triángulo es: {l1 + l2 + l3}\n---------------------\n¿Desea continuar? (s/n)")
	salir = input().lower()

	if salir == "n":
		parar = 1