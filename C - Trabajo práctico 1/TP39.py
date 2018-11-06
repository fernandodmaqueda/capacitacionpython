#TP 39
#Problema: TP 39 - Modificar las funciones anteriores, para que reciban un parámetro que indique la cantidad máxima de reemplazos o inserciones a realizar.

def ingreso_a():
	print("Función a) - Inserta el caracter entre cada letra de la cadena. (Ejemplo: 'separar', ',' y '6' debe devolver 's,e,p,a,r,a,r'")
	cadena=input("Ingrese la cadena. (Ejemplo: 'separar'): ")
	caracter=input("Ingrese el caracter. (Ejemplo: ','): ")
	maximo=int(input("Ingrese la cantidad máxima de inserciones a realizar: "))
	str=funcion_a(cadena,caracter,maximo)
	return str

def funcion_a(cadena,caracter,maximo):
	str=cadena=cadena[0] + cadena[1:-1:].replace("",caracter,maximo) + cadena[len(cadena)-1]
	return str

def ingreso_b():
	print("")
	print("Función b) - Reemplaza todos los espacios por el caracter. (Ejemplo: 'mi archivo de texto.txt', '_' y '3' debe devolver 'mi_archivo_de_texto.txt'")
	cadena=input("Ingrese la cadena. (Ejemplo: 'mi archivo de texto.txt'): ")
	caracter=input("Ingrese el caracter. (Ejemplo: '_'): ")
	maximo=int(input("Ingrese la cantidad máxima de reemplazos a realizar: "))
	str=funcion_b(cadena,caracter,maximo)
	return str

def funcion_b(cadena,caracter,maximo):
	str=cadena.replace(" ",caracter,maximo)
	return str

def ingreso_c():
	print("")
	print("Función c) - Reemplaza todos los espacios por el caracter. (Ejemplo: 'su clave es: 1540', 'X' y '4' debe devolver 'su clave es: XXXX'")
	cadena=input("Ingrese la cadena. (Ejemplo: 'su clave es: 1540'): ")
	caracter=input("Ingrese el caracter. (Ejemplo: 'X'): ")
	maximo=int(input("Ingrese la cantidad máxima de reemplazos a realizar: "))
	str=funcion_c(cadena,caracter,maximo)
	return str

def funcion_c(cadena,caracter,maximo):
	cantidad=0
	
	for x in range(len(cadena)):
		if(cantidad<maximo):
			if(cadena[x].isdigit()==True):
				cadena=cadena.replace(cadena[x],caracter,1)
				cantidad=cantidad+1
		else:
			break
	return cadena

def ingreso_d():
	print("")
	print("Función d) - Inserta el caracter cada 3 dígitos en la cadena. (Ejemplo: '2552552550', '.' y '3' debe devolver '255.255.255.0'")
	cadena=input("Ingrese la cadena. (Ejemplo: '2552552550'): ")
	caracter=input("Ingrese el caracter. (Ejemplo: '.'): ")
	maximo=int(input("Ingrese la cantidad máxima de reemplazos a realizar: "))
	str=funcion_d(cadena,caracter,maximo)
	return str
	
def funcion_d(cadena,caracter,maximo):
	cantidad=0
	
	contador=0
	str=""
	for x in cadena:
	
		if(cantidad<maximo):
			if(contador!=0 and contador%3==0):
				str=str+caracter
				cantidad=cantidad+1
		str=str+x
		contador=contador+1
	return(str)

resultado=ingreso_a()
print("Resultado -",resultado)

resultado=ingreso_b()
print("Resultado -",resultado)

resultado=ingreso_c()
print("Resultado -",resultado)

resultado=ingreso_d()
print("Resultado -",resultado)