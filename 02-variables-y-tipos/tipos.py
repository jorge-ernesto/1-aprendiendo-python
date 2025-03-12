# TIPOS DE DATOS EN PYTHON
nada = None  # Parecido a NULL
cadena = "Hola"
cadena = "Desarrollador web"
entero = 99
flotante = 4.2
booleano = True  # True o False, es sensitivo a mayusculas y minusculas
lista = [10, 20, 30, 100, 200]
listaString = [44, "treinta", 30, "cuarenta"]
tuplaNoCambia = ("master", "en", "python")
diccionario = {"nombre": "Juan", "apellido": "Perez", "curso": "Master en Python"}
rango = range(9)
dato_byte = b"Probando"

# imprimir varible y el tipo de dato
print(lista)
print(type(lista))

print(tuplaNoCambia)
print(type(tuplaNoCambia))

print(diccionario)
print(type(diccionario))

print(rango)
print(type(rango))

# imprimir varible y el tipo de dato
print(dato_byte)
print(type(dato_byte))

# CONVERTIR UN TIPO DE DATO A OTRO
texto = "Hola soy un texto"
numerito = str(776)
print(texto + " " + numerito)
print(type(numerito))

numerito = int(776)
print(type(numerito))

numerito = float(776)
print(type(numerito))
