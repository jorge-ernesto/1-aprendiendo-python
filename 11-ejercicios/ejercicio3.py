""" 
Ejercicio 3. Programa que compruebe si una variable está vacia
y si está vacia, rellenar con texto en minuscula y mostrarlo
en mayusculas.
"""

texto = ""

if len(texto.strip()) <= 0:
    texto = "hola soy un texto en minuscula"
    print(texto.upper())
else:
    print("La variable tiene contenido")
