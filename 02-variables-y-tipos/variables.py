# VARIABLES EN PYTHON
# Esto es un comentario, se puede usar """ """ para imprimir varias lineas
"""
Una variable es un contenedor de informacion
que dentro guardará un dato, se pueden crear
muchas variables y que cada una tenga un dato distinto
"""

# Crear variables y asignarles un valor
texto = "Master en Python"
texto2 = "con Victor Robles"
numero = 45
decimal = 6.7

# Mostrar valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("------------------------------")

# Sustituir el valor de algunas variables / reasignado valores
numero = 77
decimal = 8.9
print(numero)
print(decimal)

print("------------------------------")

# CONCATENAR
nombre = "Víctor"
apellidos = "Robles"
web = "victorroblesweb.es"

print(nombre + " " + apellidos + " - " + web)
print(f"{nombre} {apellidos} - {web}")  # Interpolación de variables
print("Hola me llamo {} {} y mi web es {}".format(nombre, apellidos, web))
print(nombre, apellidos, web)
