"""
Haz un programa que almacene 5 elementos en una variable del tipo lista,
la modiﬁque para que cada componente sea igual al cuadrado del componente
original. El programa mostrara la lista resultante por pantalla.
"""

lista = []

for elemento in range(1, 6):
	entrada = int(input(f"Ingrese el elemento Nº {elemento}: "))
	lista.append(entrada)
	lista_cuadrado = [(i ** 2) for i in lista]

print(lista_cuadrado)