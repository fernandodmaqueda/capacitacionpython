#TP34
#Problema: TP34 - Escribí funciones que dada una cadena y un carácter:
#	a) Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y debería devolver ’s,e,p,a,r,a,r'
#	b) Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_' debería devolver ‘mi_archivo_de_texto.txt'
#	c) Reemplace todos los dígitos en la cadena por el caracter. Ej: 'su clave es: 1540' y 'X' debería devolver 'su clave es: XXXX'
#	d) Inserte el caracter cada 3 dígitos en la cadena Ej. '2552552550' y '.' debería devolver '255.255.255.0'

def ingreso_a():
	print("Función a) - Inserta el caracter entre cada letra de la cadena. (Ejemplo: 'separar' y ',' debe devolver 's,e,p,a,r,a,r'")
	cadena=input("Ingrese la cadena. (Ejemplo: 'separar'): ")
	caracter=input("Ingrese el caracter. (Ejemplo: ','): ")
	str=funcion_a(cadena,caracter)
	return str

def funcion_a(cadena,caracter):
	cadena=cadena=cadena[0] + cadena[1:-1:].replace("",caracter) + cadena[len(cadena)-1]
	return cadena

def ingreso_b():
	print("")
	print("Función b) - Reemplaza todos los espacios por el caracter. (Ejemplo: 'mi archivo de texto.txt' y '_' debe devolver 'mi_archivo_de_texto.txt'")
	cadena=input("Ingrese la cadena. (Ejemplo: 'mi archivo de texto.txt'): ")
	caracter=input("Ingrese el caracter. (Ejemplo: '_'): ")
	str=funcion_b(cadena,caracter)
	return str

def funcion_b(cadena,caracter):
	cadena=cadena.replace(" ",caracter)
	return cadena

def ingreso_c():
	print("")
	print("Función c) - Reemplaza todos los espacios por el caracter. (Ejemplo: 'su clave es: 1540' y 'X' debe devolver 'su clave es: XXXX'")
	cadena=input("Ingrese la cadena. (Ejemplo: 'su clave es: 1540'): ")
	caracter=input("Ingrese el caracter. (Ejemplo: 'X'): ")
	str=funcion_c(cadena,caracter)
	return str

def funcion_c(cadena,caracter):
	for x in range(len(cadena)):
		if(cadena[x].isdigit()==True):
			cadena=cadena.replace(cadena[x],caracter,1)
	return cadena

def ingreso_d():
	print("")
	print("Función d) - Inserta el caracter cada 3 dígitos en la cadena. (Ejemplo: '2552552550' y '.' debe devolver '255.255.255.0'")
	cadena=input("Ingrese la cadena. (Ejemplo: '2552552550'): ")
	caracter=input("Ingrese el caracter. (Ejemplo: '.'): ")
	str=funcion_d(cadena,caracter)
	return str

def funcion_d(cadena,caracter):
	contador=0
	str=""
	for x in cadena:
	 if contador!=0 and contador%3==0:
		 str=str+caracter
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