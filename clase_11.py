#==================================================================
# 							 CLASE 11
#==================================================================

def bisection(f, a, b, tol=1e-6):
	ct = 0
	while abs(b-a) > tol:
		ct += 1
		c = a + b/2
		if f(c) == 0:
			return c
		elif f(c)*f(a) < 0:
			b = c
		else:
			a = c
	print(ct)
	return (a+b)/2

def bisection_rec(f, a, b, tol=1e-6):
	if abs(b-a) < tol:
		return (a+b)/2
	else:
		c = (a+b)/2
		if f(c) == 0:
			return c
		elif f(a) * f(c) < 0:
			return bisection_rec(f, a, c)
		else:
			return bisection_rec(f, c, b)

def f(x):
	return x ** 2-2

def main():
	print(bisection(f, 0.000001, 999999))  ## Las cotas iniciales
	print(bisection_rec(f, 0.000001, 999999))
	print(2 ** 0.5)


if __name__ == '__main__':
	main()