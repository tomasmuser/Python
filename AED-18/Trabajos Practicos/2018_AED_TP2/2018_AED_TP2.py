"""
Recaudación acumulada del día.                                      "recaudacion_total"
Promedio de recaudación por caja (un único monto).                  "recaudacion_total/4"

Monto promedio por venta (un único monto).                          "recaudacion_total/n_ven"
Cantidad promedio de ítems por venta (una única cantidad).          "items_total/n_ven"

Recaudación por caja (son 4 montos).                                "c1_r c2_r c3_r c4_r"
Número de caja con mayor recaudación.                               "may(c1_r c2_r c3_r c4_r)

Cantidad de ventas por caja (son 4 cantidades).                     "c1_v c2_v c3_v c4_v"
Número de caja con menor cantidad de ventas.                        "men(c1_v c2_v c3_v c4_v)"

Venta con mayor monto total.                                        "venta_mayor"


Determinar la cantidad de ventas con hasta 10 unidades vendidas.    "ventas_rap10"
Si esta cantidad fuera igual o mayor al promedio de ventas por caja indicar con un mensaje que deben
abrirse dos cajas rápidas.
"""

import random


def validar_cuit (c):
    numeros = '1234567890' #Numeros admitidos
    numero_persona_real = '0347' #para validar que el primer numero sea 20 23 24 27
    numero_persona_juridica = '034' # Para validar que el primer numero sea 30 33 34
                #Si lo deseas lo puedes quitar.
    l = len(c)
    ok = True #La bandera empieza valiendo True, en caso de que algo no sea correcto al final de ciclo for terminaria valiendo false
    if l !=13: #Comprueva que sea una tupla de largo 13
        ok = False
    if c[0] != '2' and c[0] != '3': #Para validar que el primer numero sea 20 23 24 27 30 33 34 37
        ok = False
    if c[0] == '2':
        if not (c[1] in numero_persona_real):
            ok = False
    elif c[0] == '3':
        if not (c[1] in numero_persona_juridica):
            ok = False
    for i in range(l):
        if i == 2:
            if c[i] != '-':
                ok = False
        elif i == 11:
            if c[i] != '-':
                ok = False
        elif not c[i] in numeros:
            ok = False
    return ok


def validador_num_caja():
    """Comprueba que el numero ingresado sea un entero mayor que cero y menor que 4"""

    while True:
        num_caja = val_num_int()
        if num_caja > 4:
            print("Las cajas son 1, 2 ,3 o 4.")
        elif 0 < num_caja <= 4:
            break
    return num_caja


def val_num_int():
    """Esta funcion se asegura que el valor de ventas sea un numero [1,ꝏ)"""
    num_int = 0
    while True:  # Ciclo infinito, solo se corta si se ingresa un valor valido.
        try:
            while num_int <= 0:
                num_int = int(input())
                if num_int <= 0:
                    print("Debe ingresar un numero positivo...")
            break
        except ValueError:
            print("\nDebe ingresar un Numero...\n")
    return num_int


def carga_ventas_manu():
    """Carga manual de datos."""
    print("Ingrese el numero de caja (1,2,3,4): ")
    num_caja = validador_num_caja()
    print("Ingrese el numero de items: ")
    items_venta = val_num_int()
    print("Ingrese el monto de Recaudacion: ")
    recaudacion_venta = val_num_int()

    return num_caja, items_venta, recaudacion_venta


def carga_ventas_auto():
    """Carga atomatica de datos."""
    num_caja = random.randint(1, 4)
    items_venta = random.randint(1, 10)
    recaudacion_venta = random.randint(1, 50000)

    return num_caja, items_venta, recaudacion_venta


