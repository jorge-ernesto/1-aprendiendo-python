"""
Modulo: Son funcionalidades ya hechas para reutilizar.

En python hay muchos modulos, que los puedes consultar aquí:
https://docs.python.org/es/3/py-modindex.html

Podemos conseguir modulos que ya vienen en el lenguaje,
modulos en internet, y tambien podemos crear nuestros modulos
"""

"""
Modulo: Un modulo en Python es una forma de empaquetar nuestro codigo,
en un modulo o lo que se conoce en otros lenguajes como librerias,
para reutilizar esas funcionalidades tantas veces como necesitemos y
en cualquier parte del programa

Instalar modulos en Python
Buscamos en Google: "python modules index"
https://docs.python.org/es/3/py-modindex.html
"""

print("\n################## IMPORTAMOS MODULOS ##################")
# IMPORT MODULO PROPIO
"""
import mimodulo
print(mimodulo.holaMundo("Ernesto"))
print(mimodulo.calculadora(3, 7, False))
"""

# IMPORT FUNCION DEL MODULO PROPIO
"""
from mimodulo import holaMundo
print(holaMundo("Ernesto"))
"""

# IMPORT MODULO PROPIO, USO DE ALIAS
"""
import mimodulo as mmod
print(mmod.holaMundo("Ernesto"))
print(mmod.calculadora(3, 7, False))
"""

# IMPORT TODAS LAS FUNCIONES DEL MODULO PROPIO
from mimodulo import *

print(holaMundo("Ernesto"))
print(calculadora(3, 7, False))

# MODULO FECHAS
print("\n################## MODULO FECHAS ##################")
import datetime

print(datetime.date.today())  # Fecha en formato YYYY-MM-DD

fecha_completa = datetime.datetime.now()  # Fecha en formato YYYY-MM-DD hh:mm:ss.ffffff
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime(
    "%d/%m/%Y %H:%M:%S"
)  # Fecha en formato DD/MM/YYYY hh:mm:ss
print(f"Mi fecha personalizada es {fecha_personalizada}")

print(datetime.datetime.now().timestamp())  # Fecha en formato timestamp
print(datetime.datetime.now().time())  # Fecha en formato hh:mm:ss

# MODULO MATEMATICAS
print("\n################## MODULO MATEMATICAS ##################")
import math

print("Raiz cuadrada de 16:", math.sqrt(16))
print("Numero pi:", float(math.pi))
print("Redondear:", math.ceil(6.56789))  # Redondear al alsa
print("Redondear:", math.floor(6.56789))  # Redondear a la baja

# MODULO RANDOM
print("\n################## MODULO RANDOM ##################")
import random

print("Numero aleatorio entre 15 y 67:", random.randint(15, 67))
