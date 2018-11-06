#TP 46
#Problema: TP 46 - Dominó: Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son recibidas en dos lupias, por ejemplo: (3,4) y (5,4)

def carga():
	#Carga en cadenas
	cadena1=input("Ingrese la ficha 1. (Formato: 3,4): ")
	cadena2=input("Ingrese la ficha 2. (Formato: 5,4): ")

	#Separa las cadenas
	tupla1=cadena1.split(",")
	tupla2=cadena2.split(",")

	#Retorna en tuplas
	return tupla1,tupla2

def encajan(ficha1, ficha2):
	#Prueba cada posicion de la ficha 1 y si uno de esos valores es igual a alguna posición de la ficha 2 determina que encajan
	for posicion in ficha1:
		if posicion==ficha2[0] or posicion==ficha2[1]:
			return True
	return False

def imprimir(logico):
	if(logico==True):
		print("Las fichas de dominó encajan")
	else:
		print("Las fichas de dominó NO encajan")

ficha1,ficha2=carga()
logico=encajan(ficha1,ficha2)
imprimir(logico)
