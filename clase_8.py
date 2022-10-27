#==================================================================
# 							 CLASE 8
#==================================================================

#------------------------------------------------------------------
# 							Paquetes
#------------------------------------------------------------------

import numpy as np

arr2d = np.array([[1,2,3], [4,5,6]])
print(arr2d)
print(arr2d.shape)
print(arr2d[1,2])    ## Me da el 6 de la matriz.

unos_3x2 = np.ones((3,2))
print(unos_3x2)
print('---'*20)
print(unos_3x2[0,:])   ## Se queda con la fila cero y todas sus columnas
print('==='*20)

#------------------------------------------------------------------
# 							Ejercicio escalador
#------------------------------------------------------------------

class Scaler:
	def fit(self, X):
		self.means = X.mean(axis = 0) ## El 'axis = 0' me promedia filas.
		self.std = X.std(axis = 0)

	def transform(self, X):
		return (X - self.means)/self.std

#------------------------------------------------------------------
def main():
	X = np.random.random((10,2))  ## 10 filas y 2 columnas.

	scaler = Scaler()
	scaler.fit(X)
	X_scaled = scaler.transform(X)
	print(X_scaled)
	print('---'*20)
	# ACA HAGO MI REGRESION

	X_new = np.random.random((2,2))
	X_new_scaled = scaler.transform(X_new)
	print(X_new_scaled)

if __name__ == "__main__":
	main()