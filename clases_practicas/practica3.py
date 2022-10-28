#==================================================================
# 							 CLASE PRACTICA 3
#==================================================================

#------------------------------------------------------------------
#								PS 2
#------------------------------------------------------------------

# EJERCICIO 1

import numpy as np

class OLS:

	def fit(self, X, y):
		xtx = np.matmul(X.T, X)
		xty = np.matmul(X.T, y)
		self.coefs_ = np.matmul(np.linalg.inv(xtx), xty)

	def predict(self, X):
		return np.matmul(X, self.coefs_)

# Ejercicio 2

class OOLS:

	def __init__(self, X, y):
		self.xtx = self._calculate_xtx(X)
		self.xty = self._calculate_xty(X, y)
		self.coefs_ = None 

	def _calculate_xtx(self, X):
		xtx = np.matmul(X.T, X)
		return xtx

	def _calculate_xty(self, X, y):
		xty = np.matmul(X.T, y)
		return xty

	def add(self, X_new, y_new):          ## Necesito guardarme el xtx & xty
		self.xtx += self._calculate_xtx(X_new)
		self.xty += self._calculate_xty(X_new, y_new)

	def fit(self):
		self.coefs_ = np.matmul(np.linalg.inv(self.xtx), self.xty)

	def predict(self, XX):
		return np.matmul(XX, self.coefs_)


#------------------------------------------------------------------
def main():
	# PS.Ejercicio1

	# X = np.random.random((10,3))
	# y = np.random.random((10,1))

	# model1 = OLS()
	# model1.fit(X, y)
	# print(model1.coefs_)

	# # Predecir
	# x = np.random.random((1,3))
	# print(ols.predict(X))

	# PS.Ejercicio 2

	X0 = np.random.random((10,3))
	y0 = np.random.random((10,1))
	
	model2 = OOLS(X0, y0)
	model2.fit()
	print(f'El beta estimado es: {model2.coefs_}')

	X1 = np.random.random((3,3))
	y1 = np.random.random((3,1))
	model2.add(X1, y1)
	model2.fit()
	print(f'El beta actualizado es: {model2.coefs_}')

if __name__ == "__main__":
	main()