"""
En una jurisdicción particular, las matrículas más antiguas consisten
en tres letras seguidas de tres números. Cuando se utilizaron todas las
placas que siguen ese patrón, el formato se cambió a cuatro números seguidos
de tres letras. Escriba una función que genere una matrícula aleatoria.

Escriba un programa principal que llame a su función y muestre la placa generada al azar.
"""

import random

def matricula_aleatoria():
	matricula = ""
	tipo_de_matricula = random.randint(0, 1)

	if tipo_de_matricula == 1:
		for i in range(4):
			matricula += chr(random.randint(48, 57))
		matricula += "-"
		for i in range(3):
			matricula += chr(random.randint(65, 90))
	else:
		for i in range(3):
			matricula += chr(random.randint(65, 90))
		matricula += "-"
		for i in range(3):
			matricula += chr(random.randint(48, 57))

	return matricula

print(matricula_aleatoria())