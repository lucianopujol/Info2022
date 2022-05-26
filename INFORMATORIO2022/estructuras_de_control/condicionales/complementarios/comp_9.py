"""
En un Centro Asistencial existen tres áreas:
Pediatría, Traumatología y Kinesiología.
El presupuesto anual del hospital se reparte conforme a la sig. tabla:

ÁREA 		PORCENTAJE

Pediatría	60%

Traumatología	20%

Kinesiología	20%


Obtener la cantidad de dinero que recibirá cada área, para cualquier
monto presupuestal que se ingrese por teclado.
"""

pres = float(input("Ingrese el monto presupuestal: $"))

print(f"Pediatría: ${pres*0.6}\nTraumatología: ${pres*0.2}\nKinesiología: ${pres*0.2}")