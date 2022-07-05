"""
Las palabras como primero, segundo y tercero se refieren
a números ordinales. En este ejercicio, escribirá una función
que toma un número entero como su único parámetro y devuelve
una cadena que contiene el número ordinal apropiado como único
resultado.

Su función debe manejar los enteros entre 1 y 12 (inclusive).
Debería devolver una cadena vacía si se proporciona un valor fuera de este rango como parámetro.
Incluya un programa principal que utilice su función mostrando cada número entero del 1 al 12 y su número ordinal.
"""

def numero_ordinal(n):
	lista_numeros_ordinales = ["primero", "segundo", "tercero", "cuarto", "quinto", "sexto", "septimo", "octavo", "noveno", "décimo", "décimo primero", "décimo segundo"]
	if 1 <= n <= 12:
		return lista_numeros_ordinales[n - 1]
	else:
		return " "

num = int(input("Ingrese el número: "))
print(numero_ordinal(num))