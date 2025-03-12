""" 
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico
nombre.
Para acceder a esos valores podemos usar un indice númerico
"""

pelicula = "Batman"

# DEFINIR LISTA
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(
    ("2pac", "Drake", "Jennifer Lopez")
)  # Le pasamos una tupla (no modificable) a la funcion list, para convertirla en lista
years = list(range(2020, 2050))
variada = ["Victor", 30, 4.4, True, "Texto"]

"""
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""

# INDICES
print(peliculas[0])
print(peliculas[-1])
print(cantantes[0:2])
print(peliculas[1:])

# MODIFICAR ELEMENTOS DE LISTA
pelicula = "Otra pelicula"
peliculas[1] = "Gran Torino"
print(peliculas)

# AÑADIR ELEMENTOS A LISTA
cantantes.append("Kase O")
cantantes.append("Natos y waor")
print(cantantes)

# RECORRER LISTA
print(
    "\n****************************** LISTA DE PELICULAS ******************************"
)

"""
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)
"""

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")

# LISTA MULTIDIMENCIONAL
print(
    "\n****************************** LISTADO DE CONTACTOS ******************************"
)
contactos = [
    ["Antoinio", "antonio@antonio.com"],
    ["Luis", "luis@luis.com"],
    ["Salvador", "salvador@salvador.com"],
]
# print(contactos)

for contacto in contactos:
    print(contacto[0] + ": " + contacto[1])

# for contacto in contactos:
#     for elemento in contacto:
#         if contacto.index(elemento) == 0:
#             print("Nombre: " + elemento)
#         else:
#             print("Email: " + elemento)
#     print("\n")