def carga_ventas(flag_auto):
    """Esta funcion carga todos los valores de las cajas en sus respectivas variables y las devuelve"""
    items_total = 0  # Total de items de todas las ventas.
    recaudacion_total = 0  # Total de Recaudacion de todas las ventas.
    ventas_rap10 = 0  # Contador de ventas menores a diez (10) items.

    venta_mayor_caja = 0   # Caja de venta con mayor recaudacion.
    venta_mayor_items = 0  # Items de venta con mayor recaudacion.
    venta_mayor_recau = 0  # Recaudacion de venta con mayor recaudacion.

    c1_i = 0  # Items de caja 1.
    c1_r = 0  # Recaudacion de caja 1.
    c1_v = 0  # Ventas de caja 1.

    c2_i = 0  # Items de caja 2.
    c2_r = 0  # Recaudacion de caja 2.
    c2_v = 0  # Ventas de caja 2.

    c3_i = 0  # Items de caja 3.
    c3_r = 0  # Recaudacion de caja 3.
    c3_v = 0  # Ventas de caja 3.

    c4_i = 0  # Items de caja 4.
    c4_r = 0  # Recaudacion de caja 4.
    c4_v = 0  # Ventas de caja 4.

    print("Ingrese la cantidad de ventas: ")
    num_ventas = val_num_int()

    for venta in range(num_ventas):
        if flag_auto is False:
            num_caja, items_venta, recaudacion_venta = carga_ventas_manu()
        elif flag_auto is True:
            num_caja, items_venta, recaudacion_venta = carga_ventas_auto()

        # Cantidad total de items y recaudacion.
        items_total += items_venta
        recaudacion_total += recaudacion_venta

        if items_venta <= 10:
            ventas_rap10 += 1

        # Monto de la venta con mayor monto total. Indicar caja y cuántos artículos.
        if recaudacion_venta > venta_mayor_recau:

            venta_mayor_caja = num_caja
            venta_mayor_items = items_venta
            venta_mayor_recau = recaudacion_venta

        if num_caja == 1:
            c1_i += items_venta
            c1_r += recaudacion_venta
            c1_v += 1

        elif num_caja == 2:
            c2_i += items_venta
            c2_r += recaudacion_venta
            c2_v += 1

        elif num_caja == 3:
            c3_i += items_venta
            c3_r += recaudacion_venta
            c3_v += 1

        elif num_caja == 4:
            c4_i += items_venta
            c4_r += recaudacion_venta
            c4_v += 1

    return ventas_rap10, num_ventas, items_total, recaudacion_total, c1_i, c1_r, c1_v, c2_i, c2_r, c2_v, c3_i, c3_r,\
        c3_v, c4_i, c4_r, c4_v, venta_mayor_caja, venta_mayor_items, venta_mayor_recau


def recau_mayor(c1_r, c2_r, c3_r, c4_r):
    recaudacion_mayor = max(c1_r, c2_r, c3_r, c4_r)
    if recaudacion_mayor == c1_r:
        caja_mayor_recau = 1
    elif recaudacion_mayor == c2_r:
        caja_mayor_recau = 2
    elif recaudacion_mayor == c3_r:
        caja_mayor_recau = 3
    elif recaudacion_mayor == c4_r:
        caja_mayor_recau = 4
    return caja_mayor_recau, recaudacion_mayor


def ventas_menor(c1_v, c2_v, c3_v, c4_v):
    ventas_menor_num = min(c1_v, c2_v, c3_v, c4_v)
    if ventas_menor_num == c1_v:
        caja_menor_ventas = 1
    elif ventas_menor_num == c2_v:
        caja_menor_ventas = 2
    elif ventas_menor_num == c3_v:
        caja_menor_ventas = 3
    elif ventas_menor_num == c4_v:
        caja_menor_ventas = 4
    return caja_menor_ventas, ventas_menor_num


