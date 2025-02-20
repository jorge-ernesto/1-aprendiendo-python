def holaMundo(nombre):
    return f"Hola que tal estas, {nombre}"


def calculadora(numero1, numero2, basicas=False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    """
    cadena += f"Suma {suma}\n"
    cadena += f"Resta {resta}\n"
    cadena += f"Multiplicacion {multi}\n"
    cadena += f"Division {division}"
    """

    if basicas == True:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "Division: " + str(division)
        cadena += "\n"
    return cadena
