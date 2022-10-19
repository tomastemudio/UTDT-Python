#=====================================================================================
# 										CLASE 4
#=====================================================================================

# PS1

## Inciso 1

l = [4, 3, 5, 8]

# for i in l:
#     if i == min(l):
#         print(l.index(i))
#     else:
#         ...
	
def posicion_minimo(l):
    candidato = 0
    for i in range(1, len(l)): ## Empiezo desde 1 xq posicion 0 ya es mi candidato,
        if l[candidato] > l[i]:
            candidato = i
    return candidato

## Inciso 2

def minimo(l):
    return l[posicion_minimo(l)]

def minimo2(l):
    candidato = l[0]
    for elem in l:
        if elem < candidato:
            candidato = elem
    return candidato

# Clase de hoy
## Inciso 3

def ordenar(l):
	l_copia = l.copy()
	l_ord = []
	for i in range(len(l_copia)):
		pos_min = posicion_minimo(l_copia)
		l_ord.append(l_copia[pos_min])
		del l_copia[pos_min]
	return l_ord


#--------------------------------------------------------------------------------
def main():
    l = [4, 3, 5, 8]
    pos_min = posicion_minimo(l)
    print(f'El indice del valor minimo es {pos_min}')
    valor = minimo(l)
    print(f'El valor del minimo es {valor}')
    valor2 = minimo2(l)
    print(f'El valor del minimo es {valor2}')
    l_ordenada = ordenar(l)
    print(f'La lista ordenada es {l_ordenada} y la orginal {l}')

if __name__ == "__main__":
    main()

# RECURSION

def suma_hasta(n):
	if n == 0:
		ret = 0
	else:
		ret = n + suma_hasta(n-1)
	return ret

# EJERCICIO MINIMO RECURSIVO
l = [4,3,5,8]

def minimo_rec(l):
    if len(l) == 1:
        ret = l[0]
    else:
        candidato = l[0]
        alternativa = minimo(l[1:])
        if candidato < alternativa:
            ret = candidato
        else:
            ret = alternativa
    return ret

print(f'El minimo recursivo es {minimo_rec(l)}')