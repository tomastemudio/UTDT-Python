#==================================================================
# 							 CLASE PRACTICA 4
#==================================================================

#------------------------------------------------------------------
#								PS 2
#------------------------------------------------------------------

import numpy as np

# EJERCICIO 1

class OLS:
	def fit(self, X, y):
		xtx = transpuesta(X) * X
		xty = transpuesta(X) * y
		self.coefs_ = np.matmul(np.linalg.inv(txt), txy)

	def predict(self, X):
		return X * self.coefs_

def transpuesta(*args):
	filas = len(X)
	print(filas)
	columnas = len(X[0])
	print(columnas)
	
	matriz_transpuesta = []
	for j in range(columnas):
		fila = []
		for i in range(filas):
			fila.append(X[i][j])
		matriz_transpuesta.append(fila)
	return matriz_transpuesta

X = [[1,2,3],
	 [3,4,5],
	 [5,6,7],
	 [8,9,10],
	 [11,12,13],
	 [14,15,16],
	 [17,18,19],
	 [20,21,22],
	 [23,24,25],
	 [26,27,28]]


def main():
	X = [[1,2,3],
		 [3,4,5],
		 [5,6,7],
		 [8,9,10],
		 [11,12,13],
		 [14,15,16],
		 [17,18,19],
		 [20,21,22],
		 [23,24,25],
		 [26,27,28]]
	y = [[1],
		 [3],
		 [5],
		 [8],
		 [11],
		 [14],
		 [17],
		 [20],
		 [23],
		 [26]]

	ols = OLS()
	ols.fit(X,y)

	X_new = [[3,8,2],
			 [1,5,3]]
	print(ols.predict(X_new))

if __name__ == "__main__":
	main()
