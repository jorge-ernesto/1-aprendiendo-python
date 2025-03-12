# Importamos clase "Coche", "from coche" es el archivo en si e "import Coche" es la clase la cual importamos
from coche import Coche

carro = Coche("Renault", "Clio", "Amarillo", 150, 200, 4)
carro1 = Coche("Seat", "Panda", "Verde", 250, 200, 4)
carro2 = Coche("Citroen", "Xara", "Azul", 100, 180, 4)
carro3 = Coche("Mercedes", "Clase A", "Rojo", 350, 400, 4)

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# Detectar tipado
print("\n---- Detectar tipado ----")
print(type(carro3))
# carro3 = "Valor aleatorio"
# print(type(carro3))
if type(carro3) == Coche:
    print("Es un objeto correcto")
else:
    print("No es un objeto")

# Visibilidad
print("\n---- Visibilidad ----")
print(carro.soy_publico)
# print(carro.__soy_privado)
print(carro.getPrivado())
