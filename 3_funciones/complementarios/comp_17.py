"""
Escriba un programa que permita al usuario convertir un número
de una base a otra. Su programa debe admitir bases entre 2 y 16
tanto para el número de entrada como para el número de resultado.

Si el usuario elige una base fuera de este rango, se debe mostrar el
mensaje de error apropiado y el programa debe salir. Divida su programa
en varias funciones, incluida una función que convierte de una base
arbitraria a una base 10, una función que convierte de una base 10 a
una base arbitraria y un programa principal que lee las bases y el número
de entrada del usuario.
"""

def base_arbitraria_a_base_10(num, base):
	resultado = 0
	lista_digitos = [int(i) for i in str(num)]
	digitos = len(lista_digitos) - 1

	for i in lista_digitos:
		resultado += i * (base ** digitos)
		digitos = digitos - 1

	return resultado

def base_10_a_base_arbitraria(num, base):
	cociente = num / base
	
	resto_lista = []

	while cociente > base:

		resto_lista = resto_lista.append(num % base)
		cociente = cociente / base

	print(resto_lista)

#base = int(input("Ingrese la base: "))
#numero = int(input(f"Ingrese el número en base {base}: "))

#print(f"El resultado en base 10 es: {base_arbitraria_a_base_10(numero, base)}")

base_10_a_base_arbitraria(13, 2)