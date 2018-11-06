#TP 44
#Problema: TP 44 - Cartas y tuplas:
#	a) Proponer una representación con tupias para las cartas de póker (francesas).
#	b) Escribir una función póker que reciba cinco cartas de la baraja francesa e informe (devuelva el valor lógico correspondiente) si esas cartas forman o no un póker (es decir que hay 4 cartas con el mismo número).

#Representación de una carta de la baraja francesa con tupla: (valor,palo)

def ingreso():
	cartas=[]
	for x in range(5):
		valor=input("Carta %d/5: Ingrese el valor (A-2-3-4-5-6-7-8-9-10-J-Q-K): " %(1+x))
		while(valor!="A" and valor!="2" and valor!="3" and valor!="4" and valor!="5" and valor!="6" and valor!="7" and valor!="8" and valor!="9" and valor!="10" and valor!="J" and valor!="Q" and valor!="K"):
			valor=input("Error. Carta %d/5: Ingrese el valor (A-2-3-4-5-6-7-8-9-10-J-Q-K): " %(1+x))
		
		palo=input("Carta %d/5: Ingrese el palo (Corazones, Diamantes, Tréboles, Picas) [C-D-T-P]: " %(1+x))
		while(palo!="C" and palo!="D" and palo!="T" and palo!="P"):
			palo=input("Error. Carta %d/5: Ingrese el palo (Corazones, Diamantes, Tréboles, Picas) [C-D-T-P]: " %(1+x))
		
		cartas.append((valor,palo))
	print("Cartas ingresadas:",cartas)
	return cartas

def poker(cartas):
	iguales=0
	siguiente=0

	for j in range(5):
		valor=cartas[j][0]
		for i in range(siguiente,5):
			if(valor==cartas[i][0]):
			   iguales+=1
		if(iguales>=4):
			return True
		iguales=0
		siguiente+=1
	
	#Si aún no se cumplió la condición para 'return True', es porque no hay póker:
	return False

def imprimir(logico):
	if(logico==True):
		print("Las cartas forman un póker (4 cartas con el mismo valor)")
	else:
		print("Las cartas NO forman un póker (no hay 4 cartas con el mismo valor)")

cartas=ingreso()
logico=poker(cartas)
imprimir(logico)