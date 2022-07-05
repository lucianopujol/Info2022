"""
Escriba un algoritmo que permita cargar una lista. Y que luego, una vez cargada,
controle y sustituya cualquier elemento negativo por 0.
"""

def cargar_lista(elementos):

	lista = []

	for valor in range(1, elementos + 1):
		elemento = int(input(f"Ingrese el elemento Nº {valor}: "))

		if elemento < 0:
			lista.append(0)
		else:
			lista.append(elemento)

	return lista

num = int(input("Ingrese la cantidad de elementos a añadir: "))
print(cargar_lista(num))