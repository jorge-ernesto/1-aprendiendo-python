"""
Ejercicio 9. Hacer un programa que pida numeros al usuario
indefinidamente hasta meter el numero 111
"""

contador = 0
contador_intento = 0
while contador < 1:
    numero = int(input("Ingrese un numero: "))

    if numero == 111:
        contador = contador + 1
        break
    else:
        contador_intento = contador_intento + 1
        print(f"Has introducido el: {numero}, es tu intento numero: {contador_intento}")
