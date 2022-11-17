#==================================================================
# 							 CLASE 12
#==================================================================
import numpy as np
import matplotlib.pyplot as plt

def newton(f, df, x0, tol=1e-6):
	x = x0
	ct = 0
	while abs(f(x)) > tol:
		x = x - f(x)/df(x)
		ct += 1
	print(ct)
	return x

def newton_rec(f, df, x0, tol=1e-6):
	if abs(f(x0)) < tol:  			## Esto es si ya encontre la raiz.
		return x0
	else:
		x = x0 - f(x0)/df(x0)
		return newton_rec(f, df, x)

def f(x):
	return x ** 2-2

def df(x):
	return 2 * x

# DESCENSO DE GRADIENTE

def gd(f, df, x0, lr, tol=1e-6):		  # El learnig rate(lr) es menor que uno.
	x_plot = np.linspace(0, 4, 500)       # Vector lineal.
	y_plot = [f(x) for x in x_plot]
	plt.plot(x_plot, y_plot, color='black')

	x = x0 
	while abs(df(x)) > tol:
		x = x - lr * df(x)  ## Regla de actualizacion.

		plt.scatter(x, f(x), color='red')
		plt.pause(0.3)
	plt.show()
	return x

def gd_rec(f, df, x0, lr, tol=1e-6):
	if abs(df(x0)) < tol:
		return x0
	else:
		x = x0 - lr*df(x0)
		return gd_rec(f, df, x, lr)


def f(x):
	return (x - 2) ** 2 + 1

def df(x):
	return 2 * (x - 2)

def main():
	print(newton(f, df, 999999))
	print(newton_rec(f, df, 999999))
	print(2 ** 0.5)

	# Descenso de gradiente
	print(gd(f, df, 3.5, 0.1))
	print(gd_rec(f, df, 3.5, 0.1))

if __name__ == "__main__":
	main()