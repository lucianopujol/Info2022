"""
Ingresar una palabra, carácter por carácter, en una lista y determinar si es palíndromo.
"""

def es_palindromo(palabra):
	lista = []

	for caracter in palabra:
		caracter = caracter.lower()
		lista.append(caracter)

	lista_reversa = lista.copy()
	lista_reversa.reverse()

	if lista == lista_reversa:
		return True
	else:
		return False

print(es_palindromo("LUCIANO"))