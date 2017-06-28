
class Mascota(object):

	def __init__(self, edad):
		self.edad = edad

	def obt_edad(self):
		return 'La edad de las mascotas es: ' + self.edad

class Perro(Mascota):

	def __init__(self, nombreP, edad):
		super(Perro, self).__init__(edad)
		self.nombreP = nombreP

	def obtener_nombre_perro(self):
		return 'El nombre del perro es: ' + self.nombreP

class Gato(Mascota):

	def __init__(self, nombreG, edad):
		super(Gato, self).__init__(edad)
		self.nombreG = nombreG

	def obtener_nombre_gato(self):
		return 'El nombre del perro es: ' + self.nombreG

if __name__ == '__main__':
	dog = Perro('Yogui', '18')
	cat = Gato('Mickey', '18')
	print dog.obt_edad()
	print dog.obtener_nombre_perro()
	print cat.obtener_nombre_gato()