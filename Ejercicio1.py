def datos():
    nombres = {
        'Nombre': 'Maria'
    }
    return nombres

def pedir_nombre():
    nombre = raw_input('Ingrese un nombre: ')
    diccionario_prueba = datos()
    if nombre in diccionario_prueba:
        print('la llave existe')
    else:
        print('la llave no existe')

if __name__ == '__main__':
    
    pedir_nombre()


    
    