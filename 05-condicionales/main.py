"""
# Conficional IF

SI se_cumpl_esta_conficion:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecuta otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones

# Operadores de comparacion
== igual 
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# Operadores logicos
and y 
or  O
!   NEGACION
not NO
"""

print("############# EJEMPLO 1 #############")

color = "rojo"
# color = "rojo ".strip()
# color = input("Adivina cual es mi color favorito: ").strip()

if color == "rojo":
    print("El color es ROJO")
else:
    print("El color NO es ROJO")

# Ejemplo 2
print("\n############# EJEMPLO 2 #############")

year = 2020
# year = int(input("¿En que año estamos? "))

if year >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("Es un año anterior a 2021")

# Ejemplo 3
print("\n############# EJEMPLO 3 #############")

nombre = "Victor Robles"
ciudad = "Barcelona"
continente = "Europa"
edad = 55
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")

    if continente == "Europa":
        print("Vive en un continente europeo")
    else:
        print("Vive en un continente no europeo")
else:
    print(f"{nombre} es menor de edad")

# Ejemplo 4
print("\n############# EJEMPLO 4 #############")

dia = 1
# dia = int(input("¿Que dia es hoy? "))

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
elif dia == 6:
    print("Es sabado")
elif dia == 7:
    print("Es domingo")
else:
    print("No es un dia de la semana")

# Ejemplo 5
print("\n############# EJEMPLO 5 #############")

edad_minima = 18
edad_maxima = 65
edad_oficial = 17
# edad_oficial = int(input("¿Que edad tienes? "))

if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
    print("Puedes votar")
else:
    print("No puedes votar")

# Ejemplo 6
print("\n############# EJEMPLO 6 #############")

pais = "España"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana")

# Ejemplo 7
print("\n############# EJEMPLO 7 #############")

pais = "España"

# Si pais no es igual a España, entonces no es un pais de habla hispana
# Con el not lo negamos, es decir no debe ser un pais de habla hispana, es decir evalua que sea FALSE para que entre en la condicional
if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} no es un pais de habla hispana")
else:
    print(f"{pais} es un pais de habla hispana")

# Ejemplo 8
print("\n############# EJEMPLO 8 #############")

pais = "USA"

# Si pais es diferente a Mexico, si pais es diferente de España, si pais es diferente de Colombia, entonces no es un pais de habla hispana
if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} no es un pais de habla hispana")
else:
    print(f"{pais} es un pais de habla hispana")
