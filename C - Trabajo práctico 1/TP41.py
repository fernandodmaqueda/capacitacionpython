#TP 41
#Problema: TP 41 - Escribí una función que reciba una cadena que contiene un largo número entero y devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe '1234567890’, debe devolver '1.234.567.890'.

def funcion(cadena):
    str=""
    contador=1
    for caracter in cadena[::-1]:
        str=caracter+str
        if(contador%3==0):
            str="."+str
        contador=contador+1
    return str

cadena=input("Ingrese un largo número entero. (Ejemplo: 1234567890): ")

resultado=funcion(cadena)
print("Resultado - El número con las separaciones de miles: %s" %(resultado))