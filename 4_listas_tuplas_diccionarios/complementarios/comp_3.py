"""
Realice una función que dada una lista de enteros L, y un número entero n.
Elimine de la lista original los elementos que sean iguales a ese número dado.
"""

lista = [12, 2, 3, 44, 5]

def eliminar_lista(lista, numero):
	for i in lista:
		if i == numero:
			lista.remove(i)
	return lista

print(eliminar_lista(lista, 3))