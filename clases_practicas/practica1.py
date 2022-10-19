#=====================================================================================
# 								CLASE PRACTICA 1
#=====================================================================================
import sys

#-------------------------------------------------------------------------------------
#								LISTAS
#-------------------------------------------------------------------------------------

# EJERCICIO 3

l = [3,2,1,3,4,2]


def eliminar_repeticiones(l):
	i = 0
	while i < len(l):
		if l[i] in l[i+1:]:
			del l[i]
		else:
			i += 1



#-------------------------------------------------------------------------------------
#								STRINGS
#-------------------------------------------------------------------------------------

# EJERCICIO 3

def get_filename(path):
	return path.split('/')[-2]

# EJERCICIO 4

def count_chars(s):
	counts = {}
	for char in s:
		if char in counts:
			counts[char] += 1
		else:
			counts[char] = 1
	
	for k, v in counts.items():
		print(k,v)

#-------------------------------------------------------------------------------------
#								RECURSION
#-------------------------------------------------------------------------------------

def potencia(n,k):
	resultado = 1
	if k >= 1 & (k % 1 == 0):
		resultado = n
		if k > 1:
			resultado = n * potencia(n, k-1)
		return resultado
	else:
		sys.exit('Pone bien el k')
		return


#-------------------------------------------------------------------------------------
def main():
	l = [1,2,3,1,4,5,2,4,2,2]
	eliminar_repeticiones(l)
	# print(l)

	# s = "/Users/tomastemudio/Desktop/UTDT_python/clases_practicas/practica1.py/"
	# name = get_filename(s)
	# # print(name)

	# s = 'ozono'
	# print('Ocurrencias de los caracteres en "ozono"')
	# count_chars(s)

	numeros = potencia(5,2)
	print(numeros)
	


if __name__ == '__main__':
	main()