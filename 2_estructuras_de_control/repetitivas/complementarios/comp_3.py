"""
Diseñar un programa que permita obtener el producto entre A y B mediante sumas sucesivas

4*3 = 3+3+3+3 = 4+4+4
"""

print("Se calculará el producto de A por B mediante sumas sucesivas (Ej: B veces A)")
a = int(input("Ingrese A: "))
b = int(input("Ingrese B: "))
producto = 0

for n in range(b):
	producto += a

print(producto)