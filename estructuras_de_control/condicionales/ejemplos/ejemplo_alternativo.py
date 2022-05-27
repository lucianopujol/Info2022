#DADO EL MONTO DE COMPRA DE UN CLIENTE, OFRECER UN DESCUENTO DEL 10%
#SIEMPRE Y CUANDO LA COMPRA SEA MAYOR A #10000
#PERO SI LA MISMA ES MENOR O IGUAL A 10000, iNRREMENTARLE UN 5%

compra = float(input("Ingrese el monto de compra: "))

if compra > 10000:
	compra = compra*0.9
	descuento = 10
	print(f"El monto total a pagar es de ${compra} y el descuento realizado %{descuento}")
else:
	compra = compra*1.05
	recargo = 5
	print(f"El monto total a pagar es de ${compra} y el recargo realizado %{recargo}")