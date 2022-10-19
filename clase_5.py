#=====================================================================================
# 										CLASE 5
#=====================================================================================


def minimo(l):
	candidato = l[0]
	for elem in l:
		if elem < candidato:
			candidato = elem
		return candidato

def minimo_rec(l):
	if len(l) == 1:
		return l[0]
	else:
		candidato = l[0]
		alternativa = minimo_rec(l[1:])
		if candidato < alternativa:
			return candidato
		else:
			return alternativa


#------------------------------------------------------------------------------------
# 											PS
#------------------------------------------------------------------------------------

# RECURSION

def factorial_iter(n):
	i = 1
	factorial = 1
	while i <= n:
		factorial = factorial * i
		i += 1
	return factorial

def factorial_iter_alternativo(n):
	ret = 1
	for i in range(n):
		ret = ret * (i+1)
	return ret

def factorial_rec(n):
	if n == 0:
		ret = 1
	else:
		ret = n * factorial_rec(n-1)
	return ret

def suma_lista(l):
	if len(l) == 0:
		ret = -1
	else:
		if len(l) == 1:
			ret = l[0]
		else:
			ret = [0] + suma_lista(l[1:])
	return ret

# STRINGS

def capicua(string):
	l = list(string)
	ret = True
	while len(l) > 1 and ret:
		if l[0] != l[len(l)-1]:
			ret = False
		del l[0]
		del l[len(l)-1]
	return ret

def capicua_alt(string):
	ret = True
	for i in range(len(string)//2):
		if string[i] != string[len(string)-1-i]:
			ret = False
	return ret



def main():
	n = 5
	string = input('Ingrese una palabra: ')
	print(f'Factorial iterativo: {factorial_iter(n)}')
	print(f'Factorial iterativo alternativo: {factorial_iter_alternativo(n)}')
	print(f'Factorial recursivo: {factorial_rec(n)}')
	# print(f'Suma lista: {suma_lista(l)}')
	print(f'Es capicua? {capicua(string)}')
	print(f'Es capicua? {capicua_alt(string)}. Esta es la forma alternativa')


if __name__ == '__main__':
	main()