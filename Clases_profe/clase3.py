# Intro: Ejercicio 1
def posicion_minimo(l):
	"""
	Inicialmente asuminos que el elemento en la posición 0 de la lista
	es el mínimo (nuestro candidato inicial), y luego recorremos las
	demás posiciones actualizando nuestra posición candidata en caso
	de ir encontrando el mínimo en otro lugar de la lista.
	"""
	candidato = 0
	for i in range(1, len(l)):
		if l[candidato] > l[i]:
			candidato = i
	return candidato


# Intro: Ejercicio 2 (alternativa 1)
def minimo(l):
	return l[posicion_minimo(l)]


# Intro: Ejercicio 2 (alternativa 2)
def minimo_alt(l):
	"""
	Mismo criterio que en la función posicion_minimo, pero ahora
	recorremos directamente los elementos de la lista en lugar
	de tener que estar indexando por las distintas posiciones.
	"""
	candidato = l[0]
	for elem in l[1:]:
		if elem < candidato:
			candidato = elem
	return candidato


def main():
	l = [4, 3, 5, 8]
	print("Posición del mínimo:", posicion_minimo(l))

	print("Valor mínimo (con la alternativa 1):", minimo(l))
	print("Valor mínimo (con la alternativa 2):", minimo_alt(l))


if __name__ == "__main__":
	main()