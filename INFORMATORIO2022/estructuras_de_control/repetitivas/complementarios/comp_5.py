"""
Solicitar el ingreso de números al usuario y emitir un
mensaje para determinar si es par o impar. El ciclo debe
finalizar cuando el usuario ingresa 0.
"""

parar = 0

while parar == 0:
	x = int(input("Ingrese un número: "))

	if x == 0:
		parar = 1
	elif x % 2 == 0:
		print(f"{x} es un número par")
	else:
		print(f"{x} es un número impar")

print("Programa terminado")