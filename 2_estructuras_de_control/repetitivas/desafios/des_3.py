"""
En una tienda de descuento por reciclado las personas que
van a pagar el importe de su compra llegan a la caja y ofrecen
tapitas para reciclar, de acuerdo a la cantidad que lleven en la
caja le entregan un código de descuento que se aplicará sobre el
total de su compra. Determinar la cantidad que pagara cada cliente
desde que la tienda abre hasta que cierra. 

Se sabe que si el código de descuento es rojo se obtendrá un 40% de descuento;
si es amarilla un 25% y si es blanca no obtendrá descuento.

Mas de 100 tapitas = 40%
Entre 25 y 100 tapitas = 25%
Menos de 25 tapitas = 0%
"""

print("BIENVENIDO!")
parar = 0
descuento = 0
color = ""

while parar == 0:
	tapitas = int(input("Cantidad de tapitas que desea reciclar: "))
	importe = float(input("Ingrese el monto a pagar: $"))

	if tapitas > 100:
		importe = importe * 0.6
		color = "Rojo"
		descuento = 40
	elif 25 <= tapitas <= 100:
		importe = importe * 0.75
		color = "Amarillo"
		descuento = 25
	elif 0 <= tapitas < 25:
		color = "Blanco"
		descuento = 0
	elif tapitas < 0:
		print("ERROR: No puede ingresar números negativos.")

	print(f"El monto a pagar es ${importe} y el descuento realizado es {descuento}%, correspondiente con el color: {color}.")

	continuar = input("¿Desea continuar? (s/n): ").lower()

	if continuar == "n":
		parar = 1

print("PROGRAMA TERMINADO")