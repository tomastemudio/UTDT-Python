# PAGINA PARA APUNTES DE CLASE

## Clases Teoricas

### Clase 7 - 26/10
1. El self nos permite que los atributos de las clases sean accesibles en todas partes.

### Clase 8 - 27/10
1. Un array de una dimension es un vector. Uno de dos dimensiones es una matriz.
2. Un array tiene n dimensiones.
3. Indexar matrices. Por ej tengo matriz de 2x3 y quiero el numero de la segunda columna y primer fila --> Hago `n[0,1]` sabiendo que mi matriz se llama n.
4. `np.argmin(variable)` nos da la posicion donde esta el minimo. Lo mismo para el maximo.
5. Las operaciones con arrays son por default elemento a elemento.

### Clase 9 - 9/11
Clase de data scrapping

### Clase 10 - 10/11
Scraping via **APIs**.


## Clases Practicas

### Clase Practica 3 - 28/10
1. `np.matmul()` sirve para multiplicar matrices.
2. `X.T` para transponer la matriz.
3. `np.linalg` paquete para hacer algebra lineal. `np.linalg.inv()` sirve para hacer la inversa de una matriz.
4. `__init__` lo uso cuando quiero definir atributos.

### Clase Practica 5 - 11/11
```python
dic = {"id":1, "filter": 2}
print(dic)

dic["c"] = [3, 5] # Me agrega esta lista al dic.
dic["results"] = [{"price": 1, "mts": 5}, {"price": 4, "mts": 2}] # Tmb puedo agregar otro diccionario. ESTO ES UNA LISTA.
print(dic)

print(dic["results"][0]) # Me accede al primer diccionario de la lista.
print(dic["results"][0]["results"]) # Me accede al results del primer diccionario de la lista.
```