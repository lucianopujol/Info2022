"""
Leer 2 números; si son iguales que los multiplique, si
el primero es mayor que el segundo que los reste y si no que los sume.
"""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 == num2:
	print(f"El resultado es: {num1 * num2}")
elif num1 > num2:
	print(f"El resultado es: {num1 - num2}")
else:
	print(f"El resultado es: {num1 + num2}")