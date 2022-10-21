#==================================================================
# 							 CLASE 6
#==================================================================

#------------------------------------------------------------------
# 								PS


#------------------------------------------------------------------
# 							STRINGS
#------------------------------------------------------------------

# Ejercicio 2

def first_letter_uppercase(s):
	l = s.split(' ')
	l_new = []
	for word in l:
		l_new.append(word[0].upper() + word[1:-1] + word[-1].upper())
	return ' '.join(l_new)

#------------------------------------------------------------------
# 							RECURSION
#------------------------------------------------------------------

# Ejercicio 5

def costo_total(canasta):
	ret = 0
	for bien in canasta:
		ret = ret + bien['precio']
	return ret

def utilidad(canasta):
	ret = 0
	for bien in canasta:
		ret = ret + bien['utilidad']
	return ret

def optimize_aux(bienes, M, canasta, i):
	if i == len(bienes):
		ret = canasta
	else:
		if costo_total(canasta) + bienes[i]['precio'] <= M:
			opcion1 = canasta.copy()
			opcion1.append(bienes[i])
			opcion1 = optimize_aux(bienes, M, opcion1, i+1)

			opcion2 = canasta.copy()
			opcion2 = optimize_aux(bienes, M, opcion2, i+1)

			utilidad1 = utilidad(opcion1)
			utilidad2 = utilidad(opcion2)

			if utilidad1 > utilidad2:
				ret = utilidad1
			else:
				ret = utilidad2
		else:
			ret = optimize_aux(bienes, M, canasta.copy(), i+1)
	return ret

def optimize(M, p, u):
	bienes = []
	for i in range(len(p)):
		bienes.append({
			'bien': i, 
			'precio': p[i], 
			'utilidad': u[i]
		}
	)
	return optimize_aux(bienes, M, [], 0)



#------------------------------------------------------------------
def main():
	print('==='*20)
	
	# String.ejercicio2
	s = 'esto es un string de prueba'
	new_s = first_letter_uppercase(s)
	print(new_s)
	print('==='*20)

	# Recursion.ejercicio 5
	M = 10
	p = [2,3,2,5,3,6]
	u = [4,7,2,3,4,8]
	canasta_optima = optimize(M, p, u)
	print(canasta_optima)
	print("Utilidad: ", utilidad(canasta_optima))
	print("Costo total: ", costo_total(canasta_optima))

if __name__ == '__main__':
	main()

