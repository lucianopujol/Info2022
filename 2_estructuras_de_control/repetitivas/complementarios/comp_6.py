"""
Imprimir, contar y sumar los múltiplos de 2 que hay
entre una serie de números, tal que el segundo sea mayor o
igual que el primero.
"""

sumar = 0
contar = 0
n = int(input("Ingrese el n deseado: "))

for i in range(n+1):
	if i % 2 == 0:
		print(i)
		contar += 1
		sumar += i

print(f"Hay {contar} múltiplos de 2 y suma es {sumar}")