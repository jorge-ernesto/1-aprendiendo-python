"""
Variables locales: Se definen dentro de la función y no
se puede usar fuera de ella, solo están disponibles dentro.
A no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de una funcion
y estan disponibles dentro y fuera de ellas.
"""

# Variable global
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"
print(frase)


def holaMundo():
    # Variable local
    # frase = "Hola mundo!!"
    print(frase)

    # Variable local
    year = 2021
    print(year)

    # Variable global
    global website
    website = "jorgeernestoweb"
    print("DENTRO", website)

    # Retornamos dato
    return "Dato devuelto: " + str(year)


# Imprimimos variable local devuelta por return en la funcion
data_year = holaMundo()
print(data_year)

# Imprimimos variable global declarada en la funcion
print("FUERA", website)
