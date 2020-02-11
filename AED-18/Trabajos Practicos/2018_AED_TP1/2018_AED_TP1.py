__author__ = "Muser-Perea"
# Se utiliza para generar valores aleatorios
import random


print("Bienvenido al juego de dardos.")
print("""
Reglas de juego.

-Cada porción de la diana está encabezada por un número que indica la puntuación de un dardo que cae en esa zona.

\t♥Si el dardo cae en centro contabiliza 50 puntos.
\t♥Si cae en el anillo que rodea al centro vale 25 puntos.
\t♥Si el dardo entra en el círculo más interior la puntuación se duplica y si cae en el círculo  exterior la puntuación se triplica.
\t♥Si los dardos que caen fuera de la diana suman cero puntos.
""")


# Se carga el nombre del jugador
nombre_jugador = input("Jugador 1: ")

# Primer JUGADA
print("\nPrimer tiro...\n")

# La semilla es un valor aleatorio float comprendido en intervalo [0,1).
semilla_1 = random.random()

# Suerte convierte la semilla en un valor entero entre [0,99].
suerte_1 = int(semilla_1 * 100)

# Dependiendo la suerte se asigna un multiplicador comprendido en [0,3] U [25] U [50].
if suerte_1 <= 15:
    multiplicador_1 = 0
elif 15 < suerte_1 < 88:
    multiplicador_1 = 1
elif 88 <= suerte_1 < 94:
    multiplicador_1 = 2
elif 94 <= suerte_1 < 96:
    multiplicador_1 = 3
elif 96 <= suerte_1 < 98:
    multiplicador_1 = 25
elif 98 <= suerte_1:
    multiplicador_1 = 50

# Si sale 0, 25 o 50 se asigna el puntaje directamente del multiplicador.
if multiplicador_1 == 0 or multiplicador_1 == 25 or multiplicador_1 == 50:
    puntaje_1 = multiplicador_1

# En caso de que el valor sea diferente a 0, 25 o 50 se procede a hacer una tirada [1,20]
# Y multiplicar la tirada con el multiplicador.
else:
    tiro_1 = random.randint(1,20)
    puntaje_1 = tiro_1 * multiplicador_1

# Dependiendo el valor del tiro se le asigna el color en el tablero rojo o verde y blanco o negro y fuera.
if multiplicador_1 == 0:
    color_1 = 0
elif multiplicador_1 == 25:
    color_1 = 5
elif multiplicador_1 == 50:
    color_1 = 6
elif multiplicador_1 == 1:
    if tiro_1 == 1 or tiro_1 == 4 or tiro_1 == 6 or tiro_1 == 15 or tiro_1 == 17 or tiro_1 == 19 or tiro_1 == 16 or tiro_1 == 11 or tiro_1 == 9 or tiro_1 == 5:
        color_1 = 2
    else:
        color_1 = 1
elif multiplicador_1 == 2:
    if tiro_1 == 1 or tiro_1 == 4 or tiro_1 == 6 or tiro_1 == 15 or tiro_1 == 17 or tiro_1 == 19 or tiro_1 == 16 or tiro_1 == 11 or tiro_1 == 9 or tiro_1 == 5:
        color_1 = 3
    else:
        color_1 = 4
elif multiplicador_1 == 3:
    if tiro_1 == 1 or tiro_1 == 4 or tiro_1 == 6 or tiro_1 == 15 or tiro_1 == 17 or tiro_1 == 19 or tiro_1 == 16 or tiro_1 == 11 or tiro_1 == 9 or tiro_1 == 5:
        color_1 = 33
    else:
        color_1 = 43

if color_1 == 0:
    print("\tCayó fuera.")
elif color_1 == 1:
    print("\tValor de tiro: ", tiro_1,"\n\tColor: Negro\n\tMultiplica: NO")
elif color_1 == 2:
    print("\tValor de tiro: ", tiro_1,"\n\tColor: Blanco\n\tMultiplica: NO")
elif color_1 == 3:
    print("\tValor de tiro: ", tiro_1,"\n\tColor: Verde\n\tMultiplica: Doble\n\tPuntaje Total: ", puntaje_1)
elif color_1 == 4:
    print("\tValor de tiro: ", tiro_1,"\n\tColor: Rojo\n\tMultiplica: Doble\n\tPuntaje Total: ", puntaje_1)
elif color_1 == 33:
    print("\tValor de tiro: ", tiro_1,"\n\tColor: Verde\n\tMultiplica: Triple\n\tPuntaje Total: ", puntaje_1)
elif color_1 == 43:
    print("\tValor de tiro: ", tiro_1,"\n\tColor: Rojo\n\tMultiplica: Triple\n\tPuntaje Total: ", puntaje_1)
elif color_1 == 5:
    print("\tValor de tiro: ", puntaje_1,"\n\tColor: Verde\n\tMultiplica: NO")
elif color_1 == 6:
    print("\tValor de tiro: ", puntaje_1,"\n\tColor: Rojo\n\tMultiplica: NO")

