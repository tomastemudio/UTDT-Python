# Ejercicio 1

# l = [4,3,5,8]


# def posicion_minimo(val):
# 	indice_valor_minimo = l.index(3)
# 	return (indice_valor_minimo)

# print(f'La posicion del valor minimo es {posicion_minimo(l)}.')

# # Ejercicio 2

# def minimo(val):
# 	for i in val:
# 		if i == min(val):
# 			return(f'{i} es el minimo de esta lista')
# 		else:
# 			...

# print(minimo(l))


#------------------------------------------------------------------
# 							LISTAS
#------------------------------------------------------------------

## Ejercicio 1

def lista_par(lista):
	lista_nueva = []
	for i in range(len(lista)):
		if i % 2 == 0:
			lista_nueva.append(lista[i])
	return lista_nueva

## Ejercicio 2

def reves_lista(lista):
	reverso =[]
	for elem in range(len(lista)):
		if elem == 0:
			valor = lista.pop(0)
		else:
			reverso.append(lista[-elem])
	reverso.append(valor)
	return reverso

## Ejercicio 4


#------------------------------------------------------------------
def main():
	print('---'*20)
	# Listas.ejercicio1
	lista = [1,2,3,4,5,10,'hola',9,3]
	print(f'La lista de los indices pares es: {lista_par(lista)}')
	print('---'*20)
	
	# Listas.ejercicio2
	print(f'La lista al reves es: {reves_lista(lista)}')
	print('---'*20)

	# Listas.ejercicio3
	print(f'La lista sin elementos repetidos es: {eliminar_repetciciones(lista)}')

if __name__ == '__main__':
	main()