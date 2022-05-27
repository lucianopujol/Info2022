"""
Realizar un programa que calcule y muestre la suma
de los múltiplos de 5 comprendidos entre dos valores A y B.
El programa no permitirá introducir valores negativos para A y B
y verificará que A es menor que B. Si A es mayor que B, se deben intercambiar los valores.
"""

suma = 0

a = int(input("Ingrese el valor A: "))
b = int(input("Ingrese el valor B: "))

if a >= 0 and b >= 0:
	if a < b:
		for i in range(a, b+1):
			if i % 5 == 0:
				suma += i
		print(f"La suma de los múltiplos de 5 comprendidos entre {a} y {b} es {suma}")
	else:
		for i in range(b, a+1):
			if i % 5 == 0:
				suma += i
		print(f"La suma de los múltiplos de 5 comprendidos entre {b} y {a} es {suma}")
else:
	print("No se permiten ingresar números negativos.")