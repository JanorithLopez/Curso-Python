# Crear una app que reciba el nombre y edad de un usuario
# 1. Impeimir el ano en el que ese usuario va a cumplir 100 anos


if __name__ == '__main__':
    Nombre = input("Ingrese su nombre: ")
    Edad = int(input("Ingrese su edad: "))
    Anio= int(input("Ingrese el anio actual: "))
    Cien = "cumplira 100 anios en el: "
    print(Nombre, Cien,(100 - Edad)+ Anio)
