"""
Escribir un programa que almacene las matrices

A = [[1, 2, 3], [4, 5, 6]]

B = [[-1, 0], [0, 1], [1, 1]]

en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
"""

filas_A = int(input("Ingrese la cantidad de filas de la matriz A: "))
columnas_A = int(input("Ingrese la cantidad de columnas de la matriz A: "))
matriz_A = []

for fila in range(filas_A):
	a = []
	for columna in range(columnas_A):
		a.append(int(input(f"Ingrese el elemento {fila + 1}x{columna + 1}: ")))
	matriz_A.append(a)

filas_B = int(input("Ingrese la cantidad de filas de la matriz B: "))
columnas_B = int(input("Ingrese la cantidad de columnas de la matriz B: "))
matriz_B = []

for fila in range(filas_B):
	b = []
	for columna in range(columnas_B):
		b.append(int(input(f"Ingrese el elemento {fila + 1}x{columna + 1}: ")))
	matriz_B.append(b)

print(matriz_A)
print(matriz_B)