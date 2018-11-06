#Gestión de contraseñas
#Problema: Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario la contraseña, y no le permite continuar hasta que la haya ingresado correctamente.
#   También:
#       a) Modificar el programa anterior para que solamente permita una cantidad fija de intentos.
#       b) Modificar el programa anterior para que después de cada intento agregue una pausa cada vez mayor, utilizando la función sleep del módulo time.
#       c) Modificar el programa anterior para que sea una función que devuelva si el usuario ingresó o no la contraseña correctamente, mediante un valor booleano (True o False)

def asignacion():
    contraseña=input("Ingrese la contraseña inventada: ")
    limite=int(input("Ingrese la cantidad máxima de intentos: "))
    return contraseña,limite

def pedir(contraseña,limite):
    intentos=0
    
    ingresado=input("Ingrese la contraseña: ")
    while(ingresado!=contraseña):
        intentos=intentos+1
        if(intentos<limite):
            time.sleep(1*intentos)
            ingresado=input("La contraseña ingresada es incorrecta. Intente nuevamente: ")
        else:
            return False
    
    return True
	
def imprimir(logico):
	if(logico==True):
		print("Correcto. Programa terminado.")
	else:
		print("La contraseña ingresada es incorrecta. Se alcanzó el límite de intentos. Programa terminado.")
		
import time
contraseña,limite=asignacion()
logico=pedir(contraseña,limite)
imprimir(logico)