nombre = "Victor Robles"

# FUNCIONES GENERALES
print(type(nombre))

# DETECTAR EL TIPADO
comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variable es un string")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

# LIMPIAR ESPACIOS
frase = "         mi contenido          "
print(frase)
print(frase.strip())

# ELIMINAR VARIABLES
year = 2022
print(year)
del year
# print(year) # Los errores detienen la instruccion del script

# COMPROBAR VARIABLE VACIA
texto = " ff "
if len(texto) <= 0:
    print("La variable esta vacia")
else:
    print("La variable tiene contenido con largo de:", len(texto))

# ENCONTRARA CARACTERES
frase = "La vida es bella"
palabra = "vida"
print(
    "La palabra",
    f'"{palabra}"',
    "se encuentra a partir del caracter",
    frase.find("vida"),
)

# REEMPLAZAR VARIABLES EN UN STRING
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

# MAYUSCULAS Y MINUSCULAS
print(nombre)
print(nombre.lower())
print(nombre.upper())
