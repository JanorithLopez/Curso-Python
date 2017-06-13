import random
# 1. Crear 20 numeros aleatorios entre el 0 y el 100
# Imprimir una lista de los numeros generados, ordenados ascendente
# Primero los pares y luego los impares
# Ejemplo si los numeros generados son [4,3,5,6,2]
# El resultao seria [2,4,6,3,5]

A = [ ]
B = [ ]
C = [ ]

for i in range(20):
	A.append(random.randint(0,100))
	
	if ((A[i]%2)==0):
		B[i] = A[0:]

    else if ((A[i]%2)!=0):
    	C[i] = A[0:]

print(A)
print(B.sort()+C.sort())