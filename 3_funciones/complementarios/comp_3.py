"""
Un minorista en línea proporciona una forma de envío
urgente de $ 10.95 para el primer elemento y $ 2.95 para
cada segundo elemento posterior. Escriba una función que
tome el número de elementos en el pedido como su único parámetro.

Devuelva los gastos de envío del pedido como resultado de la función.

Incluya un programa principal que lea la cantidad de artículos comprados
al usuario y muestre los gastos de envío.
"""

def gastos_envio(elementos):
	if elementos == 1:
		return 10.95
	elif elementos > 1:
		return 10.95 + 2.95 * (elementos - 1)

cantidad_elementos = int(input("Ingrese la cantidad de elementos comprados: "))

print(f"Los gatos de envio son: ${gastos_envio(cantidad_elementos):.2f}")