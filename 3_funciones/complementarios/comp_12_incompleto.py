"""
En este ejercicio creará una función llamada proximo_primo que encuentra
y devuelve el primer número primo mayor que algún número entero, n.

El valor de n se pasará a la función como su único parámetro.

Incluya un programa principal que lea un número entero del usuario y
muestre el primer número primo mayor que el valor ingresado.
"""

def proximo_primo(numero):
	numero += 1

	for x in range(2, numero):
		if numero % x != 0:
			break
		else:
			numero += 1

	return numero

print(proximo_primo(7))