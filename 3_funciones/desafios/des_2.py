"""
Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas de dos ciudades se cumpla lo siguiente:

Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.

Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.

Si ambos números son iguales, debe devolver el nombre de ambas.
"""

def relacion(a, b):
	if a > b:
		print("CIUDAD 1")
	elif a < b:
		print("CIUDAD 2")
	elif a == b:
		print("CIUDAD 1 y CIUDAD 2")

parar = 0

while parar == 0:
	num1 = int(input("Ingrese el primer número: "))
	num2 = int(input("Ingrese el segundo número: "))

	relacion(num1, num2)

	salir = input("¿Desea continuar? (s/n): ").lower()

	if salir == "n":
		parar = 1

print("PROGRAMA TERMINADO")