# crear una app que reciba el nombre y edad de un usuario
# 1. Impeimir el ano en el que ese usuario va a cumplir 100 anos 

Nombre = input("Ingrese su nombre: ")
Edad = int(input("Ingrese su edad: "))
Anio= int(input("Ingrese el anio actual: "))
Cien = "cumplira 100 anios en el: "


if __name__ == '__main__':
	print(Nombre, Cien,(100 - Edad)+ Anio)

#repl.it