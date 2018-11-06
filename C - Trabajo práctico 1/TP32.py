#TP32
#Problema: TP32 - Escribí funciones que dada una cadena de caracteres:
#   a) Imprima los dos primeros caracteres.
#   b) Imprima los tres últimos caracteres.
#   c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'
#   d) Dicha cadena en sentido inverso. Ej.: 'hola mundo!’ debe imprimir '!odnum aloh’
#   e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime 'reflejoojelfer.

def funcion_a(str):
    print("Punto a) - Imprimir los dos primeros caracteres:",str[0:2])
	
def funcion_b(str):
    print("Punto b) - Imprimir los tres últimos caracteres:",str[len(str)-3:len(str)])
	
def funcion_c(str):
    print("Punto c) - Imprimir dicha cadena cada dos caracteres. (Ejemplo: 'recta' debería imprimir 'rca'):",str[::2])

def funcion_d(str):
    print("Punto d) - Imprimir dicha cadena en sentido inverso. (Ejemplo: 'hola mundo!' debe imprimir '!odnum aloh'):",str[len(str)::-1])

def funcion_e(str):
    print("Punto e) - Imprimir la cadena en un sentido y en sentido inverso. (Ejemplo: 'reflejo' imprime 'reflejoojelfer'):",str+str[len(str)::-1])

cadena=input("Ingrese una cadena de caracteres. (Ejemplos: 'recta', 'hola mundo!', 'reflejo'): ")

funcion_a(cadena)
funcion_b(cadena)
funcion_c(cadena)
funcion_d(cadena)
funcion_e(cadena)