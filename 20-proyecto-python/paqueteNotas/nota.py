import paqueteUsuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


class Nota:
    def __init__(self, usuario_id, titulo, descripcion):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    # Metodos magicos en Python
    # https://www.tutorialsteacher.com/python/magic-methods-in-python
    # Imprimir un objeto en Python con "__repr__"
    # https://es.stackoverflow.com/questions/311450/como-puedo-imprimir-una-lista-de-objetos-objetos-de-clase-en-python
    def __repr__(self):
        return str(self.__dict__)

    def guardar(self):
        # Preparamos insert
        sql = f"""
        INSERT INTO notas (id, usuario_id, titulo, descripcion, fecha)
        VALUES (null, {self.usuario_id}, '{self.titulo}', '{self.descripcion}', NOW())
        """

        # Ejecutamos insert
        cursor.execute(sql)
        database.commit()
        result = [cursor.rowcount, self]

        # print("result guardar:", result)
        return result

    def listar(self):
        # Preparamos select
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"

        # Ejecutamos select
        cursor.execute(sql)
        result = cursor.fetchall()

        # print("result listar:", result)
        return result

    def eliminar(self):
        # Preparamos delete
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'"

        # Ejecutamos delete
        cursor.execute(sql)
        database.commit()
        result = [cursor.rowcount, self]

        # print("result delete:", result)
        return result
