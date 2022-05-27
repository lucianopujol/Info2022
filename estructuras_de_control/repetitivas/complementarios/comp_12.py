"""
Calcular el monto a pagar por cada cliente y total recaudado
en una estación de servicio. Debe diseñar un programa que permita monto
por cliente y el total recaudado por la gasolinera, tomando en cuenta lo siguiente:

El precio del litro es para el Tipo A $50, para el Tipo B $ 55 y para el Tipo C $60

El programa finaliza cuando se introduce una D como tipo de gasolina.
"""

parar = 0
total = 0

while parar == 0:
	tipo = input("Ingrese el tipo de gasolina:\nA) $50\nB) $55\nC) $60\nD) SALIR\nSu opción: ").lower()
	
	if tipo == "a":
		litros = float(input("Ingrese la cantidad de litros: "))
		precio = litros*50
		print(f"El precio es ${precio}\n---------------------------------")
		total = total + precio
	elif tipo == "b":
		litros = float(input("Ingrese la cantidad de litros: "))
		precio = litros*55
		print(f"El precio es ${precio}\n---------------------------------")
		total = total + precio
	elif tipo == "c":
		litros = float(input("Ingrese la cantidad de litros: "))
		precio = litros*60
		print(f"El precio es ${precio}\n---------------------------------")
		total = total + precio
	elif tipo == "d":
		parar = 1
	else:
		print("ERROR")

print(f"---------------------------------\nEl monto total recaudado por la gasolinera es ${total}")