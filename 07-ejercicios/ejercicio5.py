"""
Ejercicio 5. Hacer un programa que muestre todos los numeros entre
dos numeros que diga el usuario.
"""

numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))

if numero1 < numero2:
    for contador in range(numero1, (numero2 + 1)):
        print(contador)
else:
    print("El número 1 debe ser menor al numero 2")
