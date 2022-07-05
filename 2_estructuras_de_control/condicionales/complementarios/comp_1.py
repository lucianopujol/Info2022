"""
Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.
"""

#EL PROFE UTILIZÓ IF ANIDADOS

numbers = []
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

numbers.append(num1)
numbers.append(num2)
numbers.append(num3)
numbers.sort(reverse=True)
print(numbers)