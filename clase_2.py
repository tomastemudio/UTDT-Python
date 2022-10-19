# # ================================================================================================
# #											CLASE 2
# # ================================================================================================

# l = [1,2,3]
# l.append(4)

# l.insert(2,10)

# elem = l.pop()

# # ======================================================================

# # FUNCIONES

# def es_par(val):
# 	ret = False
# 	if val % 2 == 0:
# 		ret = True
# 	return ret

# print(es_par(4))
# print(es_par(1))

# def funcion_dummy(b,a):
# 	return b ** a

# a=3
# b=2

# funcion_dummy(a,b)

# # ======================================================================

# # OBJETOS MUTABLES

# ## Para copiar lista utilizo el .copy().

# lista1 = [1,2,3,4,5]
# lista1
# lista2 = lista1.copy()
# lista2

# # ======================================================================

# # ITERACION

# mi_lista= []

# for i in range(1,11):
# 	mi_lista.append(i+1)

# print(mi_lista)

def es_par(val):
	ret = True
	if val % 2 != 0:
		ret = False
	return ret

def todos_pares(l):
	ret = True
	i = 0
	while i < len(l) and ret:
		if not es_par(l[i]):
			ret = False
		i += 1
	return ret

# ======================================================================
#					ACORDARSE DE ESTO
# ======================================================================

# def ...():
# 	...

# def main():
# 	...

# if __name__ == "__main__":
# 	main()
# ======================================================================
# ======================================================================

def main():
	l = [4,4,6,8,3,2,5,6,6]
	son_todos_pares = todos_pares(l)
	print(son_todos_pares)

if __name__ == "__main__":
	main()


