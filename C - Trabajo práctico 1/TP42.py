#TP 42
#Problema: TP 42 - Escribí una función que dada una cadena de caracteres, devuelva:
#   a) La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe devolver 'USB'.
#   b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe 'república argentina' debe devolver 'República Argentina'.
#   c) Las palabras que comiencen con la letra 'A'. Por ejemplo, si recibe 'Antes de ayer' debe devolver 'Antes ayer'

def funcion(cadena):
    lista=[]
    temp=cadena.split(" ")

    str_a=""
    for palabra in temp:
        str_a=str_a+(palabra[0])
    lista.append(str_a)

    str_b=""
    for palabra in temp:
        if(str_b==""):
            str_b=palabra.capitalize()
        else:
            str_b=str_b + " " + palabra.capitalize()
    lista.append(str_b)

    str_c=""
    for palabra in temp:
        if(palabra.startswith("A") or palabra.startswith("a")):
            if(str_c==""):
                str_c=palabra
            else:
                str_c=str_c + " " + palabra
    lista.append(str_c)
    return lista

cadena=input("Ingrese una cadena de caracteres. (Ejemplos: Universal Serial Bus, república argentina, Antes de ayer): ")

lista=funcion(cadena)
print("Punto a) - La primera letra de cada palabra:",lista[0])
print("Punto b) - La primera letra de cada palabra en mayúsculas:",lista[1])
print("Punto c) - Las palabras que comiencen con la letra 'A':",lista[2])