#DADO EL MONTO DE COMPRA DE UN CLIENTE
#si LA COMPRA es MAYOR A #10000 DESCONTAR 5%
#si la compra es mayor a 15000 descontar 10%
#si la compra es mayor a 50000 descontar un 20%
#si la compra es mayor a 100000 descontar un 30%
# MOSTRAR AL FINAL EL MONTO TOTAL Y EL DESCUENTO REALIZADO

compra = float(input("Ingrese el monto de compra: "))

if compra > 10000 and compra < 15000:
	compra = compra*0.95
	descuento = 5
elif compra > 15000 and compra < 50000:
	compra = compra*0.9
	descuento = 10
elif compra > 50000 and compra < 100000:
	compra = compra*0.8
	descuento = 20
elif compra > 100000:
	compra = compra*0.7
	descuento = 30

print(f"El monto total a pagar es de ${compra} y el descuento realizado %{descuento}")