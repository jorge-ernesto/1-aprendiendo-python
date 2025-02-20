"""
Ejercicio 1. Hacer un programa que tenga una lista 
de 8 numeros enteros y haga lo siguiente:
(hecho) - Recorrer la lista y mostrarla
(hecho) - Hacer funcion que recorra listas de numeros y devuelva un string
(hecho) - Ordenarla y mostrarla
(hecho) - Mostrar su longitud
(hecho) - Buscar algun elemento (que el usuario pida por teclado)
"""

# CREAR LA LISTA
from logging import exception


numeros = [13, 64, 52, 73, 21, 7, 91, 63]


def mostrarLista(lista):
    resultado = ""
    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"
    return resultado


# RECORRER Y MOSTRAR
print("\n############### Recorrer y mostrar ###############")
"""
for numero in numeros:
    print(numero)
"""

print(mostrarLista(numeros))
print(mostrarLista([1, 3, 7]))
print(mostrarLista(["victor", "juan", "pepe"]))

# ORDERNAR Y MOSTRAR
print("\n############### Ordenar y mostrar ###############")
print(mostrarLista(numeros))
numeros.sort()
print(mostrarLista(numeros))

# MOSTRAR LONGITUD
print("\n############### Mostrar Longitud ###############")
print(len(numeros))

# BUSCAR EN LA LISTA
print("\n############### Buscar en la lista ###############")
# Manejo de errores para la busqueda en la lista
try:
    # Pedimos numero al usuario y detectamos el tipado
    busqueda = int(input("Introduce el numero: "))
    comprobar = isinstance(busqueda, int)

    # Comprobamos que el usuario haya ingresado un numero entero y que numero sea mayor que 0
    while not comprobar or busqueda <= 0:
        busqueda = int(input("Introduce el numero: "))
        comprobar = isinstance(busqueda, int)
    else:
        print(f"Has introducido el {busqueda}")

    search = numeros.index(busqueda)
    print(f"El numero buscado existe en la lista, en el indice: {search}")
except:
    print("Ha ocurrido un error")
