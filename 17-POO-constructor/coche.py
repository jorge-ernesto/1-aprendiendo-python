class Coche:
    # Atributos o propiedades (variables)
    # Caracteristicas del coche
    marca = "Ferrari"
    modelo = "Avenador"
    color = "Rojo"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Otros atributos
    soy_publico = "Hola, soy un atributo publico"
    __soy_privado = "Hola, soy un atributo privado"

    # Constructor de la clase
    def __init__(self, marca, modelo, color, velocidad, caballaje, plazas):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    # Metodos para otros atributos
    def getPrivado(self):
        return self.__soy_privado

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

    def getVelocidad(self):
        return self.velocidad

    def setVelocidad(self, velocidad):
        self.velocidad = velocidad

    def getCaballaje(self):
        return self.caballaje

    def setCaballaje(self, caballaje):
        self.caballaje = caballaje

    def getPlazas(self):
        return self.plazas

    def setPlazas(self, plazas):
        self.plazas = plazas

    # Metodo general que obtenga toda la informacion del coche
    def getInfo(self):
        info = "---- Informacion del coche ----"
        info += "\nMarca: " + self.getMarca()
        info += "\nModelo: " + self.getModelo()
        info += "\nColor: " + self.getColor()
        info += "\nVelocidad: " + str(self.getVelocidad())
        info += "\nCaballaje: " + str(self.getCaballaje())
        info += "\nPlazas: " + str(self.getPlazas())
        return info

    # Otros metodos
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
