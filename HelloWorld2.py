#Import (Estos van siempre al inicio de los modulos)
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("Nombre")
parser.add_argument("Apellido")
args = parser.parse_args()
print(args.Nombre)
print(args.Apellido)

Variable1 = 'Hello'
Variable2 = 1
Variable3 = 2.3

#Concatena
cadena = 'Cadena uno' + 'Cadena dos'


#Interpolacion 
otra_cadena ='Hola {}'.format('un valor')
variable4 = 'Hola{0}{1}'.format(' Mundo',' xd')
var = 'Hola {variable1} {variable2}'.format(variable1 = 'World', variable2 = '!')

def mi_funcion(val):
    print("Dentro de mi Funcion") #Esto es un comentario
    print (otra_cadena)
    print (variable4)
    print (var)

if __name__ == '__main__':
	print ('Hello World')
	mi_funcion(54)
	

#Agrumentos
