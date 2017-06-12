# Dado el texto "esto es una prueba" imprimir una cadena formateada de la siguiente manera

#argumento <nombre>

#esto es una prueba <nombre>

# 1. Imprimir cuantas letras "E" tiene la cadena
# 2. Capitalizar la cadena
# 3. Imprimir longitud de la cadena
# 4. Reemplazar en la cadena la letra "o" por 0

Texto = 'esto es una cadena'

if __name__ == '__main__':
	print(Texto)
	print(str.count(Texto,'e'))
	print(str.capitalize(Texto))
	print(len(Texto))
	print(str.replace(Texto,'o','0'))