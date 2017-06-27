import random

NOMBRES = [
    'Ana',
    'Pedro',
    'Pablo',
    'Ernesto',
    'Ariel',
    'Carlos',
    'Luis',
    'Oscar',
    'Alicia',
    'Maria',
    'Brenda'
]

CIUDADES = [
    'Managua',
    'Masaya',
    'Matagalpa',
    'Chinandega',
    'Somoto',
    'Rivas'
]


def generar_diccionario_estudiantes():
    estudiantes = {}

    for nombre in NOMBRES:
        estudiantes[nombre] = {
            'edad': random.randrange(16, 30),
            'anio': random.randrange(1, 5),
            'cuidad': random.choice(CIUDADES)
        }

    return estudiantes

def imprimir():
    doc = open('Imprimir.txt', 'w')
    diccionario = generar_diccionario_estudiantes()
    for key, value in diccionario.iteritems():
        letras = 'El estudiante {nombre} de {edad} anios, es de la ciudad de {ciudad} y cursa el {anio} anio en la universidad \n'.format(nombre = key, edad = value['edad'], ciudad = value['cuidad'], anio = value['anio'])
        doc.write(letras)
        print '---' letras
    doc.close()

def imprimir_managua():
    doc = open('Imprimir_Managua.txt', 'w')
    diccionario = generar_diccionario_estudiantes()
    for key, value in diccionario.iteritems():
        if 'Managua' == value['cuidad']:
            letras = 'El estudiante {nombre} de {edad} anios, es de la ciudad de {ciudad} y cursa el {anio} anio en la universidad \n'.format(nombre = key, edad = value['edad'], ciudad = value['cuidad'], anio = value['anio'])
            doc.write(letras)
            print '---' letras
    doc.close()

def imprimir_masaya():
    diccionario = generar_diccionario_estudiantes()
    for key, value in diccionario.iteritems():
        if 'Masaya' == value['cuidad']:
            letras = 'El estudiante {nombre} de {edad} anios, es de la ciudad de {ciudad} y cursa el {anio} anio en la universidad \n'.format(nombre = key, edad = value['edad'], ciudad = value['cuidad'], anio = value['anio'])
            doc.write(letras)
            print '---' letras
    doc.close()

def imprimir_menores():
    diccionario = generar_diccionario_estudiantes()
    for key, value in diccionario.iteritems():
        if value['edad'] < 21:
            letras = 'El estudiante {nombre} de {edad} anios, es de la ciudad de {ciudad} y cursa el {anio} anio en la universidad \n'.format(nombre = key, edad = value['edad'], ciudad = value['cuidad'], anio = value['anio'])
            doc.write(letras)
            print '---' letras
    doc.close()

if __name__ == '__main__':
    imprimir()
    print 'ESTUDIANTES DE MANAGUA'   
    imprimir_managua()
    print 'ESTUDIANTES DE MASAYA'
    imprimir_masaya()
    print 'ESTUDIANTES MENORES DE 21'
    imprimir_menores()