import numpy as np
from random import randint
from tqdm import tqdm

class Album:
	def __init__(self, n_espacios):
		self.espacios = [False]*n_espacios  ## Lista de False de largo n_espacios.

	def pegar(self, paquete):
		i = 0
		while i < len(paquete):
			if self.espacios[paquete[i]] == False:
				self.espacios[paquete[i]] = True
				del paquete[i]
			else:
				i += 1

	def completo(self):
		# V1
		return sum(self.espacios) == len(self.espacios)

		# V2 
		# ret = True
		# i = 0
		# while i < len(self.espacios) and ret:
		# 	if self.espacios[i] == False:
		# 		ret = False
		# 	i += 1
		# return ret

class Albumes:
	def _init_(self):
		self.albumes = []

	def nuevo_album(self, album):
		self.albumes.append(album)

	def pegar(self, paquete):
		for album in self.albumes:
			album.pegar(paquete)

	def todos_completos(self):     ## Para fijarme si los albumes estan completos.
		ret = True
		i = 0 
		while i < len(self.albumes) and ret:
			if not albumes[i].completo():    ## Ver si el album esta completo.
				ret = False     			 ## Si album no esta completo se corta la iteracion.
			i += 1
		return ret

def abrir_paquete(n_figuritas, n_espacios):
	ret = []
	for i in range(n_figuritas):
		ret.append(randint(0, n_espacios-1))
	return ret


def simular(n_amigos, n_espacios, n_figurtias):
	albumes = Albumes()
	for i in range(n_amigos):
		album = Album(n_espacios)  ## Para cada amigo creo un album nuevo.
		albumes.nuevo_album(album) ## En cada iteracion creo un album nuevo con n espacios.

		paquetes = 0
		while not albumes.todos_completos():
			paquete = abrir_paquete(n_figuritas, n_espacios)
			albumes.pegar(paquete)
			paquetes += 1
		return paquetes // n_amigos


def main():
	n_amigos = 3
	n_espacios = 638
	n_figuritas = 5

	simulaciones = []
	for i in tqdm(range(1000)):
		simulaciones.append(simular(n_amigos, n_espacios, n_figuritas))
	print(np.quantile(simulaciones, 0.9))

if __name__ == "__main__":
	main()