# Capturar excepcion y manejar errores en código
# Susceptible a fallos/errores

"""
try:
    nombre = input("¿Cual es tu nombre?: ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre
        
    print(nombre_usuario)
except:
    print("Ha ocurrido un error: Mete bien el nombre")
else:
    print("Todo ha funcionado correctamente")
finally:
    print("Fin de la iteración !!") 
"""

# Realizar multiples excepciones
"""
try:
    numero = int(input("Numero para elevarlo al cuadrado: "))
    print("El cuadrado es " + str(numero*numero))
# except ValueError:
#     print("Debe ingresar un entero")
# except TypeError:
#     print("Debe convertir tu cadena a entero en el codigo")
except Exception as e:    
    print(type(e))        
    print("Ha ocurrido un error:", type(e).__name__) #Obtenemos el tipo de dato y mostramos la constante con "__name__". type(e).__name__, debe mostrar "ValueError" o "TypeError"
"""

# Realizar excepciones personalizadas o lanzar excepcion
try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es correcta")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completa")
    else:
        print(f"Bienvenido al Maste en Python {nombre}!!")
# except ValueError:
#     print("Introduce los datos correctamente")
except Exception as e:
    print("Existe un error:", e)
