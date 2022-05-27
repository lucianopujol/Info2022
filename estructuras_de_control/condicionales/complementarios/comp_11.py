"""
Determinar si un alumno aprueba a reprueba un
curso, sabiendo que aprobara si su promedio de
tres calificaciones es mayor o igual a 70; desaprueba en caso contrario.
"""

cal1 = float(input("Ingrese la primera calificación: "))
cal2 = float(input("Ingrese la segunda calificación: "))
cal3 = float(input("Ingrese la tercera calificación: "))

promedio = (cal1 + cal2 + cal3) / 3

if 0 < cal1 < 100 and 0 < cal2 < 100 and 0 < cal3 < 100:
	if promedio >= 70:
		print("El alumno aprueba el curso.")
	else:
		print("El alumno reprueba el curso.")
else:
	print("Se ha ingresado una calificación incorrecta.")