"""
En este ejercicio escribirá una función que determina si una
contraseña es buena o no. Definiremos como una buena contraseña
aquella que tenga una longitud de al menos 8 caracteres y contenga
al menos una letra mayúscula, al menos una letra minúscula y al menos un número.

Su función debe devolver verdadero si la contraseña que se le pasó, como
único parámetro, es buena, de lo contrario debería devolver falso. Incluya
un programa principal que lea una contraseña del usuario e informe si es buena o no.
"""

contrasenia = input("Ingrese la contraseña a evaluar: ")

def evaluar_contrasenia(passwd):
	minus = False
	mayus = False
	numeric = False
	segura = False

	if len(passwd) >= 8:
		for i in passwd:
			if i.islower():
				minus = True
				break
		for i in passwd:
			if i.isupper():
				mayus = True
				break
		for i in passwd:
			if i.isnumeric():
				numeric = True
				break

		if minus and mayus and numeric:
			segura = True
			return segura
		else:
			return segura
	else:
		return segura

print(evaluar_contrasenia(contrasenia))