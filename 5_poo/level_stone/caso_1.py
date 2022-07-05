class Vehiculo:
	def __init__(self, color, ruedas):
		self.color = color
		self.ruedas = ruedas

	def setColor(self, nuevo_color):
		self.color = nuevo_color

	def getColor(self):
		return self.color

	def setRuedas(self, nueva_ruedas):
		self.ruedas = nueva_ruedas

	def getRuedas(self):
		return self.ruedas

	def __str__(self):
		return f"Color: {self.color}\nRuedas: {self.ruedas}"

class Coche(Vehiculo):
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

coche1 = Coche("Rojo", 4, 300, 5)
print(coche1)
coche1.setVelocidad(240)
coche1.setColor("Verde")
coche1.setCilindrada(6)
coche1.setRuedas(5)
print(coche1)