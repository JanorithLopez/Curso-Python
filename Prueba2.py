# Crear una app que reciba el nombre y edad de un usuario
# 1. Impeimir el ano en el que ese usuario va a cumplir 100 anos


if __name__ == '__main__':
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    anio = int(input("Ingrese el anio actual: "))

    cien = "{nombre} cumplira 100 anios en el: {anio_calculado}"
    anio_calculado = (100 - edad) + anio

    mensaje = cien.format(nombre=nombre, anio_calculado=anio_calculado)
    print(mensaje)
