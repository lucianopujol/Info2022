compra = float(input("Ingrese el monto de compra: "))

if compra > 100000:
	compra = compra*0.7
	descuento = 30
elif compra > 50000:
	compra = compra*0.8
	descuento = 20
elif compra > 15000:
	compra = compra*0.9
	descuento = 10
elif compra > 10000:
	compra = compra*0.95
	descuento = 5
else:
	descuento = 0

print(f"El monto total a pagar es de ${round(compra)} y el descuento realizado %{descuento}")