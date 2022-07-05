"""
Realiza una función separar(lista) que tome una lista que tenga
datos de cantidad de árboles plantados en diferentes ciudades de
Argentina durante la cuarentena. Luego la función debe devolver dos
listas ordenadas. La primera con las cantidades que superen los 100 y la segunda con el resto.

Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena.
"""

arboles = [2754, 50, 25, 350, 1522, 45, 755]

def separar(lista):

	lista_mayor_100 = []
	lista_resto = []

	for item in lista:
		if item > 100:
			lista_mayor_100.append(item)
		else:
			lista_resto.append(item)

	lista_mayor_100.sort()
	lista_resto.sort()

	print(f"Lista con cantidades que superan los 100: {lista_mayor_100}\nLista con el resto: {lista_resto}")

separar(arboles)