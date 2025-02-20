cantantes = ["2pac", "Drake", "Bad Bunny", "Julio Ingleias"]
numeros = [1, 2, 5, 8, 3, 4]

# ORDENAR UNA LISTA
print("Numeros:", numeros)
numeros.sort()
print("Numeros:", numeros)

# print("Cantantes:", cantantes)
# cantantes.sort()
# print("Cantantes:", cantantes)

# AÑADIR ELEMENTOS
cantantes.append("Natos y Waor")
cantantes.insert(0, "David Bisbal")
print("Cantantes:", cantantes)

# ELIMINAR ELEMENTOS
cantantes.pop(1)
cantantes.remove("Bad Bunny")
print("Cantantes:", cantantes)

# DAR LA VUELTA
numeros.reverse()
print("Numeros:", numeros)

# BUSCAR DENTRO DE UNA LISTA
print("Drake" in cantantes)
print("Drake2" in cantantes)

# CONTAR ELEMENTOS
print("Cantantes:", cantantes)
print("Leargo Cantantes:", len(cantantes))

# CANTIDAD DE VECES QUE APARECE UN ELEMENTO
numeros.append(8)
print("Cantidad de veces que aparece un elemento:", numeros.count(8))

# CONSEGUIR INDICE
print("Conseguir indice:", cantantes.index("Drake"))

# UNIR LISTAS
cantantes.extend(numeros)
print("Unir listas:", cantantes)
