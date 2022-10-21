#==================================================================
# 							 CLASE PRACTICA 2
#==================================================================

#------------------------------------------------------------------
#							COMBINANDO FUNCIONES
#------------------------------------------------------------------

## Ejercicio 1


from random import randint
import random
import numpy as np
from tqdm import tqdm

def open_pack(n=638, m=5):
	# N cantidad total de figuritas del album.
	# M cantidad total de figuritas por paquete.
	return [randint(0, n-1) for i in range(m)]

def simulate(n_friends, n=638, m=5):

	album = [0] * n

	packs = 0

	while sum(album) < n*n_friends:
		pack = open_pack(n, m)
		packs += 1

		for f in pack:
			if album[f] < n_friends:
				album[f] += 1
	return packs



#------------------------------------------------------------------

def main():
	print('---'*20)
	# Combinando funciones.ejercicio1

	packs_totales = []
	n_friends = 1
	for i in tqdm(range(1000)):
		total_packs = simulate(n_friends)
		per_capita_packs = total_packs // n_friends
		packs_totales.append(per_capita_packs)

	print(packs_totales)
	print('---'*20)
	print(np.mean(packs_totales))

	print(f'Paquetes para completar {str(n_friends)} albumes con prob 0.9 son {int(np.quantile(packs_totales, 0.9))}')

if __name__ == '__main__':
	main()