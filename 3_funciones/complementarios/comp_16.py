"""
Escriba dos funciones, hex2int e int2hex, que conviertan
entre dígitos hexadecimales (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E y F) y
enteros de base 10. La función hex2int es responsable de convertir
una cadena que contiene un solo dígito hexadecimal en un entero de base 10,
mientras que la función int2hex es responsable de convertir un entero entre 0
y 15 en un solo dígito hexadecimal. Cada función tomará el valor para convertir
como su único parámetro y devolverá el valor convertido como el único resultado de
la función. Asegúrese de que la función hex2int funcione correctamente para letras
mayúsculas y minúsculas. Sus funciones deberían finalizar el programa con un mensaje
de error significativo si se proporciona un parámetro no válido.
"""

def hex2int(string):
	resultado = ""
	string = string.upper()

	if "0" <= string <= "9":
		resultado += string
	if "A" <= string <= "F":
		if string == "A":
			resultado += "10"
		elif string == "B":
			resultado += "11"
		elif string == "C":
			resultado += "12"
		elif string == "D":
			resultado += "13"
		elif string == "E":
			resultado += "14"
		elif string == "F":
			resultado += "15"
	return resultado

def int2hex(string):
	resultado = ""

	if 0 <= int(string) <= 9:
		resultado = string
	if 10 <= int(string) <= 15:
		if int(string) == 10:
			resultado = "A"
		elif int(string) == 11:
			resultado = "B"
		elif int(string) == 12:
			resultado = "C"
		elif int(string) == 13:
			resultado = "D"
		elif int(string) == 14:
			resultado = "E"
		elif int(string) == 15:
			resultado = "F"

	return resultado

hexa = input("Ingrese el dígito hexadecimal: ")
dec = input("Ingrese el dígito en decimal: ")
print(hex2int(hexa))
print(int2hex(dec))