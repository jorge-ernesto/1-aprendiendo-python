# HERENCIA: Es la posibilidad de compartir atributos y metodos
# entre clases. Y que diferentes clases hereden de otras


class Persona:
    """
    Atributos que tendra la clase:
    - nombre
    - apellidos
    - altura
    - edad
    """

    # Metodos getters y setters basicos
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getApellidos(self):
        return self.apellidos

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def getAltura(self):
        return self.altura

    def setAltura(self, altura):
        self.altura = altura

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    # Otros metodos
    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "Estoy durmiendo"


class Informatico(Persona):
    """
    Atributos o propiedades que tendra la clase:
    - lenguajes
    - experiencia
    """

    def __init__(self):
        self.lenguajes = "HTML, CSS, JavaScript, PHP"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "Estoy programando"

    def repararPC(self):
        return "He reparado tu ordenador"


class TecnicoRedes(Informatico):

    def __init__(self):
        """
        El constructor de la clase "Informatico" no se ejecuta en la clase "TenicoRedes", es decir:
        - El constructor no se ejecuta en las clases hijos, en las clases que heredan, el constructor es exclusivo de cada clase.
        - Si queremos copiar el constructor y heredarlo tambien, debemos usar la funcion "super().__init__()"
        """
        super().__init__()
        self.auditarRedes = "experto"
        self.experienciaRedes = 15

    def auditoria(self):
        return "Estoy auditando una red"
