"""
Crea una clase llamada Cuenta que tendrá los siguientes atributos:
titular (que es una persona) y cantidad (puede tener decimales).
El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:

Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente,
sólo ingresando o retirando dinero.
mostrar(): Muestra los datos de la cuenta.
ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
"""

class Cuenta:
	def __init__(self):
		self.titular = None
		self.cantidad = 0.0

	def set_titular(self, titular):
		self.titular = titular
		print(f"Se ha cambiado el Titular a: {self.titular}")

	def mostrar(self):
		print(f"Nombre del Titular: {self.titular}\nSaldo en cuenta: {self.cantidad}")

	def ingresar(self, cantidad):
		if cantidad > 0:
			self.cantidad += cantidad

	def retirar(self, cantidad):
		self.cantidad -= cantidad

luciano = Cuenta()
luciano.set_titular("Luciano")
luciano.mostrar()
luciano.ingresar(2500)
luciano.retirar(3500)
luciano.mostrar()