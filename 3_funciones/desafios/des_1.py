"""
150 años es el tiempo que tarda una bolsa de plástico común en
degradarse y una botella de PET puede tardar 1.000 años en desaparecer. 

Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.

Un trozo de chicle tarda 5 años en degradarse. 

Se solicita una función para que dado el ingreso de un elemento, se
solicite tipo: Bolsa de plástico, botella PET, envase tetrabrik o chicle,
e imprima la cantidad de años que tarda en degradarse.
"""

print("BIENVENIDO!")

parar = 0

def degradado(tipo):
	if tipo == 1:
		print("Una bolsa de plástico tarda 150 años en degradarse.\n---------------------------------------------------------")
	elif tipo == 2:
		print("Una botella PET tarda 1.000 años en degradarse.\n---------------------------------------------------------")
	elif tipo == 3:
		print("Un envase Tetrabrick tarda 30 años en degradarse.\n---------------------------------------------------------")
	elif tipo == 4:
		print("Un chicle tarda 5 años en degradarse.\n---------------------------------------------------------")


while parar == 0:
	rta = int(input("Ingrese el tipo de elemento:\n1) Bolsa de plástico\n2) Botella PET\n3) Tetrabrick\n4) Chicle\nSu respuesta: "))
	degradado(rta)
	salir = input("¿Desea continuar? (s/n): ").lower()

	if salir == "n":
		parar = 1

print("PROGRAMA TERMINADO")