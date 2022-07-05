from caso_1 import Vehiculo, Coche

class Camioneta(Vehiculo):
	def __init__(self, color, ruedas, carga):
		super().__init__(color, ruedas)
		self.carga = carga

	def setCarga(self, nueva_carga):
		self.carga = nueva_carga

	def getCarga(self):
		return self.carga

	def __str__(self):
		return super().__str__() + f"\nCarga: {self.carga}"

class Bicicleta(Vehiculo):
	def __init__(self, color, ruedas, tipo):
		super().__init__(color, ruedas)
		self.tipo = tipo

	def setTipo(self, nuevo_tipo):
		self.tipo = nuevo_tipo

	def getTipo(self):
		return self.tipo

	def __str__(self):
		return super().__str__() + f"\nTipo: {self.tipo}"

class Motocicleta(Vehiculo):
	def __init__(self, color, ruedas, velocidad, cilindrada):
		super().__init__(color, ruedas)
		self.velocidad = velocidad
		self.cilindrada = cilindrada

	def setVelocidad(self, nueva_velocidad):
		self.velocidad = nueva_velocidad

	def getVelocidad(self):
		return self.velocidad

	def setCilindrada(self, nueva_cilindrada):
		self.cilindrada = nueva_cilindrada

	def getCilindrada(self):
		return self.cilindrada

	def __str__(self):
		return super().__str__() + f"\nVelocidad: {self.velocidad}\nCilindraje: {self.cilindrada}"

coche1 = Coche("Verde", 4, 5, 120)
camioneta1 = Camioneta("Rojo", 4, 2000)
bicicleta1 = Bicicleta("Negro", 2, "Deportiva")
motocicleta1 = Motocicleta("Blanco", 2, 4, 200)
vehiculos = [coche1, camioneta1, bicicleta1, motocicleta1]

def catalogar(lista, ruedas = None):
	contador = 0
	if ruedas == None:
		for elemento in lista:
			print(f"Nombre de Clase: {type(elemento).__name__}\n{elemento.__str__()}\n---------------------------------------------")
	else:
		for elemento in lista:
			if elemento.getRuedas() == ruedas:
				contador += 1
		print(f"Se han encontrado {contador} vehículos con {ruedas} ruedas.")

catalogar(vehiculos)
catalogar(vehiculos, 4)
catalogar(vehiculos, 2)
catalogar(vehiculos, 0)