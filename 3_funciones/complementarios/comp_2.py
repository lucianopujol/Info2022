"""
En una jurisdicción particular, las tarifas de taxi consisten
en una tarifa base de $40.00, más $15.00 por cada 140 metros
recorridos. Escriba una función que tome la distancia recorrida
(en kilómetros) como su único parámetro y devuelva la tarifa total
como su único resultado. Escriba un programa principal que use la función.



Sugerencia: Utilice constantes para presentar la base y la porción
variable de las tarifas así el programa podrá actualizar fácilmente
cuando las tasas aumentan.
"""

def tarifa(kilometros):
	base = 40
	variable = 15
	recorrido = 140
	extra = kilometros * 1000 / recorrido
	return base + variable * extra

distancia = float(input("Ingrese la distancia recorrida en km: "))

print(f"Tarifa total: ${tarifa(distancia):.2f}")