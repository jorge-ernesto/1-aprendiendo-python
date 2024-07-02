"""
Ejercicio 2. Escribir un script que nos muestre por pantalla 
todos los numeros pares entre 1 y 100.
"""

rango = range(1, 101);

for i in rango:
    if (i % 2 == 0): # Operacion de resto, para validar que no lo haya, es decir que sea par
        print(i);
    