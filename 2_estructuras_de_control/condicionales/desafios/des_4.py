"""
DESAFIO 4

Tenemos que decidir entre 2 recetas ecológicas. Los ingredientes para cada tipo de receta aparecen a continuación.

Ingredientes comunes: Verduras y berenjena.

Ingredientes Receta 1: Lentejas y apio.

Ingredientes Receta 2: Morrón y Cebolla..

Escribir un programa que pregunte al usuario que tipo de receta desea, y en función de su respuesta le muestre un menú
con los ingredientes disponibles para que elija. Solo se puede eligir 3 ingrediente (entre la receta elegida y los comunes.)
y el tipo de receta. Al final se debe mostrar por pantalla la receta elegida y todos los ingredientes.
"""

print("MENÚ\n-----------------------\n¿Que tipo de receta desea?\n1) Receta 1\n2) Receta 2")
receta_elegida = input("Ingrese la opción elegida (1-2): ")
print("-----------------------\n¿Que ingrediente desea?\n1) Verduras\n2) Berenjena")
verdura_elegida = input("Ingrese la opción elegida (1-2): ")
print("-----------------------")

if receta_elegida == "1" and verdura_elegida == "1":
	print("Usted eligió la receta 1 y todos los ingredientes son: Lentejas, apio y verduras.")
elif receta_elegida == "1" and verdura_elegida == "2":
	print("Usted eligió la receta 1 y todos los ingredientes son: Lentejas, apio y berenjena.")
elif receta_elegida == "2" and verdura_elegida == "1":
	print("Usted eligió la receta 2 y todos los ingredientes son: Morrón, cebolla y verduras.")
elif receta_elegida == "2" and verdura_elegida == "2":
	print("Usted eligió la receta 2 y todos los ingredientes son: Morrón, cebolla y berenjena.")
else:
	print("La opción elegida no es válida.")