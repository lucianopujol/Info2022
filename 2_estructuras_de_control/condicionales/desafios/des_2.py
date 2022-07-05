"""
DESAFIO 2

Para seguir colaborando en esta misión de salvar al planeta,
necesitamos que elabores un programa en Python que
dado el tamaño de un pez indique si su organismo está contaminado.
Para ello tendremos 4 opciones:

Tamaño Normal: Mensaje "Pez en buenas condiciones"
Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"
Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"
Tamaño sobredimensionado: Mensaje "Pez contaminado"
"""

tamaño = float(input("Ingrese el peso del pez en gramos: "))

if tamaño == 500:
	print("Pez en buenas condiciones")
elif tamaño < 500:
	print("Pez con problemas de nutrición")
elif 500 < tamaño < 1000:
	print("Pez con síntomas de organismo contaminado")
else:
	print("Pez contaminado")