"""
Proyecto Python y MySQL:
- Abrir un asistente
- Login o registro
- Si elegimos login, identifica al usuario y nos preguntara
- Crear notas, mostrar notas, borrarlas.
"""

# Desde el paquete "paqueteUsuarios" importamos el modulo "acciones"
from paqueteUsuarios import acciones

# Mostramos comandos disponibles
print(
    """
Acciones disponibles:
    - registro
    - login
"""
)

# Creamos el objeto "hazEl" (instanciamos la clase "Acciones")
hazEl = acciones.Acciones()

# Preguntamos accion a realizar
accion = input("¿Que quieres haces?: ")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()
