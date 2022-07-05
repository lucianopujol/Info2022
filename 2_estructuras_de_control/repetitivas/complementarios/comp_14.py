"""
Una pizzería, vende sus pizzas en tres tamaños: pequeña, mediana; y grandes.
Una pizza puede ser sencilla (con sólo salsa y carne), o con ingredientes extras,
tales como pepinillos, champiñones o cebollas. Desarrolle una solución que calcule
el precio de venta de una pizza, dándole el tamaño y el número de ingredientes extras.
El precio de venta será 1.5veces el costo total, que viene determinado por el tamaño,
más el número de ingredientes. En particular el costo total se calcula sumando:

- un costo fijo de preparación. $2

- un costo variable que es proporcional al tamaño de la pizza. $0,5 $1 $1,5

- un costo adicional por cada ingrediente extra (por simplicidad se supone
que cada ingrediente extra tiene el mismo costo) $0,25
"""

parar = 0
total = 0

while parar == 0:
	tamaño = input("Tamaño de pizza:\n1) Pequeña\n2) Mediana\n3) Grande\n4) SALIR\nSu opción: ")
	
	if tamaño == "1":
		extras = int(input("Número de ingredientes extras: "))
		total = 2.5 + (0.25 * extras)
		print(f"--------------\nEl total a pagar es: ${total * 1.5}\n--------------")
	elif tamaño == "2":
		extras = int(input("Número de ingredientes extras: "))
		total = 3 + (0.25 * extras)
		print(f"--------------\nEl total a pagar es: ${total * 1.5}\n--------------")
	elif tamaño == "3":
		extras = int(input("Número de ingredientes extras: "))
		total = 3.5 + (0.25 * extras)
		print(f"--------------\nEl total a pagar es: ${total * 1.5}\n--------------")
	elif tamaño == "4":
		parar = 1
		print("--------------\nPROGRAMA TERMINADO")