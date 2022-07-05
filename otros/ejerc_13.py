"""
Escribir un programa que pregunte por una muestra de números,
separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
"""

import statistics

numeros = [input("Ingrese los números separados por una coma: ")]

print(numeros)

media = statistics.mean(numeros)
sd = statistics.stdev(numeros)

print(f"La media de los datos proporcionados es: {media} y la desviación típica: {sd}")