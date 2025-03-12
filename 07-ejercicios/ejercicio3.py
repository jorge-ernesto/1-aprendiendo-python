"""
Ejercicio 3. Escribir un programa que muestre los cuadrados
(un numero multiplicado por si mismo) de los 60 primeros numeros
naturales. Resolver con for y con while
"""

for i in range(1, 61):
    print("El cuadrado de", i, "es", i**2)

print("----------------------------------------------")

contador = 1
while contador <= 60:
    print("El cuadrado de", contador, "es", contador**2)
    contador += 1
