"""
Determinar el número mayor de 10 números ingresados

TIP:Ir guardando en una variable el número más grande
"""

valor = 0

for i in range(1, 11):
	x = int(input(f"Ingrese el número {i}: "))

	if x > valor:
		valor = x

print(f"El número más grande es {valor}")