def menu_2(flag_auto):
    ventas_rap10, num_ventas, items_total, recaudacion_total, c1_i, c1_r, c1_v, c2_i, c2_r, c2_v, c3_i, c3_r, c3_v,\
        c4_i, c4_r, c4_v, venta_mayor_caja, venta_mayor_items, venta_mayor_recau = carga_ventas(flag_auto)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Datos cargados correctamente")

    if ventas_rap10 >= (num_ventas / 4):
        print("\nDeben abrirse dos(2) cajas rapidas.")
    opcion = 10
    while opcion != 81:
        print("\nMenu de datos.")
        print("(1) Recaudación acumulada del día.")
        print("(2) Promedio de recaudación por caja.")
        print("(3) Monto promedio por venta.")
        print("(4) Cantidad promedio de ítems por venta.")
        print("(5) Recaudación por caja.")
        print("(6) Número de caja con mayor recaudación.")
        print("(7) Cantidad de ventas por caja.")
        print("(8) Número de caja con menor cantidad de ventas.")
        print("(9) Venta con mayor monto total.")
        print("(81) Volver al menu anterior (Se perderan todos los datos).")
        print("Ingrese la opcion deseada: ")
        opcion = val_num_int()

        if opcion == 1:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("Recaudación acumulada del día:  ", recaudacion_total)
        elif opcion == 2:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("Promedio de recaudación por caja: ", recaudacion_total/4)
        elif opcion == 3:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("Monto promedio por venta: ", recaudacion_total/num_ventas)
        elif opcion == 4:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("Cantidad promedio de ítems por venta: ", items_total/num_ventas)
        elif opcion == 5:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("Recaudación por caja: ",
                  "\nCaja 1: ", c1_r,
                  "\nCaja 2: ", c2_r,
                  "\nCaja 3: ", c3_r,
                  "\nCaja 4: ", c4_r)
        elif opcion == 6:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            caja_mayor_recau, recaudacion_mayor = recau_mayor(c1_r, c2_r, c3_r, c4_r)
            print("Número de caja con mayor recaudación: ", caja_mayor_recau,
                  "\nRecaudacion total de la caja: ", recaudacion_mayor)
        elif opcion == 7:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("Cantidad de ventas por caja: ",
                  "\nCaja 1: ", c1_v,
                  "\nCaja 2: ", c2_v,
                  "\nCaja 3: ", c3_v,
                  "\nCaja 4: ", c4_v)
        elif opcion == 8:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            caja_menor_ventas, ventas_menor_num = ventas_menor(c1_v, c2_v, c3_v, c4_v)
            print("Número de caja con menor cantidad de ventas: ", caja_menor_ventas,
                  "\nVentas totales de la caja: ", ventas_menor_num)
        elif opcion == 9:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("Venta con mayor monto total.",
                  "\nCaja n: ", venta_mayor_caja,
                  "\nItems vendidos: ", venta_mayor_items,
                  "\nRecaudacion total: ", venta_mayor_recau)
        elif opcion == 81:
            print("Saliendo....")
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("Opcion incorrecta...")
    return 0

cuit_base = "00-00000000-0"
num_cuit = cuit_base
razon_social = ""

print("Bienvenido.\n")
if num_cuit == cuit_base:
    while True:
        print("CUIT: ", num_cuit, "\nRazon Social: ", razon_social)
        print("\n¿Desea cambiar los datos de Cuit y Razon Social?")
        print("Sí(1) - No(2)")
        print("\nIngrese la opcion deseada: ")
        carga_cuit_opc = val_num_int()
        if carga_cuit_opc == 1:
            print("\nEligio SÍ(1).\n")
            razon_social = input('Ingrese la Razon Social.')
            num_cuit = input('Ingrese el numero de cuit incluyendo guiones.')

            flag_cuit_valido = False
            while flag_cuit_valido is False:
                flag_cuit_valido = validar_cuit(num_cuit)
                if flag_cuit_valido is False:
                    num_cuit = input('Error, ingrese un cuit valido')
                else:
                    break
        elif carga_cuit_opc == 2:
            print("\nEligio NO(2).\n")
            break
        else:
            print("Error...\nReintente...\n")
else:
    print("CUIT: ", num_cuit, "\nRazon Social: ", razon_social)
while True:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Carga de Datos.")
    print("1. Carga manual.")
    print("2. Carga automatica.")
    print("3. Salir.")
    print("\nIngrese la opcion deseada: ")
    opcion = val_num_int()
    if opcion == 1:
        print("Carga manual de datos.")
        flag_auto = False
        menu_2(flag_auto)
    elif opcion == 2:
        print("Carga automatica de datos.")
        flag_auto = True
        menu_2(flag_auto)
    elif opcion == 3:
        "Cerrando programa...."
        break
    else:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("Opcion incorrecta...")
