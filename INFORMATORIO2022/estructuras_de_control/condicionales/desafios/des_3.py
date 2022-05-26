"""
DESAFIO 3

Para el uso de fertilizantes es necesario medir cuánto abarca un determinado compuesto en el suelo el cual debe
existir en una cantidad de al menos 10% por hectárea, y no debe existir vegetación del tipo MATORRAL. Escribir un
programa que determine si es factible la utilización de fertilizantes.
"""

superficie = float(input("Ingrese la superficie cubierta por fertilizante (ha): "))
hectarea = float(input("Ingrese la superficie total (ha): "))
tipo_vegetacion = input("Ingrese el tipo de vegetación en MAYÚSCULAS: ")

sup_cubierta = superficie / hectarea

if sup_cubierta >= 0.1 and tipo_vegetacion != "MATORRAL":
	print("Es factible la utilización de fertilizante.")
else:
	print("No es factible la utilización de fertilizante.")