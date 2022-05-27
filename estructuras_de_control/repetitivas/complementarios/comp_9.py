"""
Un censador recopila ciertos datos aplicando encuestas para
el último Censo Nacional de Población y Vivienda. Desea obtener
de todas las personas que alcance a encuestar en un día, que porcentaje
tiene estudios de primaria, secundaria, carrera técnica, estudios profesionales y estudios de posgrado.
"""

encuestados = int(input("Ingrese la cantidad de personas encuestadas: "))
primaria = 0
secundaria = 0
tecnica = 0
profesional = 0
posgrado = 0

for i in range(1, encuestados + 1):
	print(f"Ingrese los estudios de la persona N°{i}:\n1) Primaria\n2) Secundaria\n3) Carrera Técnica\n4) Estudios profesionales\n5) Estudios de posgrado\nSu respuesta: ")
	res = int(input())

	if res == 1:
		primaria += 1
	elif res == 2:
		secundaria +=1
	elif res == 3:
		tecnica += 1
	elif res == 4:
		profesional += 1
	elif res == 5:
		posgrado += 1
	else:
		print("ERROR")

print(f"\n--------------------\nRESULTADOS\n{primaria * 100 / encuestados}% PRIMARIA\n{secundaria * 100 / encuestados}% SECUNDARIA\n{tecnica * 100 / encuestados}% TÉCNICA\n{profesional * 100 / encuestados}% PROFESIONAL\n{posgrado * 100 / encuestados}% POSGRADO")