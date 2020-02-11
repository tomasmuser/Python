import random

class Paciente:
    def __init__(self, id, nombre, practica, dias, medicamentos):
        self.id = id
        self.nombre = nombre
        self.practica =  practica
        self.dias = dias
        self.medicamentos = medicamentos


def to_strig(paciente):
    r = ""
    r += "-ID: " + str(paciente.id)
    r += "\n-Nombre: " + paciente.nombre
    r += "\n-Practica: " + str(paciente.practica)
    r += "\n-Dias: " + str(paciente.dias)
    r += "\n-Medicamentos: " + str(paciente.medicamentos)
    r += "\n---------------------------------------------\n"
    return r


def carga_pacientes_auto(n):
    vector_nombres = ["Tomás", "Juan", "Martin", "Ivan", "Roman", "Matias", "Julieta", "Ivonne", "Romina", "Yamil",
                      "Veronica"]
    pacientes = [None] * n
    for i in range(n):
        id = i+1
        nombre = random.choice(vector_nombres)
        practica = random.randint(0, 29)
        dias = random.randint(1,1000)
        medicamentos = random.randint(0, 200)
        pacientes[i] = Paciente(id, nombre, practica, dias, medicamentos)
    pacientes = ordena_nombres(pacientes)
    return pacientes


def ordena_nombres(vector):
    n = len(vector)
    for i in range(0, n):
        for j in range(i+1, n):
            if vector[i].nombre > vector[j].nombre:
                vector[i], vector[j] = vector[j], vector[i]
    return vector


def contador_practicas(vector):
    contador = [0] * 30
    for i in vector:
        n = i.practica
        contador[n] += 1
    return contador


def busqueda_paciente(vector, id_b, dias_b):
    for i in vector:
        if i.id == id_b and i.dias >= dias_b:
            return print(to_strig(i))
    print("No se encontro paciente...")


def printer_pacientes(vector):
    for i in vector:
        print(to_strig(i))


def muestra_practicas(vector):
    n = len(vector)
    for i in range(n):
        print("Practica " + str(i), ": ", vector[i])


def menu():
    print("Bienvenido al Sistema de Pacientes.")
    n = int(input("Ingrese la cantidad de Pacientes que desea que se carguen: "))
    pacientes = carga_pacientes_auto(n)
    print("Los pacientes se cargaron correctamente...")
    opcion = 0
    while opcion != 4:
        print("""
        Menu de Opciones:
        1_ Muestra los pacientes por nombre.
        2_ Muestra el contador de practicas.
        3_ Busqueda de pacientes.
        4_ Salir
        """)
        opcion =  int(input())
        if opcion== 1:
            printer_pacientes(pacientes)
        elif opcion == 2:
            muestra_practicas(contador_practicas(pacientes))
        elif opcion == 3:
            id_b = int(input("Ingrese el ID: "))
            dias_b = int(input("Ingrese la cantidad de dias: "))
            busqueda_paciente(pacientes, id_b, dias_b)


if __name__ == '__main__':
    menu()