# Segunda JUGADA
print("\nSegundo tiro...\n")

# La semilla es un valor aleatorio float comprendido en intervalo [0,1).
semilla_2 = random.random()

# Suerte convierte la semilla en un valor entero entre [0,99].
suerte_2 = int(semilla_2 * 100)

# Dependiendo la suerte se asigna un multiplicador comprendido en [0,3] U [25] U [50].
if suerte_2 <= 15:
    multiplicador_2 = 0
elif 15 < suerte_2 < 88:
    multiplicador_2 = 1
elif 88 <= suerte_2 < 94:
    multiplicador_2 = 2
elif 94 <= suerte_2 < 96:
    multiplicador_2 = 3
elif 96 <= suerte_2 < 98:
    multiplicador_2 = 25
elif 98 <= suerte_2:
    multiplicador_2 = 50

# Si sale 0, 25 o 50 se asigna el puntaje directamente del multiplicador.
if multiplicador_2 == 0 or multiplicador_2 == 25 or multiplicador_2 == 50:
    puntaje_2 = multiplicador_2

# En caso de que el valor sea diferente a 0, 25 o 50 se procede a hacer una tirada [1,20]
# Y multiplicar la tirada con el multiplicador.
else:
    tiro_2 = random.randint(1,20)
    puntaje_2 = tiro_2 * multiplicador_2

# Dependiendo el valor del tiro se le asigna el color en el tablero rojo o verde y blanco o negro y fuera.
if multiplicador_2 == 0:
    color_2 = 0
elif multiplicador_2 == 25:
    color_2 = 5
elif multiplicador_2 == 50:
    color_2 = 6
elif multiplicador_2 == 1:
    if tiro_2 == 1 or tiro_2 == 4 or tiro_2 == 6 or tiro_2 == 15 or tiro_2 == 17 or tiro_2 == 19 or tiro_2 == 16 or tiro_2 == 11 or tiro_2 == 9 or tiro_2 == 5:
        color_2 = 2
    else:
        color_2 = 1
elif multiplicador_2 == 2:
    if tiro_2 == 1 or tiro_2 == 4 or tiro_2 == 6 or tiro_2 == 15 or tiro_2 == 17 or tiro_2 == 19 or tiro_2 == 16 or tiro_2 == 11 or tiro_2 == 9 or tiro_2 == 5:
        color_2 = 3
    else:
        color_2 = 4
elif multiplicador_2 == 3:
    if tiro_2 == 1 or tiro_2 == 4 or tiro_2 == 6 or tiro_2 == 15 or tiro_2 == 17 or tiro_2 == 19 or tiro_2 == 16 or tiro_2 == 11 or tiro_2 == 9 or tiro_2 == 5:
        color_2 = 33
    else:
        color_2 = 43

if color_2 == 0:
    print("\tCayó fuera.")
elif color_2 == 1:
    print("\tValor de tiro: ", tiro_2,"\n\tColor: Negro\n\tMultiplica: NO")
elif color_2 == 2:
    print("\tValor de tiro: ", tiro_2,"\n\tColor: Blanco\n\tMultiplica: NO")
elif color_2 == 3:
    print("\tValor de tiro: ", tiro_2,"\n\tColor: Verde\n\tMultiplica: Doble\n\tPuntaje Total: ", puntaje_2)
elif color_2 == 4:
    print("\tValor de tiro: ", tiro_2,"\n\tColor: Rojo\n\tMultiplica: Doble\n\tPuntaje Total: ", puntaje_2)
elif color_2 == 33:
    print("\tValor de tiro: ", tiro_2,"\n\tColor: Verde\n\tMultiplica: Triple\n\tPuntaje Total: ", puntaje_2)
elif color_2 == 43:
    print("\tValor de tiro: ", tiro_2,"\n\tColor: Rojo\n\tMultiplica: Triple\n\tPuntaje Total: ", puntaje_2)
elif color_2 == 5:
    print("\tValor de tiro: ", puntaje_2,"\n\tColor: Verde\n\tMultiplica: NO")
elif color_2 == 6:
    print("\tValor de tiro: ", puntaje_2,"\n\tColor: Rojo\n\tMultiplica: NO")


# Tercer JUGADA
print("\nTercer tiro...\n")

# La semilla es un valor aleatorio float comprendido en intervalo [0,1).
semilla_3 = random.random()

# Suerte convierte la semilla en un valor entero entre [0,99].
suerte_3 = int(semilla_3 * 100)

# Dependiendo la suerte se asigna un multiplicador comprendido en [0,3] U [25] U [50].
if suerte_3 <= 15:
    multiplicador_3 = 0
elif 15 < suerte_3 < 88:
    multiplicador_3 = 1
elif 88 <= suerte_3 < 94:
    multiplicador_3 = 2
elif 94 <= suerte_3 < 96:
    multiplicador_3 = 3
elif 96 <= suerte_3 < 98:
    multiplicador_3 = 25
