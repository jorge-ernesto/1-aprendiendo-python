import pathlib  # pathlib es un modulo
import shutil  # shutil es un modulo
import os  # os es un modulo

print(
    "\n################################### ABRIR FICHEROS ###################################"
)

# OBTENEMOS RUTA
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
print("RUTA:", ruta)

# CREAMOS Y ABRIMOS ARCHIVO
archivo = open(ruta, "a+")  # Open actua como funcion predefinida

# ESCRIBIR ARCHIVO
archivo.write("*************** Soy un texto metido desde Python ***************\n")

# CERRAR ARCHIVO
archivo.close()

print(
    "\n################################### CREAR FICHEROS ###################################"
)

# ABRIR
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

# LEER CONTENIDO
# contenido = archivo_lectura.read()
# print(contenido)

# LEER CONTENIDO Y GUARDAR EN LISTA
lista = archivo_lectura.readlines()
# for frase in lista:
#     if not frase.isnumeric():
#         print("- "+frase.upper())

for frase in lista:
    lista_frase = frase.split()
    print(lista_frase)

# for frase in lista:
#     print(frase.center(100))

archivo_lectura.close()

print(
    "\n################################### COPIAR ARCHIVOS ###################################"
)
# COPIAR
"""
ruta_original    = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva       = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_alternativa = str(pathlib.Path().absolute()) + "/../07-ejercicios/fichero_copiado77.txt"

shutil.copyfile(ruta_original, ruta_nueva)
shutil.copyfile(ruta_original, ruta_alternativa)
"""

print(
    "\n################################### MOVER ARCHIVOS ###################################"
)
# MOVER
"""
ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva    = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"

shutil.move(ruta_original, ruta_nueva)
"""

print(
    "\n################################### ELIMINAR ARCHIVOS ###################################"
)
# ELIMINAR
"""
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"
os.remove(ruta_nueva)
"""

# COMPROBAR SI EXISTE ARCHIVO
import os.path

print(os.path.abspath("./"))
ruta_comprobar = os.path.abspath("./") + "/fichero_texto.txt"
print(ruta_comprobar)

if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
else:
    print("El archivo no existe")
