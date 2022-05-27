"""
Un comercio ofrece un descuento del 15% sobre el
total de la compra si esta supera los $1000. Obtenga
para determinado cliente cuánto deberá pagar finalmente
por su compra y el descuento obtenido, si es que corresponde.
"""

total = float(input("Ingrese el total de su compra: $"))

if total > 1000:
	pagar = total*0.85
	print(f"El total a pagar es ${pagar} y el descuento realizado es del 15%.")
elif total <= 0:
	print("El monto ingresado es inválido.")
else:
	print(f"El total a pagar es ${total} y no hay descuento realizado.")