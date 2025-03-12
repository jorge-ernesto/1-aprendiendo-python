"""
Paquete: Un paquete es un conjunto de modulos,
para crear un paquete necesitamos crear en un repositorio, un archivo llamado "__init__.py",
con ese archivo le indicamos a Python que es un paquete, es decir que es una agrupación de módulos

Instalar paquetes en Python
https://pypi.org/
"""

print("PROBANDO PAQUETES:")

from mipaquete import pruebas, herramientas

pruebas.probando()
herramientas.nombreCompleto("Ernesto", "Si")
