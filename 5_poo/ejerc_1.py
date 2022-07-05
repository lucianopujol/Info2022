"""
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
Construye los siguientes métodos para la clase:

Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
mostrar(): Muestra los datos de la persona.
esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
"""

class Persona:
	def __init__(self):
		self.nombre = None
		self.edad = None
		self.dni = None

	def set_nombre(self, nombre):
		self.nombre = nombre
		print(f"Se ha cambiado el nombre a: {self.nombre}")

	def set_edad(self, edad):
		self.edad = edad
		print(f"Se ha cambiado la edad a: {self.edad}")

	def set_dni(self, dni):
		self.dni = dni
		print(f"Se ha cambiado el DNI a: {self.dni}")

	def mostrar(self):
		print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nDNI: {self.dni}")

	def esMayorDeEdad(self):
		if self.edad >= 18:
			return True
		elif 0 <= self.edad < 18:
			return False
		else:
			print("La edad ingresada es inválida")

Luciano = Persona()
Luciano.set_nombre("Luciano")
Luciano.set_edad(27)
Luciano.set_dni("37796153")
print(Luciano.esMayorDeEdad())