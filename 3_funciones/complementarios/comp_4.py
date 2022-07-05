"""
Escriba una función que tome tres números como parámetros y
devuelva el valor medio de esos parámetros como resultado.
Incluya un programa principal que lea tres valores del usuario y muestre su mediana.

Sugerencia: El valor medio es el medio de los tres valores cuando
se ordenan en orden ascendente. Se puede encontrar usando declaraciones if, o con un poco de creatividad matemática.
"""

def mediana(a, b, c):
	lista_mediana = []
	lista_mediana.extend([a, b, c])
	lista_mediana.sort()
	return lista_mediana[1]

num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))
num_3 = int(input("Ingrese el tercer número: "))

print(f"La mediana de los números dados es: {mediana(num_1, num_2, num_3)}")