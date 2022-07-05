"""
Escribir un programa que pregunte a diferentes personas cuánto conocen
sobre contaminación del 1 al 10, almacene estos valores en una lista y los muestre por pantalla ordenados de menor a mayor. 
"""

def encuesta_contaminacion(personas):
	lista = []
	for persona in range(personas):
		respuesta = int(input("¿Cuánto conoce sobre contaminación del 1 al 10?:" ))
		lista.append(respuesta)
	lista.sort()
	return lista

print(encuesta_contaminacion(3))