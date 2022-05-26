"""
Desarrollar una solución que calcule la suma de los cuadrados
de los n primeros números naturales: 1 + 22 + 32 +… + n2
"""

resultado = 0
n = int(input("Ingrese el n deseado: "))

for i in range(n+1):
	resultado += i ** 2

print(f"La sumatoria de n^2 es: {resultado}")