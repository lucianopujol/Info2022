"""
DESAFIO 5

La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo
al nombre de la barrio y el tipo del barrio (CÉNTRICO y NO CÉNTRICO)

La sección A esta formada por los barrios céntricos cuyo nombre comienza con una
letra anterior a M y los barrios no céntricos con nombre posterior a la M, y la sección
B el resto.

Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe
en que sección se encuentra.
"""

print("BIENVENIDO!")
nombre = input("Ingrese el nombre del barrio: ").lower()
tipo = input("¿Se encuentra en Zona Céntrica? (SI/NO): ").lower()
print("---------------------")

if nombre[0] < "m" and tipo == "si":
	print("Se encuentra en la ZONA A.")
elif nombre[0] <= "m" and tipo == "no":
	print("Se encuentra en la ZONA B.")
elif nombre[0] >= "m" and tipo == "si":
	print("Se encuentra en la ZONA B.")
elif nombre[0] > "m" and tipo == "no":
	print("Se encuentra en la ZONA A.")
else:
	print("ERROR")