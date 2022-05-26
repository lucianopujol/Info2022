"""
Realizar un programa que sea capaz de, habiéndose
ingresado dos números m y n, determine si n es divisor de m.
"""

m = int(input("Ingrese el dividendo: "))
n = int(input("Ingrese el divisor: "))

if m % n == 0:
	print(f"{n} es divisor de {m}")
else:
	print(f"{n} no es divisor de {m}")