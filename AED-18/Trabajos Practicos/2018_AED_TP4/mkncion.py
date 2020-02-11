#!/usr/bin/env python
# -*- coding:utf-8 -*-


import pickle
import random

titulo_vec = ["I Like It", "This Is America", "Back To You", "SAD!",
              "Nice For What", "God's Plans", "TheMiddle", "One Kiss",
              "Make Me Feel", "No Brainer", "Look Alive", "Lucid Dreams",
              "In My Blood", "Friends", "Jackie Chan", "Call Out My Name"]
disco_vec = ["Golden Hour", "Invasion Of Privacy", "Daytona", "Care For Me",
             "Scorpion", "Isolation", "R.A.M.", "American Utopia",
             "And Nothing Hurt"]
artista_vec = ["Eminen", "Drake", "Taylor Swift", "Justin Bieber",
               "Ed Sherman", "Maroon 5", "Ariana Grande", "Rihanna",
               "Selena Gomez"]
genero_lst = ["Rock", "Pop", "Infantil", "Reggae", "Clasica", "Indie", "Hip-Hop", "Jazz", "Electronica",
              "Metal"]
idioma_lst = ["Inglés", "Español", "Francés", "Otros"]


class Cancion:  # Crecion del registro Cancion con sus atributos.
    def __init__(self, titulo, disco, interprete, idioma, genero, rep):
        self.titulo = titulo
        self.disco = disco
        self.interprete = interprete
        self.idioma = idioma
        self.genero = genero
        self.rep = rep


def to_string(cancion):  # Funcion que ordena los datos del registro para que se puedan ver claramente.
    r = ''
    r += "\nTitulo: " + str(cancion.titulo)
    r += "\nDisco: " + str(cancion.disco)
    r += "\nInterprete: " + str(cancion.interprete)
    r += "\nIdioma: " + str(idioma_lst[cancion.idioma])
    r += "\nGenero: " + str(genero_lst[cancion.genero])
    r += "\nReproducciones: " + str(cancion.rep)
    return r


def carga_auto_ordenada(vector_length):  # Genera los registros de manera automatica y ordenada por titulo.
    vector = []
    for pos in range(vector_length):
        titulo = random.choice(titulo_vec)
        disco = random.choice(disco_vec)
        interprete = random.choice(artista_vec)
        idioma = random.randint(0, 3)
        genero = random.randint(0, 9)
        rep = random.randint(0, 100000)
        cancion = Cancion(titulo, disco, interprete, idioma, genero, rep)
        add_in_order(vector, cancion)
    return vector


def add_in_order(vector, cancion):
    n = len(vector)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if vector[c].titulo == cancion.titulo:
            pos = c
            break
        if cancion.titulo < vector[c].titulo:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    vector[pos:pos] = [cancion]


def crear_file(vector, file_bin):  # Crea un archivo binarios.
    m = open(file_bin, 'wb')
    pickle.dump(vector, m)
    m.close()


def leer_file(file_bin):  # Toma los datos del archivo y los devuelve en Vector.
    m = open(file_bin, "rb")
    vector = pickle.load(m)
    m.close()
    return vector


def muestra(vector):  # Muestra cada registro Cancion del vector invocando la funcion to_string.
    for cancion in vector:
        print(to_string(cancion))


def valida_int():
    while True:
        try:
            numero = int(input())
            break
        except ValueError:
            print("ERROR: ")
    return numero


def test():  # Prueba el Programa.
    file_bin = "canciones.dat"  # Nombre del Archivo a generar.
    print("Ingrese la cantidad de registros a generar.")  # Cantidad de registros a cargar.
    vector_length = valida_int()
    vector = carga_auto_ordenada(vector_length)  # Generacion del Vector.
    crear_file(vector, file_bin)  # Creacion del Archivo.
    vector = leer_file(file_bin)  # Lectura de los datos del Archivo.
    muestra(vector)  # Muestra de los Registros del Vector en el Archivo.


if __name__ == '__main__':
    test()
