# Desde el paquete "paqueteUsuarios" importamos el modulo "conexion"
import paqueteUsuarios.conexion as conexion

# Importamos modulo de Python datetime
import datetime

# Importamos modulo para encriptar contraseñas
import hashlib

# Obtenemos variables de conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


class Usuario:
    # Constructor
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    # Metodos magicos en Python
    # https://www.tutorialsteacher.com/python/magic-methods-in-python
    # Imprimir un objeto en Python con "__repr__"
    # https://es.stackoverflow.com/questions/311450/como-puedo-imprimir-una-lista-de-objetos-objetos-de-clase-en-python
    def __repr__(self):
        return str(self.__dict__)

    def registrar(self):
        # Preparamos insert
        sql = "INSERT INTO usuarios VALUES (null, %s, %s, %s, %s, %s)"

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode("utf8"))  # El metodo update recibe un byte
        password_cifrado = (
            cifrado.hexdigest()
        )  # Obtenemos el string hexadecimal del cifrado que genero la libreria

        # Obtenemos fecha
        fecha = datetime.datetime.now()

        # Obtenemos datos
        usuario = (self.nombre, self.apellidos, self.email, password_cifrado, fecha)

        # Ejecutamos insert
        # Capturamos error provocado por la restriccion de llave unica del campo "email" de la tabla "usuarios"
        # Este error ocurre cuando se intenta registrar un correo ya existente
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [
                cursor.rowcount,
                self,
            ]  # Cantidad de registros o filas que han sido afectadas y el objeto que hayamos guardado
        except:
            result = [0, self]

        # print("result registrar:", result)
        return result

    def identificar(self):
        # Preparamos select
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode("utf8"))  # El metodo update recibe un byte
        password_cifrado = (
            cifrado.hexdigest()
        )  # Obtenemos el string hexadecimal del cifrado que genero la libreria

        # Obtenemos datos
        usuario = (self.email, password_cifrado)

        # Ejecutamos select
        # Solo puede traer un unico registro por la restriccion de llave unica del campo "email" de la tabla "usuarios"
        # Si no se encuentra registro, result es None
        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        # print("result identificar:", result)
        return result
