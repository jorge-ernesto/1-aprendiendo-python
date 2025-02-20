""" 
FUNCIONES: 
Una función es un conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarse invocando a
la función tantas veces como sea necesario.

def nombreDeMiFuncion(parametros):
    # BLOQUE / CONJUNTO DE INTRUCCIONES
    
nombreDeMiFuncion(mi_parametro)
nombreDeMiFuncion(mi_parametro)
"""

############################### Ejemplo 1 ###############################
print("\n########### EJEMPLO 1 ###########")


# Definir funcion
def muestraNombre():
    print(f"Victoria")


# Invocar funcion
muestraNombre()

############################### Ejemplo 2: Parametros ###############################
mostrar2 = False
if mostrar2:
    print("\n########### EJEMPLO 2 ###########")

    def mostrarTuNombre(nombre):
        print(f"Tu nombre es: {nombre}")

    nombre = input("Ingresa tu nombre: ")
    mostrarTuNombre(nombre)

############################### Ejemplo 3 ###############################
mostrar3 = False
if mostrar3:
    print("\n########### EJEMPLO 3 ###########")

    def tabla(numero):
        print(f"Tabla de multiplicar del numero {numero}")

        for contador in range(1, 11):
            operacion = numero * contador
            print(f"{numero} x {contador} = {operacion}")
        print("\n")

    numero = int(input("Ingrese numero para tabla de multiplicar: "))
    tabla(numero)

############################### Ejemplo 3.1 ###############################
if mostrar3:
    print("\n########### EJEMPLO 3.1 ###########")
    for numero_tabla in range(1, 11):
        tabla(numero)

############################### Ejemplo 4: Parametros opcionales ###############################
print("\n########### EJEMPLO 4 ###########")


def getEmpleado(nombre, dni=None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")

    if dni != None:
        print(f"DNI: {dni}")


getEmpleado("Ernesto")

############################### Ejemplo 5: Parametros opcionales y return o devolver datos ###############################
print("\n########### EJEMPLO 5 ###########")


def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    return saludo


print(saludame("Ernesto"))

############################### Ejemplo 6 ###############################
print("\n########### EJEMPLO 6 ###########")


def calculadora(numero1, numero2, basicas=False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    """
    cadena += f"Suma {suma}\n"
    cadena += f"Resta {resta}\n"
    cadena += f"Multiplicacion {multi}\n"
    cadena += f"Division {division}"
    """

    if basicas == True:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "Division: " + str(division)
        cadena += "\n"
    return cadena


print(calculadora(2, 3, True))

############################### Ejemplo 7 ###############################
print("\n########### EJEMPLO 7 ###########")


def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto


def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto


def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto


print(devuelveTodo("Ernesto", "Si"))

############################### Ejemplo 8: Funciones Lambda ###############################
print("\n########### EJEMPLO 8 ###########")

dime_el_year = lambda year: f"El año es {year}"
print(dime_el_year(2022))
