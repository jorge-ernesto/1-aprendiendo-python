import os
import shutil

# VERIFICAMOS RUTA
ruta = os.path.abspath("./mi_carpeta")
print("\n")
print("RUTA:", ruta)

# CREAR CARPETA
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe directorio")

# COPIAR CARPETA
"""
ruta_original    = "./mi_carpeta"
ruta_nueva       = "./mi_carpeta_COPIADA"
shutil.copytree(ruta_original, ruta_nueva)
"""

# ELIMINAR CARPETA
"""
# os.rmdir("./mi_carpeta_COPIADA")
"""

# LISTAR CONTENIDO DE CARPETA
print("\n")
print("Contenido de mi carpeta")
contenido = os.listdir("./mi_carpeta")
print(contenido)

for fichero in contenido:
    print("Fichero:", fichero)
