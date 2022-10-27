#==================================================================
# 							 CLASE 6
#==================================================================

class Estudiante:
	def __init__(self, nombre, legajo, notas={}):
		self.nombre = nombre
		self.legajo = legajo
		self.notas = notas

	def agregar_nota(self, materia, nota): ## No devuevle nada solo modifica el dicc notas.
		self.notas[materia] = nota

	def mostrar_nombre(self):
		print(self.nombre)

	def promedio(self):
		ret = 0
		# V1
		for nota in self.notas.values():
			ret += nota
		return ret / len(self.notas)

		#V2
		num = 0
		denom = 0
		for nota in self.notas.values():
			num += nota
			denom += 1
		return num / denom


#------------------------------------------------------------------
def main():
	estudiante1 = Estudiante("Juana", "20T1233")
	estudiante1.mostrar_nombre()
	estudiante1.agregar_nota("Lab", 10)
	estudiante1.agregar_nota("OI", 8)
	print(estudiante1.promedio())

	estudiante2 = Estudiante("Pedro", "21J1233")
	estudiante2.mostrar_nombre()
	estudiante2.agregar_nota("Lab", 10)
	estudiante2.agregar_nota("OI", 5)
	print(estudiante2.promedio())

if __name__ == "__main__":
	main()