""" 
Diccionario:
Un tipo de dato que almacena un conjunto de datos.
En forma clave > valor.
Es parecido a un array asociativo o un objeto json.
"""

# DICCIONARIOS
print("\n****************************** DICCIONARIOS ******************************")
persona = {"nombre": "Victor", "apellidos": "Robles", "web": "victoroblesweb.es"}

print(type(persona))
print(persona)
print(persona["apellidos"])

# LISTA CON DICCIONARIOS
print(
    "\n****************************** LISTA CON DICCIONARIOS ******************************"
)
contactos = [
    {
        "nombre": "Victor",
        "apellidos": "Robles",
        "email": "victorobles@victorrobles.com",
    },
    {"nombre": "Ernesto", "apellidos": "Si", "email": "ernesto@ernesto.com"},
    {"nombre": "Liliana", "apellidos": "Si", "email": "liliana@liliana.com"},
]

print(type(contactos))
print(contactos)
print(contactos[0]["nombre"])

print(
    "\n****************************** LISTADO DE CONTACTOS ******************************"
)

print("-----------------------------------")
for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("-----------------------------------")
