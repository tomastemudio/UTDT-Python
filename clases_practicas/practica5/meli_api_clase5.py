from random import random
import requests
from time import sleep
from tqdm import tqdm
import json

class Scraper:
    def __init__(self, endpoint, params):
        self.results = [] # Lista que acumula los diccionarios con los datos de cada propiedad
        self.endpoint = endpoint
        self.params = params
        self.params["offset"] = 0 # Agregamos el offset inicialmente en 0

    def _get_page(self):
        """
        Request al endpoint. Somos optimistas y no hacemos error handling.
        """
        ret = None
        req = requests.get(self.endpoint, self.params)
        if req.status_code == 200:
            ret = req.json()
        return ret

    def _next_page(self):
        """
        Sólo actualizamos el offset. Usamos el limit default por página que es 50.
        """
        self.params["offset"] += 50

    def get_results(self, n=1000):
        """
        Bajamos los primeros n elementos que nos devuelve la API de MELI.
        """
        with tqdm(total=n) as pbar: # Progress bar para el while. Sólo con fines cosméticos.
            while len(self.results) < n:
                content = self._get_page()
                if content is not None and "results" in content:
                    # No nos interesa todo el json que devuelve la request, sólo lo que está en la lista bajo "results"
                    self.results += content["results"]
                    self._next_page()

                    pbar.update(len(content["results"])) # Update del progress bar
                    sleep(0.35+random()) # Espaciamos requests consecutivas

        # En principios siempre vamos a tener un nro de resultados múltiplo de 50. Si n no es múltiplo de 50,
        # después de la última request nos van a quedar más resultados que los pedidos. Tomo la decisión de
        # dropear los extras (podría, alternativamente, conservarlos)
        self.results = self.results[:n]

def get_area(elem):
    """
    Los resultados tienen una lista de diccionarios bajo la clave "attributes". Uno de esos diccionarios
    contiene el área del inmueble. Esta función busca ese diccionario, accede al área y la devuelve.
    """
    ret = None
    for attr in elem["attributes"]:
        if attr["id"] == "COVERED_AREA":
            ret = attr["value_struct"]["number"]
    return ret

def avg_price_sqmt(results):
    """
    Calcula el precio por metro cuadrado de los inmuebles publicados en USD y devuelve el promedio.
    """
    res = []
    for elem in results:
        if elem["currency_id"] == "USD":
            area = get_area(elem)
            if area is not None and area > 0:
                res.append(elem["price"]/area)
    return sum(res)/len(res)

def main():
    scraper = Scraper(
        endpoint="https://api.mercadolibre.com/sites/MLA/search",
        params={
            "category": "MLA1459", # Categoría inmuebles
            "state": "TUxBUENBUGw3M2E1", # Capital Federal
            "OPERATION": 242075 # En venta
        }
    )
    ret = scraper._get_page()
    print(ret)
    # json_object = json.dumps(ret[0], indent = 4) 
    # print(json_object)
    # scraper.get_results(n=1000)
    # print(avg_price_sqmt(scraper.results))

if __name__ == "__main__":
    main()