"""
Leer una frase y luego invierta el orden de las palabras en la frase.
Por Ejemplo: “una imagen vale por mil palabras” debe convertirse en “palabras mil por vale imagen una”.
"""

def invertir_frase(frase):
	#Variables locales de la función
	lista = []
	palabra = ""
	resultado = ""

	#Se examina cada letra de la frase
	for letra in frase:
		if letra == frase[-1]:
			lista.append(palabra)
			palabra = ""
		elif letra != " ":
			palabra += letra
		elif letra == " ":
			lista.append(palabra)
			palabra = ""

	lista.reverse()

	for i in lista:
		resultado += i + " "

	return resultado

print(invertir_frase("una imagen vale por mil palabras."))