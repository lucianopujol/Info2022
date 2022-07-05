"""
Ejercicio 6: Centrar una cadena en la terminal

Escriba una función que tome una cadena de caracteres como
primer parámetro y el ancho de la terminal en caracteres como
segundo parámetro. Su función debe devolver una nueva cadena que
consta de la cadena original y el número correcto de espacios iniciales
para que la cadena original aparezca centrada dentro del ancho proporcionado
cuando se imprima. No agregue ningún carácter al final de la cadena.

Incluya un programa principal que use su función.
"""

def centrar(cadena, ancho_ter):
	ancho_cadena = len(cadena) #cuenta la cantidad de caracteres de la cadena
	ancho = (ancho_ter - ancho_cadena) // 2 # cuenta la cantidad de caracteres desde la mitad menos la cadena

	for i in range(ancho):
		cadena = " " + cadena

	return cadena

mensaje = "BIENVENIDO"
tamaño_terminal = 80

print(centrar(mensaje, tamaño_terminal)) #usando mi funcion
print(mensaje.center(tamaño_terminal, " ")) #usando una funcion de python
print("-" * tamaño_terminal) #imprime el tamaño de la terminal