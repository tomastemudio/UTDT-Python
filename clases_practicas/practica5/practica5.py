#==================================================================
# 							 CLASE PRACTICA 5
#==================================================================

from random import random
import requests
from time import sleep
from tqdm import tqdm
import json

results = [] # Lista que acumula los diccionarios con los datos de cada propiedad

endpoint="https://api.mercadolibre.com/sites/MLA/search" ## EN QUE PAGINA TENGO QUE IR A BUSCAR.
params={  												 ## LOS SACAMOS DE LA API DE MELI.
    "category": "MLA1459", # Categoría inmuebles
    "state": "TUxBUENBUGw3M2E1", # Capital Federal
    "OPERATION": 242075 # En venta
}
params["offset"] = 0 # Agregamos el offset inicialmente en 0

ret = None
req = requests.get(endpoint, params) ## EL ENDPOINT ES LA PAGINA DE LA API.
if req.status_code == 200:
    ret = req.json()

# json_object = json.dumps(ret, indent = 4)
# print(json_object)

# if type(ret) == dict:
# 	for k in ret:
# 		print(k) ## Son los key del diccionario ret.

# for k in ret["results"][0]:  ## ESTOY AGARRANDO EL PRIMER ELEMENTO DE UNA LISTA DE DICCIONARIOS. ESTE PRIMER ELEMENTO ES UN DICCIONARIO.
# 	print(k)  ## PARA CADA LUGAR DEL DICCIONARIO IMPRIMIME LA KEY.
	# print(ret["results"][0][k]) ## IMPRIMIR LOS VALORES DEL PRIMER RES.

# Luego de ver los keys de results nos interesan:
## price
## prices
## currency_id
## attributes

# print(ret["results"][0]["attributes"]) ## Es una lista de diccionarios.
json_object = json.dumps(ret["results"][0]["attributes"][0], indent = 4)
# print(json_object)

# for publication in ret["results"][0]["attributes"]:
# 	print(publication["id"]) ## Me tira los values en el key id dentro del attributes.


PRECIOS = []

for publication in range(len(ret['results'])):
	if ret["results"][publication]['currency_id'] == "USD":
		# COMO ACCEDER A LOS METROS CUADRADOS
		for attribute in ret["results"][publication]["attributes"]:
			if attribute["id"] == "COVERED_AREA":
				mts = attribute["value_struct"]["number"]

		# COMO ACCEDER AL PRECIO
		precio = ret["results"][publication]["price"]
		precio_mts = precio / mts

		PRECIOS.append(precio_mts)

	else:
		pass

	# # COMO ACCEDER A LA CURRENCY
	# print(ret['results'][publication]['currency_id'])


print(PRECIOS)
print(sum(PRECIOS)/len(PRECIOS))
