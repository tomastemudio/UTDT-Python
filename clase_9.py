import requests
from bs4 import BeautifulSoup
from time import sleep  ## Pone a dormir el codigo el tiempo que le digas.
from random import random




def main():
	url = "https://listado.mercadolibre.com.ar/departamentos-en-venta-en-capital-federal#D[A:departamentos%20en%20venta%20en%20capital%20federal,L:undefined]"
	# continuar = True      # Para hacerlo para todas las paginas
	for i in range(3): ## VAMOS A HACERLO PARA SOLO 3 PAGINAS
		req = requests.get(url)
		if req.status_code == 200:
			soup = BeautifulSoup(req.content, "lxml")
			resultados = soup.find_all(class_="ui-search-layout__item")
			for resultado in resultados:
				precio = resultado.find(class_="price-tag-text-sr-only")
				print(precio.text)

		next_btn = soup.find(class_="andes-pagination__button--next")
		next_link = next_btn.find("a")  # Me encuentra el primer elemtento con tag a.
		url = next_link["href"]

		sleep(1+random())  ## Hace que no sea muy periodica la request.

		# if url is None:			# Para hacerlo para todas las paginas
		# 	continuar = False

if __name__ == "__main__":
	main()