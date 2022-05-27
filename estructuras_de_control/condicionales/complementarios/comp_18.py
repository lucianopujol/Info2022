"""
Se leen tres números que son las longitudes
de los lados de un triángulo. Determinar e
informar si el mismo es equilátero (3 lados iguales),
isósceles (2 lados iguales) o escaleno (3 lados distintos).
"""

l1 = float(input("Ingrese la longitud del primer lado: "))
l2 = float(input("Ingrese la longitud del segundo lado: "))
l3 = float(input("Ingrese la longitud del tercer lado: "))

if l1 == l2 == l3:
	print("El triángulo es equilátero.")
elif l1 == l2 or l1 == l3 or l3 == l2:
	print("El triángulo es isósceles.")
else:
	print("El triángulo es escaleno.")