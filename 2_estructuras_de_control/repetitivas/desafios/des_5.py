"""
Se está desarrollando un sistema de control de vehículos
desde donde se han tirado restos de basura a la vía pública.

Para ello la ciudad cuenta con sistemas de monitoreo de
patentes que devuelve 3 letras y un valor numérico de 5
dígitos a la Central con el siguiente significado:

3 letras: Correspondientes a la patente.
Del valor numérico:
	Los 3 primeros números corresponden a la patente
	El 4 número indica
		1- Tiró basura a la vía pública
		0 - No tiró basura a la vía pública
	El 5 número indica
		1- Ya había sido multado el vehículo
		0 - Vehículo sin multas.

EJEMPLO: AAA12310

Deberás informar cantidad de vehículos observados, cantidad
de vehículos que han tirado basura y porcentaje de éstos que
ya habían sido multados.
"""

parar = 0
observados = 0
tiro_basura = 0
multados = 0

while parar == 0:
	patente = input("Ingrese la patente del vehículo: ")

	if patente[6] == "1":
		tiro_basura += 1

	if patente[7] == "1":
		multados += 1

	observados += 1

	continuar = input("¿Desea continuar? (s/n): ").lower()

	if continuar == "n":
		parar = 1

print(f"Cantidad de vehiculos observados: {observados}\nCantidad de vehículos que han tirado basura: {tiro_basura}\nPorcentaje de vehículos que han sido multados: {multados * 100 / observados}")