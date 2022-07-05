"""
Escribir un programa que cargue una tupla con nombres de especie, y
para cada nombre de especie imprima el mensaje Hola soy ......, cuidame.

Modificá el programa anterior y dada una posición inicial p y una
cantidad n, imprima el mensaje anterior para los n nombres que se
encuentran a partir de la posición i.
"""

def saludo(inicial, cantidad):

	inicial = inicial - 1

	nombres_especies = ("Carcharodon carcharias",
	"Panthera onca",
	"Canis lupus baileyi",
	"Panthera tigris tigris",
	"Priodontes maximus",
	"Panthera leo krugeri",
	"Ara militaris",
	"Ambystoma mexicanum",
	"Crocodylus acutus",
	"Ursus arctos nelsoni",
	"Acinonyx jubatus"
	"Cynomys mexicanus",
	"Campephilus imperialis",
	"Ursus maritimus",
	"Acerodon jubatus")

	for especie in nombres_especies[(inicial):(inicial + cantidad)]:
		print(f"Hola soy {especie}, cuidame.")

saludo(4,5)