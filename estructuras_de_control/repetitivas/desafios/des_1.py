"""
DESAFIO 1

Nos han pedido desarrollar una aplicación móvil para reducir comportamientos
inadecuados para el ambiente.

a) Te toca escribir un programa que simule el proceso de Login. Para ello el
programa debe preguntar al usuario la contraseña, y no le permita continuar
hasta que la haya ingresado correctamente.

b) Modificar el programa anterior para que solamente permita una cantidad fija
de intentos. 
"""

usuario = "admin"
contrasenia = "1234"
user = ""
passwd = ""
count = 0

print("BIENVENIDO!")

while (usuario != user or contrasenia != passwd) and count < 3:
	user = input("Ingrese su usuario: ")
	passwd = input("Ingrese su contraseña: ")
	count = count + 1

	if usuario != user or contrasenia != passwd:
		print("\nUsuario/contraseña incorrecta.\n")
		if count == 3:
			print("--------------------------------\nSe acabaron los intentos.")
	elif usuario == user and contrasenia == passwd:
		print("\nIngresó correctamente.")