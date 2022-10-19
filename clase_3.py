#==========================================================================================
#								CLASE 3
#==========================================================================================

# PS 1

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

def minimo(l):
    return l[posicion_minimo(l)]

def minimo2(l):
    candidato = l[0]
    for elem in l:
        if elem < candidato:
            candidato = elem
    return candidato


#--------------------------------------------------------------------------------
def main():
    l = [4, 3, 5, 8]
    pos_min = posicion_minimo(l)
    print(f'El indice del valor minimo es {pos_min}')
    valor = minimo(l)
    print(f'El valor del minimo es {valor}')
    valor2 = minimo2(l)
    print(f'El valor del minimo es {valor2}')

if __name__ == "__main__":
    main()