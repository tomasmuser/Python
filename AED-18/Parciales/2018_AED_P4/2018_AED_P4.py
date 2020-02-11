import random
import pickle
import os.path


list_pais = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"]
list_genero = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


class Pelicula:
    def __init__(self, idem, titulo, importe, genero, pais):
        self.idem = idem
        self.titulo = titulo
        self.importe = importe
        self.genero = genero
        self.pais = pais


def to_string(registro):
    r = ""
    r += "ID: {} Titulo: {} Importe: {} Genero: {} Pais: {}".format(registro.idem, registro.titulo, registro.importe,
                                                                    list_genero[registro.genero],
                                                                    list_pais[registro.pais])
    return r


def muestra_registro(vector):
    for registro in vector:
        print(to_string(registro))


def carga_automatica(vector_lenght):
    vector = []
    for i in range(vector_lenght):
        idem = random.randint(0, vector_lenght)
        titulo = random.choice("abcdefgh")
        importe = round(random.random() * 1000000, 2)
        genero = random.randint(0, 9)
        pais = random.randint(0, 19)
        registro = Pelicula(idem, titulo, importe, genero, pais)
        add_in_order(vector, registro)
    return vector


def add_in_order(vector, registro):
    n = len(vector)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if vector[c].titulo == registro.titulo:
            pos = c
            break
        if vector[c].titulo > registro.titulo:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    vector[pos:pos] = [registro]


def valida_int():
    try:
        numero = int(input())
    except ValueError:
        print("Error", end="")
        numero = valida_int()
    return numero


def valida_float():
    try:
        numero = float(input())
    except ValueError:
        print("Error", end="")
        numero = valida_int()
    return numero


def opcion_2(vector):
    nuevo_vector = []
    x = valida_float()
    for registro in vector:
        if (registro.pais != 10) and (registro.importe < x):
            nuevo_vector.append(registro)
    return nuevo_vector


def crea_archivo(vector, file_bin):
    m = open(file_bin, 'wb')
    pickle.dump(vector, m)
    m.close()


def abrir_archivo(file_bin):
    m = open(file_bin, 'rb')
    vector = pickle.load(m)
    m.close
    return vector


def opcion_4(vector):
    encontro = False
    num = valida_int()
    for registro in vector:
        if registro.idem == num:
            print(to_string(registro))
            encontro = True
            break
    if not encontro:
        print("No existe registro solicitado.")


def opcion_5(vector):
    matriz = [[0] * 10 for i in range(20)]
    for registro in vector:
        matriz[registro.pais][registro.genero] += 1
    return matriz


def muestra_matriz(matriz):
    for i in range(20):
        print("\nPais: {}".format(list_pais[i]))
        for j in range(10):
            if matriz[i][j] != 0:
                print("\nGenero: {0} \nCantidad: {1}".format(list_genero[j], matriz[i][j]))


def test():
    print("Ingrese la cantidad de registos a generar: ")
    vector_lenght = valida_int()
    vector = carga_automatica(vector_lenght)
    if vector is []:
        print("No se genero ningun registro...\n Reintente...")
        test()

    opcion = 0
    while opcion != 6:
        print("""
        Registros generados exitosamente.

        Opcion 1: Mostrar los registros.
        Opcion 2: Crear Archivo de Peliculas segun Importe.
        Opcion 3: Mostrar Peliculas de Opcion 2.
        Opcion 4: Busqueda por ID una Pelicula.
        Opcion 5: Mostrar cantidad de Peliculas por Genero y Pais.
        Opcion 6: Salir.
        """)
        opcion = valida_int()
        print("\n" * 100)

        if opcion == 1:
            muestra_registro(vector)
            input("Volver...")
            print("\n" * 100)

        elif opcion == 2:
            file_bin = "Peliculas.dat"
            print("Ingrese el monto maximo del importe."
                  "(Las peliculas del pais {0} no seran incluidas)".format(list_pais[10]))
            nuevo_vector = opcion_2(vector)
            if nuevo_vector == []:
                print("No se encontraron peliculas con monto menor al requerido.")
            else:
                crea_archivo(nuevo_vector, file_bin)
                print("Generado existosamente")
            input("Volver...")
            print("\n" * 100)

        elif opcion == 3:  # En caso de cambiar el parametro de opc 2 y no encontrar nada pero ya haber una busqueda previa devuelve la ultima busqueda
            file_bin = "Peliculas.dat"
            if not os.path.exists(file_bin):
                print("No hay nada para mostrar.")
            else:
                nuevo_vector = abrir_archivo(file_bin)
                muestra_registro(nuevo_vector)
            input("Volver...")
            print("\n" * 100)

        elif opcion == 4:
            print("Ingrese el valor del ID a buscar en los registros.")
            opcion_4(vector)
            input("Volver...")
            print("\n" * 100)

        elif opcion == 5:
            matriz = opcion_5(vector)
            muestra_matriz(matriz)
            input("Volver...")
            print("\n" * 100)

        elif opcion == 6:
            break

    print("Fin del programa....")


if __name__ == '__main__':
    test()
