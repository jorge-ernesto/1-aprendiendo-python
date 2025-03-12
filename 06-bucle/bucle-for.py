# BUCLE FOR
"""
# FOR
for variable in elemento_iterable (lista, rango, etc):
    BLOQUE DE INSTRUCCIONES
"""

contador = 0
resultado = 0

for contador in range(0, 5):
    print("Voy por el numero: " + str(contador))
    resultado += contador

print("El resultado es: " + str(resultado))

print("----------------------------------------------")

# EJEMPLO DE TABLAS DE MULTIPLICAR
# Se puede utilizar un else en el for, esto  no lo tienen otros lenguajes de programación, cuando termina la iteraccion muestra el else

numero_usuario = int(input("¿De que número quieres la tabla?: "))
if numero_usuario < 1:
    numero_usuario = 1
print(f"\nTabla del {numero_usuario}")

for numero in range(1, 11):

    if numero_usuario == 45:
        print("No se puede mostrar numeros prohibidos")
        break

    print(
        str(numero_usuario) + " x " + str(numero) + " = " + str(numero_usuario * numero)
    )
else:
    print("Tabla finalizada")
