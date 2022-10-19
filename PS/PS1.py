# Ejercicio 1

l = [4,3,5,8]


def posicion_minimo(val):
	indice_valor_minimo = l.index(3)
	return (indice_valor_minimo)

print(f'La posicion del valor minimo es {posicion_minimo(l)}.')

# Ejercicio 2

def minimo(val):
	for i in val:
		if i == min(val):
			return(f'{i} es el minimo de esta lista')
		else:
			...

print(minimo(l))