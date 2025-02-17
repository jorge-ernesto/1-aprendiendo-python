# Programacion orientada a objetos (POO o OOP)


# Definir una clase (molde para crear mas objetos de este tipo)
# (Coche) con caracteristicas similares
class Coche:
    # Atributos o propiedades (variables)
    # Caracteristicas del coche
    marca = "Ferrari"
    modelo = "Avenador"
    color = "Rojo"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Metodos getters y setters, son acciones que hace el objeto (coche) (funciones)
    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getModelo(self):
        return self.modelo

    def setModelo(self, modelo):
        self.modelo = modelo

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    # Otros metodos
    def getVelocidad(self):
        return self.velocidad

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1


# COCHE 1
print("-------------------------------")
print("COCHE 1")

# Crear objetos / Instanciar la clase
coche = Coche()
coche.setModelo("Murcielago")
coche.setColor("amarillo")
print(coche.getMarca(), coche.getModelo(), coche.getColor())
print("Velocidad actual: ", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()
print("Velocidad nueva: ", coche.getVelocidad())

# COCHE 2
print("-------------------------------")
print("COCHE 2")

# Crear mas objetos
coche2 = Coche()
coche2.setModelo("Gallargo")
coche2.setColor("Verde")
print(coche2.getMarca(), coche2.getModelo(), coche2.getColor())
print(type(coche), type(coche2))
