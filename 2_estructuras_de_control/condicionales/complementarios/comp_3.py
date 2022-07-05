"""
Determinar si el primero de un conjunto de tres números dados, es
menor que los otros dos.
"""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 < num2 and num1 < num3:
	print(f"{num1} es menor que {num2} y {num3}")
elif num1 > num2 and num1 > num3:
	print(f"{num1} es mayor que {num2} y {num3}")
elif num1 < num2 and num1 > num3:
	print(f"{num1} es menor que {num2} y mayor que {num3}")
elif num1 > num2 and num1 < num3:
	print(f"{num1} es menor que {num3} y mayor que {num2}")