"""
Un equipo de fútbol ha tenido una buena campaña y
desea premiar a sus jugadores con un aumento del
salario para la siguiente campaña. Los sueldos deben
ajustarse de la siguiente forma:

Sueldo Actual (en $)    Aumento

0 – 6000							15%

6000 – 7900					   10%

7900 – 12000					6%

Más de 12000				   0%

Diseñar un programa que lea el salario de un jugador, y
que a continuación muestre el tanto por ciento de
aumento, el sueldo actual y el sueldo aumentado.
"""

salario = float(input("Ingrese el salario del jugador: $"))

if salario > 12000:
	aumento = 0
	salario_aumentado = salario*(1 + aumento)
elif 7900 < salario < 12000:
	aumento = 0.06
	salario_aumentado = salario*(1 + aumento)
elif 6000 < salario < 7900:
	aumento = 0.1
	salario_aumentado = salario*(1 + aumento)
elif 0 < salario < 6000:
	aumento = 0.15
	salario_aumentado = salario*(1 + aumento)

print(f"El aumento de su salario es del {aumento*100}%, su salario actual es ${salario} y su salario aumentado es de ${salario_aumentado}")