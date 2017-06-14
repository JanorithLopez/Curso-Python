#""Crear el juego de piedra, papel y tijera
#-Usar while
#-Diccionario
#-Argparse

#- *La app debera solicitar al usuario un valor 'piedra', 'papel' o 'tijera'
#- *La app debera generar un valor aleatorio 'piedra', 'papel' o 'tijera'
#- *La app debera imprimir el resultado de cada mano
#- *La app debera imprimir el ganador entre maquina y usuario (El que gane 3 rondas)
#- *Si es empate, nadie gana puntos y se realiza otra ronda"""

import random

nombre = input('Escribe tu nombre')
print('Bienvenido '+ nombre)
print('*Que empiece el juego*')
aleatorio = random.randrange(0,3)
rock = ('1. Piedra')
paper= ('2. Papel')
sissors= ('3. Tijeras')

print(rock)
print(paper)
print(sissors)
opcion = int(input('Elije una opcion'))

if opcion == 1:
  OpcionUsuario = ('Piedra')
elif opcion == 2:
  OpcionUsuario = ('Papel')
elif opcion == 3:
  OpcionUsuario = ('Tijeras')
print('Has elegido:', OpcionUsuario)

if aleatorio == 1:
  OpcionPc = ('Piedra')
elif opcion == 2:
  OpcionPc = ('Papel')
elif opcion == 3:
  OpcionPc = ('Tijeras')
print('La computadora eligio:', OpcionPc)

while contador < 3:
    if OpcionPc == 'Piedra' and OpcionUsuario == 'Papel'
 print('Ganaste, papel envuelve tijeras')
 GanaUsuario +=1
 PierdePc +=1
elif OpcionPc == 'Piedra' and OpcionUsuario == 'Tijeras'
 print('Perdiste, piedra quiebra a tijeras')
 PierdeUsuario +=1
 GanaPc +=1
elif OpcionPc == 'Papel' and OpcionUsuario == 'Piedra'
 print('Perdiste, papel envuelve piedra')
 PierdeUsuario +=1
 GanaPc +=1
elif OpcionPc == 'Paper' and OpcionUsuario 'Tijeras'
 print ('Ganaste, tijeras corta a papel')
 GanaUsuario +=1
 PierdePc +=1
elif OpcionPc == 'Tijeras' and OpcionUsuario == 'Piedra'
 print('Ganaste, piedra quiebra tijeras')
 GanaUsuario +=1
 PierdePc +=1
elif OpcionPc == 'Tijeras' and OpcionUsuario == 'Papel'
 print('Perdiste, tijeras corta papel')
 PierdeUsuario +=1
 GanaPc +=1
elif OpcionPc == OpcionUsuario
 print ('Empate :v')