def calculadora(a, b, c):
	if a == "+":
		resultado = b + c
	elif a == "-":
		resultado = b - c
	elif a == "*":
		resultado = b * c
	elif a == "/":
		resultado = b / c
	else:
		resultado = "ERROR"

	return resultado

operacion = input("Ingrese la operación (+ - * /): ")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

res = calculadora(operacion, num1, num2)

print(f"El resultado es {res}")

