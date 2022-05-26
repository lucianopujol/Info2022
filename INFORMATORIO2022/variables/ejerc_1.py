prod_1 = float(input("Ingrese precio del primer producto: "))
cant_1 = int(input("Ingrese la cantidad del primer producto: "))

prod_2 = float(input("Ingrese precio del segundo producto: "))
cant_2 = int(input("Ingrese la cantidad del segundo producto: "))

prod_3 = float(input("Ingrese precio del tercer producto: "))
cant_3 = int(input("Ingrese la cantidad del tercer producto: "))

res = cant_1*prod_1 + cant_2*prod_2 + cant_3*prod_3
res_iva = res * 1.21

cant_total = cant_1 + cant_2 + cant_3

print(f"El precio total incluyendo IVA es: ${res_iva} y la cantidad total de artículos es: {cant_total}")