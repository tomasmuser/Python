# -*- coding: utf-8 -*-
import random
import canciones


artista_vec = ["Eminen", "Drake", "Taylor Swift", "Justin Bieber",
               "Ed Sherman", "Maroon 5", "Ariana Grande", "Rihanna",
               "Selena Gomez"]
disco_vec = ["Golden Hour", "Invasion Of Privacy", "Daytona", "Care For Me",
             "Scorpion", "Isolation", "R.A.M.", "American Utopia",
             "And Nothing Hurt"]
titulo_vec = ["I Like It", "This Is America", "Back To You", "SAD!",
              "Nice For What", "God's Plans", "TheMiddle", "One Kiss",
              "Make Me Feel", "No Brainer", "Look Alive", "Lucid Dreams",
              "In My Blood", "Friends", "Jackie Chan", "Call Out My Name"]


def carga_auto(n):
    song_list = [None] * n  # n se ingresa por teclado y debe ser menor o igual a 20, validarlo
    for i in range(n):
        titulo = random.choice(titulo_vec)
        disco = random.choice(disco_vec)
        artista = random.choice(artista_vec)
        idioma = random.randint(0, 3)
        genero = random.randint(0, 9)
        rep = random.randint(0, 100000)
        song_list[i] = canciones.Cancion(titulo, disco, artista,
                                         idioma, genero, rep)
    return song_list


def read(vector):
    for i in vector:
        r = canciones.to_string(i)
        print(r)


def ordena_titulo(vector):
    n = len(vector)
    for i in range(n):
        for j in range(n-i-1):
            if vector[j].titulo > vector[j+1].titulo:
                vector[j], vector[j+1] = vector[j+1], vector[j]
    return vector


def ordena_rep(vector):
    n = len(vector)
    for i in range(n):
        for j in range(n-i-1):
            if vector[j].rep > vector[j+1].rep:
                vector[j], vector[j+1] = vector[j+1], vector[j]
    return vector


def busqueda_disco(vector,  nombre):
    nuevo_vector = []
    nombre = nombre.title()
    for cancion in vector:
        if cancion.disco == nombre:
            nuevo_vector.append(cancion)
    if nuevo_vector == []:
        print("No se encontraron canciones de dicho albun")
    return nuevo_vector


def busqueda_artista(vector,  nombre):
    nuevo_vector = []
    nombre = nombre.title()
    for cancion in vector:
        if cancion.artista == nombre:
            nuevo_vector.append(cancion)
    if nuevo_vector == []:
        print("No se encontraron canciones de dicho artista")
    return nuevo_vector


def promedio_reps(vector):
    reps = 0
    n = len(vector)
    for cancion in vector:
        reps += cancion.rep
    reps = reps / n
    return reps


def max_reps(vector, reps):
    nuevo_vector = []
    for cancion in vector:
        if cancion.rep >= reps:
            nuevo_vector.append(cancion)
    return nuevo_vector


def cancion_max(vector):
    maximo = []
    n = len(vector)
    a = -1
    if n <= 1:
        return vector
    while vector[a].rep == vector[a-1].rep:
        maximo.append(vector[a-1])
        a -= 1
    return maximo


def gen_matriz():
    matriz = [[0] * 4 for f in range(10)]
    return matriz


def carga_matriz(vector):
    matriz = gen_matriz()
    for cancion in vector:
        matriz[cancion.genero][cancion.idioma] += 1
    return matriz


def conteo_idioma(matriz, idioma):
    conteo = 0
    for i in matriz:
        print(i)
        conteo += i[idioma]
    return conteo


def printer_matriz(matriz):
    for i in matriz:
        print(i)


def menu():
    n = 0
    while n <= 0 or n > 20:
        print("Ingrese la cantidad de canciones que desea para el vector, recuerde que como maximo deberan ser 20.")
        n = int(input())
    print(n)


    song_list = carga_auto(n)
    song_list = ordena_titulo(song_list)
    reproducciones = promedio_reps(song_list)
    maximos = max_reps(song_list, reproducciones)
    matriz = carga_matriz(song_list)

    opcion = 0
    while opcion != 9:
        print("""
        Bienvenido!!! ☺
        El vector ya fue generado. Por favor ingrese una de las siguientes opciones:
    
        1_ Muestra el vector ordenado alfabéticamente por título.
        2_ Búsqueda por DISCO.
        3_ Ver canciones que superan el promedio de reproducciones.
        4_ Ver la canción de determinado artista con más reproducciones.
        5_ Ver una matriz con los idiomas y géneros.
        6_ Ver las canciones totales de un idioma.
        9_ Salir
        """)
        opcion = int(input("Elija:"))
        if opcion == 1:
            read(song_list)

        elif opcion == 2:
            frase_busqueda = input("Ingrese el nombre del disco a buscar: ")
            vector_busqueda = busqueda_disco(song_list, frase_busqueda)
            read(vector_busqueda)

        elif opcion == 3:
            print("Canciones que superan el máximo.")
            read(maximos)

        elif opcion == 4:
            frase_busqueda = input("Ingrese el nombre del artista: ")
            vector_busqueda = busqueda_artista(song_list,frase_busqueda)
            rep_ordenados = ordena_rep(vector_busqueda)
            rep_maximo = cancion_max(rep_ordenados)
            read(rep_maximo)

        elif opcion == 5:
            print("Matriz idioma género")
            printer_matriz(matriz)

        elif opcion == 6:
            idioma_busqueda = int(input("Ingrese un idioma: "))
            conteo = conteo_idioma(matriz, idioma_busqueda)
            print("En el idioma", idioma_busqueda ,"hay", conteo ,"canciones")

if __name__ == "__main__":
    menu()
