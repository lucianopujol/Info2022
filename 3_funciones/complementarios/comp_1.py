"""
Escriba una función que tome las longitudes de los dos lados más
cortos de un triángulo rectángulo como sus parámetros y devuelva
la hipotenusa del triángulo, calculada usando el teorema de Pitágoras,
como resultado de la función. Incluya un programa principal que lea
las longitudes de los lados más cortos de un triángulo rectángulo del
usuario, use su función para calcular la longitud de la hipotenusa y
muestre el resultado.
"""

import math

def hipotenusa(cateto_1, cateto_2):
	return math.sqrt(cateto_1**2 + cateto_2**2)

cat_1 = float(input("Ingrese el cateto 1: "))
cat_2 = float(input("Ingrese el cateto 2: "))

print(f"La hipotenusa vale {hipotenusa(cat_1, cat_2):.2f}")