elif 98 <= suerte_3:
    multiplicador_3 = 50

# Si sale 0, 25 o 50 se asigna el puntaje directamente del multiplicador.
if multiplicador_3 == 0 or multiplicador_3 == 25 or multiplicador_3 == 50:
    puntaje_3 = multiplicador_3

# En caso de que el valor sea diferente a 0, 25 o 50 se procede a hacer una tirada [1,20]
# Y multiplicar la tirada con el multiplicador.
else:
    tiro_3 = random.randint(1,20)
    puntaje_3 = tiro_3 * multiplicador_3

# Dependiendo el valor del tiro se le asigna el color en el tablero rojo o verde y blanco o negro y fuera.
if multiplicador_3 == 0:
    color_3 = 0
elif multiplicador_3 == 25:
    color_3 = 5
elif multiplicador_3 == 50:
    color_3 = 6
elif multiplicador_3 == 1:
    if tiro_3 == 1 or tiro_3 == 4 or tiro_3 == 6 or tiro_3 == 15 or tiro_3 == 17 or tiro_3 == 19 or tiro_3 == 16 or tiro_3 == 11 or tiro_3 == 9 or tiro_3 == 5:
        color_3 = 2
    else:
        color_3 = 1
elif multiplicador_3 == 2:
    if tiro_3 == 1 or tiro_3 == 4 or tiro_3 == 6 or tiro_3 == 15 or tiro_3 == 17 or tiro_3 == 19 or tiro_3 == 16 or tiro_3 == 11 or tiro_3 == 9 or tiro_3 == 5:
        color_3 = 3
    else:
        color_3 = 4
elif multiplicador_3 == 3:
    if tiro_3 == 1 or tiro_3 == 4 or tiro_3 == 6 or tiro_3 == 15 or tiro_3 == 17 or tiro_3 == 19 or tiro_3 == 16 or tiro_3 == 11 or tiro_3 == 9 or tiro_3 == 5:
        color_3 = 33
    else:
        color_3 = 43

if color_3 == 0:
    print("\tCayó fuera.")
elif color_3 == 1:
    print("\tValor de tiro: ", tiro_3,"\n\tColor: Negro\n\tMultiplica: NO")
elif color_3 == 2:
    print("\tValor de tiro: ", tiro_3,"\n\tColor: Blanco\n\tMultiplica: NO")
elif color_3 == 3:
    print("\tValor de tiro: ", tiro_3,"\n\tColor: Verde\n\tMultiplica: Doble\n\tPuntaje Total: ", puntaje_3)
elif color_3 == 4:
    print("\tValor de tiro: ", tiro_3,"\n\tColor: Rojo\n\tMultiplica: Doble\n\tPuntaje Total: ", puntaje_3)
elif color_3 == 33:
    print("\tValor de tiro: ", tiro_3,"\n\tColor: Verde\n\tMultiplica: Triple\n\tPuntaje Total: ", puntaje_3)
elif color_3 == 43:
    print("\tValor de tiro: ", tiro_3,"\n\tColor: Rojo\n\tMultiplica: Triple\n\tPuntaje Total: ", puntaje_3)
elif color_3 == 5:
    print("\tValor de tiro: ", puntaje_3,"\n\tColor: Verde\n\tMultiplica: NO")
elif color_3 == 6:
    print("\tValor de tiro: ", puntaje_3,"\n\tColor: Rojo\n\tMultiplica: NO")

# La ejecucion se detiene hasta precionar enter.
input("\nContinuar...\n")

# Se suma todos los puntajes para obtener el puntaje final.
puntaje_final = (puntaje_1 + puntaje_2 + puntaje_3)

if puntaje_final <=10:
    print("El puntaje final es: ", puntaje_final)
    print(nombre_jugador, "deberías dedicarse a otra cosa.")
elif 10 < puntaje_final < 50:
    print("El puntaje final es: ", puntaje_final)
    print(nombre_jugador, "tendrías que practicar más.")
elif 50 <= puntaje_final < 100:
    print("El puntaje final es: ", puntaje_final)
    print(nombre_jugador, "vas por buen camino.")
elif 100 <= puntaje_final < 180:
    print("El puntaje final es: ", puntaje_final)
    print(nombre_jugador, "genio!!!")
elif 180 == puntaje_final:
    print("El puntaje final es: ", puntaje_final)
    print(nombre_jugador, "master of the Universe.")

# Se comparan las tres JUGADAS para saber cual fue la que mayor puntaje obtuvo.
if puntaje_1 > puntaje_2 and puntaje_1 > puntaje_3:
    tirada_mayor = puntaje_1
elif puntaje_2 > puntaje_3:
    tirada_mayor = puntaje_2
else:
    tirada_mayor = puntaje_3
print("Tu mejor puntaje fue: ", tirada_mayor, "☺")
print("Fin del juego. :(")
print("\nAutores Muser Tomás y Perea Ivonne.")
input("Salir...")
