compra = float(input("Ingrese el precio de compra: "))

if compra > 10000:
	compra = compra*0.9
	print(f"Su compra tiene un descuento del 10% y es ${compra}")
else:
	print(f"Su compra no tiene descuento y es ${compra}")

#EL PROFE LO HIZO ASÍ

"""
compra = float(input("Ingrese el precio de compra: "))

if compra > 10000:
	compra = compra*0.9

print(f"El monto total a pagar es de ${compra}")
"""