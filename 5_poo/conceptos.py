"""
Una clase para profesores y otra clase para alumnos
Con los atributos y los metodos que querramos para cada cual. 
Y a partir de eso crear algunos prof y alumnos
"""

class Profesor:
	def __init__(self, nombre, apellido, edad, genero, especialidad):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.genero = genero
		self.especialidad = especialidad

	def enseniar(self):
		print(f"{self.nombre} enseña a sus alumnos")

class Alumno:
	def __init__(self, nombre, apellido, edad, genero, grado):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.genero = genero
		self.grado = grado

	def aprender(self):
		print(f"{self.nombre} aprende del profesor")

alumno1 = Alumno("Luciano", "Pujol", 27, "Masculino", "Universitario incompleto")
alumno2 = Alumno("Ezequiel", "Pujol", 30, "Masculino", "Secundario completo")
profesor1 = Profesor("Laura", "Gimenez", 45, "Femenino", "Posgrado completo")
profesor2 = Profesor("Silvia", "Magaldi", 34, "Femenino", "Universitario completo")

profesor1.enseniar()
alumno1.aprender()

print(alumno2.nombre)
print(profesor2.especialidad)