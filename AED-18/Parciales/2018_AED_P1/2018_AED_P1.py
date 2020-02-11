# Se carga por teclado 4 números enteros.
print("""
Parcial de Algoritmos y Estructuras de Datos.
Curso 1K
Alumno: 
Legajo: 
""")

numero_primero = int(input("Ingrese el primer número entero: "))
numero_segundo = int(input("Ingrese el segundo número entero: "))
numero_tercero = int(input("Ingrese el tercer número entero: "))
numero_cuarto = int(input("Ingrese el cuarto número entero: "))


# Compara si el número primero es mayor a el número segundo y lo imprime. A su vez asigna a primer mayor al mayor entre ambos
if numero_primero > numero_segundo:
    print("El mayor entre los dos primeros números es: ", numero_primero)
    primer_mayor = numero_primero
# Caso contrario el segundo número es mayor y lo asgina a pa variable primer mayor e imprime el valor.
else:
    print("El mayor entre los dos primeros números es: ", numero_segundo)
    primer_mayor = numero_segundo

# Se suma el tercer y cuarto número.
suma_segundos = numero_tercero + numero_cuarto

# Verifica si la suma es igual al mayor entre los primero número e imprime en pantalla si es igual o NO.
if suma_segundos == primer_mayor:
    print("La suma del tercer y cuarto número SI es igual a el mayor de los dos primeros números.")
else:
    print("La suma del tercer y cuarto número NO es igual a el mayor de los dos primeros números.")

# Se compara el tercer y cuarto número para determinar el menor, y lo imprime en pantalla a su vez asigna el número a una variable.
if numero_tercero > numero_cuarto:
    print("El menor número entre el tercer y cuarto número es: ", numero_cuarto)
    segundo_menor = numero_cuarto
else:
    print("El menor número entre el tercer y cuarto número es: ", numero_tercero)
    segundo_menor = numero_tercero

resta_primeros = numero_primero - numero_segundo

# Determina si el menor entre el tercer y cuarto número es igual a la resta entre el primer número y el segundo número.
if segundo_menor == resta_primeros:
    print("La resta de los primeros números SI es igual al menor entre el primero y el segundo")
else:
    print("La resta de los primeros números NO es igual al menor entre el primero y el segundo")
