#!/usr/bin/env python
# -*- coding:utf-8 -*-

import mkncion
import os


def opcion_1(file_bin):  # Reproducciones por idioma/genero.
    vector = mkncion.leer_file(file_bin)
    matriz = [[0] * 4 for f in range(10)]
    for cancion in vector:
        matriz[cancion.genero][cancion.idioma] += cancion.rep
    muestra_matriz(matriz)


def muestra_matriz(matriz):  # Muestra matriz idioma/genero.
    for i in range(len(matriz)):
        print("\nGenero {0}:".format(mkncion.genero_lst[i]))
        for j in range(len(matriz[i])):
            print("Idioma {0}:".format(mkncion.idioma_lst[j]), matriz[i][j])


def opcion_2(file_bin):
    vector = mkncion.leer_file(file_bin)
    mkncion.muestra(vector)


def opcion_3(file_bin):
    t = str(input("Ingrese el titulo de la cancion a buscar: "))
    vector = mkncion.leer_file(file_bin)
    vector = busqueda_titulo(vector, t)
#   mkncion.crear_file(vector, file_bin)


def busqueda_titulo(vector, t):
    n = len(vector)
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if vector[c].titulo.lower() == t.lower():
            rep_pasado = vector[c].rep
            vector[c].rep += 1
            print("Reproducciones de \"{0}\" incrementadas de {1} a {2}.".format(vector[c].titulo.title(), rep_pasado,
                                                                                 vector[c].rep))
            return vector
        if t.lower() < vector[c].titulo.lower():
            der = c - 1
        else:
            izq = c + 1
    print("No se encontro la cancion de titulo \"{0}\".".format(t.title()))


def opcion_4(file_bin_1, file_bin_2):
    vector = mkncion.leer_file(file_bin_1)
    promedio = prom_rep(vector)
    nuevo_vector = max_prom_rep(vector, promedio)
    veinte_viral(nuevo_vector, file_bin_2)
    vector = mkncion.leer_file(file_bin_2)
    return vector


def prom_rep(vector):
    n = len(vector)
    total = 0
    for cancion in vector:
        total += cancion.rep
    promedio = total / n
    return promedio


def max_prom_rep(vector, promedio):
    nuevo_vector = []
    for cancion in vector:
        if cancion.rep >= promedio:
            nuevo_vector.append(cancion)
    nuevo_vector = ordena_max_prom_rep(nuevo_vector)
    return nuevo_vector


def ordena_max_prom_rep(vector):
    n = len(vector)
    for i in range(n):
        for j in range(n - i - 1):
            if vector[j].rep < vector[j+1].rep:
                vector[j], vector[j+1] = vector[j+1], vector[j]
    return vector


def veinte_viral(vector, file_bin):
    n = len(vector)
    if n <= 20:
        mkncion.crear_file(vector, file_bin)
    else:
        n_vector = []
        for i in range(20):
            n_vector.append(vector[i])
            veinte_viral(n_vector, file_bin)


def opcion_5(file_bin_1, file_bin_2):
    if os.path.exists(file_bin_2) is False:
        vector = opcion_4(file_bin_1, file_bin_2)
    else:
        vector = mkncion.leer_file(file_bin_2)
    frase_busqueda = str(input("Ingrese el interprete a buscar en los \"Virales 20\": "))
    nuevo_vector = []
    for cancion in vector:
        if cancion.interprete.lower() == frase_busqueda.lower():
            nuevo_vector.append(cancion)
    if len(nuevo_vector) is 0:
        print("No se encontro ninguna cancion de \"{0}\" en los Virales 20.".format(frase_busqueda.title()))
    else:
        mkncion.muestra(nuevo_vector)


def opcion_6(file_bin):
    d = str(input("Ingrese el nombre del disco: "))
    i = str(input("Ingrese el interprete: "))
    canciones_list = []
    vector = mkncion.leer_file(file_bin)
    for cancion in vector:
        if cancion.interprete.lower() == i.lower():
            if cancion.disco.lower() == d.lower():
                canciones_list.append(cancion.titulo)
    if len(canciones_list) is 0:
        print("No se encontro el disco \"{0}\" del artista \"{1}\".".format(d.title(), i.title()))
    else:
        m = open(i.title() + "-" + d.title() + ".txt", "w")
        r = muestra_op(canciones_list, d, i)
        m.write(r)
        m.close()
        m = open(i + "-" + d + ".txt")
        print(m.read())
        m.close()


def muestra_op(canciones_list, d, i):
    r = ""
    r += "-----------------------------------------"
    r += "\n" + str(d).upper()
    r += "\n(" + str(i).title() + ")"
    for j in range(len(canciones_list)):
        r += "\n" + str(j+1) + ". " + canciones_list[j]
    r += "\n\n(Total: " + str(len(canciones_list)) + " canciones)"
    r += "\n-----------------------------------------\n"
    return r


def test():
    file_bin_1 = "canciones.dat"
    file_bin_2 = "virales.dat"
    print("Ingrese la cantidad de canciones a generar: ")
    vector_length = mkncion.valida_int()
    vector = mkncion.carga_auto_ordenada(vector_length)
    mkncion.crear_file(vector, file_bin_1)

    opcion = 0
    while opcion != 9:
        print("""
        Menu de opciones

        1_ Mostrar reproducciones por idioma y genero.
        2_ Mostrar canciones ordenadas por titulo.
        3_ Añadir reproduccion a cancion.
        4_ Mostrar las "Virales 20".
        5_ Mostrar de las "Virales 20" las canciones de un artista particular.
        6_ Canciones de un disco e interprete determinado.
        9_ Salir...



        """)
        print("Elija una opcion: ")
        opcion = mkncion.valida_int()
        print("\n" * 75)
        if opcion == 1:
            print("Mostrar reproducciones por idioma y genero.")
            opcion_1(file_bin_1)
            input("Volver...")
            print("\n" * 75)
        elif opcion == 2:
            print("Mostrar canciones ordenadas por titulo.")
            opcion_2(file_bin_1)
            input("Volver...")
            print("\n" * 75)
        elif opcion == 3:
            print("Añadir reproduccion a cancion.")
            opcion_3(file_bin_1)
            input("Volver...")
            print("\n" * 75)
        elif opcion == 4:
            print("Mostrar las \"Virales 20\".")
            if os.path.exists(file_bin_2) is False:
                vector = opcion_4(file_bin_1, file_bin_2)
            else:
                vector = mkncion.leer_file(file_bin_2)
            mkncion.muestra(vector)
            input("Volver...")
            print("\n" * 75)
        elif opcion == 5:
            print("Mostrar de las \"Virales 20\" las canciones de un artista particular.")
            opcion_5(file_bin_1, file_bin_2)
            input("Volver...")
            print("\n" * 75)
        elif opcion == 6:
            print("Canciones de un disco e interprete determinado.")
            opcion_6(file_bin_1)
            input("Volver...")
            print("\n" * 75)
        elif opcion == 9:
            pass
    print("\n" * 75, "Cerrando programa... ")


if __name__ == '__main__':
    test()
