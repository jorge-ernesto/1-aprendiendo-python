# Importamos modulo que nos permite trabajar con MySQL dentro de Python
import mysql.connector


def conectar():
    # Conexion
    conexion = mysql.connector.connect(
        host="localhost", user="root", password="", database="master_python", port=3306
    )

    # Creamos cursor
    cursor = conexion.cursor(
        buffered=True
    )  # El parametro nos permitira hacer muchas consultas usando el mismo cursor

    # Retornamos conexion y cursor
    return [conexion, cursor]
