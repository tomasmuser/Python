"""
Cargar por teclado un texto completo en una variable de tipo cadena de caracteres.*

El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final del texto. *
Cada palabra de ese texto está separada de las demás por un espacio en blanco.*
---------             ---------           ---------              ---------           ---------         ---------
Determinar la cantidad de palabras que no tenían ninguna vocal.*
El promedio de consonantes por palabra en todo el texto.*
Determinar cuántas palabras tenían una "p" o una "r", y al mismo tiempo comenzaban con la letra "a".*
Determinar la cantidad de palabras que incluyeron la expresión “ar” pero de forma que comience después de la segunda letra de esas palabras.
"""


def cadena_frmt_palabras(cad):
    lista_palabras = []
    palabra = ""
    for i in cad:
        if i in cadena_consonantes or i in cadena_vocales or i in cadena_numeros:
            palabra += i
        elif i == " " or i == ".":
            lista_palabras.append(palabra)
            palabra = ""
    return lista_palabras


def vocal_nulo(lista_palabras):
    sin_vocal = 0
    vocal = False
    for palabra in lista_palabras:
        for i in palabra:
            if i in cadena_vocales:
                vocal = True
                break
        if vocal == False:
            sin_vocal += 1
        vocal = False

    return sin_vocal


def cons_prom(cad, lista_palabras):
    num_consonantes = 0
    for i in cad:
        if i in cadena_consonantes:
            num_consonantes += 1
    prom_consonantes = int(100/(num_consonantes/len(lista_palabras)))
    return prom_consonantes


def analisis_pra(lista_palabras):
    palabra_par = 0
    for palabra in lista_palabras:
        if palabra[0] == "a" or palabra[0] == "A":
            for i in range((len(palabra))):
                if palabra[i] == "p" or palabra[i] == "r" or palabra[i] == "P" or palabra[i] == "R":
                    if i > 0:
                        palabra_par += 1
                        break
    return palabra_par


def analisis_ar(lista_palabras):
    palabra_2ar = 0
    for palabra in lista_palabras:
        for i in range(len(palabra)-1):
            if (i+1) > len(palabra):
                break
            elif palabra[i] == "a" and palabra[i+1] == "r":
                if i > 1:
                    palabra_2ar += 1
    return palabra_2ar


def cadena_frmt():
    cad_final = ""
    cad_princ = str(input("Ingrese un texto.\n(El programa tomara como fin el primer punto que encuentre descartando el resto, ademas el sistema rechaza cualquier caracter especial.)\n-"))
    for i in cad_princ:
        cad_final += i
        if i == ".":
            return cad_final
    print("Fin de cadena no encontrado....")
    print("Añadiendo fin a cadena...")
    cad_final += "."
    return cad_final


cadena_vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
cadena_consonantes = "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
cadena_numeros = "1234567890"
cadena_principal = cadena_frmt()
print("\"", cadena_principal, "\"")
lista_palabras = cadena_frmt_palabras(cadena_principal)

sin_vocal = vocal_nulo(lista_palabras)
print("El numero de palabras que no tenían ninguna vocal es de: ", sin_vocal)
prom_consonantes = cons_prom(cadena_principal, lista_palabras)
print("El promedio de consonantes por palabra en todo el texto es: ", prom_consonantes, "%", sep='')
palabra_par = analisis_pra(lista_palabras)
print("El numero de palabras tenían una \"p\" o una \"r\", y al mismo tiempo comenzaban con la letra \"a\" es de: ", palabra_par)
palabra_2ar = analisis_ar(lista_palabras)
print("El numero de palabras que incluyeron la expresión “ar” pero de forma que comience después de la segunda letra de esas palabras: ", palabra_2ar)