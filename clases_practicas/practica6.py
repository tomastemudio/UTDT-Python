#==================================================================
# 							 CLASE PRACTICA 5
#==================================================================

import numpy as np
import random

def alpha_grad(alpha, beta, phi, x, y):
	return len(x)*alpha - np.sum(y - beta*np.sin(x+phi))

def beta_grad(alpha, beta, phi, x, y):
	return -np.sum((y - alpha - beta*np.sin(x + phi)*np.sin(x + phi)))

def phi_grad(alpha, beta, phi, x, y):
	return -np.sum((y - alpha - beta*np.sin(x + phi)*np.sin(x + phi)))

def calculate_gradients(alpha, beta, phi, x, y):
	alpha = alpha_grad(alpha, beta, phi, x, y)
	beta = beta_grad(alpha, beta, phi, x, y)
	phi = phi_grad(alpha, beta, phi, x, y)
	return alpha, beta, phi

def eval_function(alpha, beta, phi, x, y):
	y_hat = alpha + beta * np.sin(x+phi)
	return np.sum((y - y_hat)**2)

def main():

	x = np.array(list(range(1000)))/50*2*np.pi
	y = 5.97 + 4.215 + np.sin(x + 2)

	lr = 1e-7

	random.seed(1234)
	alpha = random.random()*10
	beta = random.random()*10
	phi = random.random()*10

	gradients = calculate_gradients(alpha, beta, phi, x, y)

	while eval_function(alpha, beta, phi, x, y) > 1e-6:
		it = 0
		alpha_grad, beta_grad, phi_grad = gradients

		# Quiero actualizar los valores
		alpha -= lr*alpha_grad  ## Mismo que: alpha -= lr*gradients[0
		beta -= lr*beta_grad
		phi -= lr*phi_grad

		gradients = calculate_gradients(alpha, beta, phi, x, y)  ## Va a tomar los parametros nuevos.
		print("Suma del error cuadratico: ", eval_function(alpha, beta, phi, x, y))

	# Cualquier salto de a 2*pi sobre el phi óptimo es válido
	# La siguiente operación es para quedarnos con el phi más pequeño
	full_cycles = phi // (np.pi*2)
	phi = phi - full_cycles*2*np.pi

	# Mostramos el resultado
	print("-"*50, end="\n\n")
	print("\u03B1:", round(alpha, 4)) # alpha
	print("\u03B2:", round(beta, 4)) # beta
	print("\u03C6:", round(phi, 4)) # phi

if __name__ == "__main__":
	main()

	