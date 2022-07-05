"""
Crea un diccionario donde la clave sea el nombre de biólogos y
el valor sea el email (no es necesario validar). Tendrás que ir
pidiendo contactos hasta el usuario diga que no quiere insertar mas.

No se podrán insertar nombres repetidos.
"""

mail_contactos = {}

while True:
	nombre = input("Ingrese el nombre del biólogo/a: ")
	mail = input(f"Ingrese el mail de {nombre}: ")
	mail_contactos.setdefault(nombre, mail)
	salir = input("----------------------------------------------------\n¿Desea continuar? (s/n): ")
	print("----------------------------------------------------")

	if salir.lower() == "n":
		break

print(f"Se guardaron los siguientes contactos: {mail_contactos}")