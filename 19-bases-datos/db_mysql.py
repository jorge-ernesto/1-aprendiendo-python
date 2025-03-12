"""
En Python debemos instalar el modulo de MySQL, no viene por defecto como SQLite
Instalamos módulo de MySQL
    - Buscar en Google: "mysql connector python"
    - Entramos a la web de Python: https://pypi.org/project/mysql-connector-python/
    - Ejecutamos en consola: "pip install mysql-connector-python"
"""

# Importamos modulo que nos permite trabajar con MySQL dentro de Python
import mysql.connector

# Configurar conexion a la base de datos MySQL
conexion = mysql.connector.connect(
    host="localhost", user="root", password="", database="master_python"
)

# ¿La conexión ha sido correcta?
# print(database)

# Creamos cursor
cursor = conexion.cursor(
    buffered=True
)  # El parametro nos permitira hacer muchas consultas usando el mismo cursor

# Creamos base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

# Obtenemos array de bases de datos
cursor.execute("SHOW DATABASES")
bases_datos = cursor.fetchall()

# Recorremos array de bases de datos
print("---- SHOW DATABASES ----")
for bd in bases_datos:
    print(bd)

# Usamos base de datos
cursor.execute("USE master_python")

# Creamos tablas
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS vehiculos(
    id INT(10) AUTO_INCREMENT NOT NULL,
    marca VARCHAR(40) NOT NULL,
    modelo VARCHAR(40) NOT NULL,
    precio FLOAT(10,2) NOT NULL,
    CONSTRAINT pk_vehiculo PRIMARY KEY (id)
)
"""
)

# Obtenemos y recorremos array de tablas
cursor.execute("SHOW TABLES")
tablas = cursor.fetchall()
print("---- SHOW TABLES ----")
for tabla in tablas:
    print(tabla)

# Insertamos datos y guardamos cambios
# cursor.execute("INSERT INTO vehiculos VALUES (NULL, 'Opel', 'Astra', 18500);")
# conexion.commit()

# Insertamos muchos registros de golpe
vehiculos = [
    ("Seat", "Ibiza", 5000),
    ("Renault", "Clio", 15000),
    ("Citroen", "Saxo", 2000),
    ("Mercedes", "Clase C", 35000),
]
# print("Productos:", vehiculos)
# cursor.executemany("INSERT INTO vehiculos VALUES (NULL, %s, %s, %s)", vehiculos)
# conexion.commit()

# Listamos datos
cursor.execute("SELECT * FROM vehiculos /*WHERE precio <= 5000 AND marca = 'Seat'*/;")
result = cursor.fetchall()
print("\n")
for coche in result:
    print("---- Vehiculo ----")
    print(coche)
    print("ID:", coche[0])
    print("Marca:", coche[1])
    print("Modelo:", coche[2])
    print("Precio:", coche[3])
    print("\n")

cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()  # Obtenemos el primer coche guardado en la base de datos
print("---- Vehiculo ----")
print(coche)
print("ID:", coche[0])
print("Marca:", coche[1])
print("Modelo:", coche[2])
print("Precio:", coche[3])
print("\n")

# Eliminamos datos
# cursor.execute("DELETE FROM vehiculos WHERE marca = 'Renault'");
# conexion.commit()
# print(cursor.rowcount, "registros borrados") # Saber cuantos registros se involucraron en la consulta anterior del cursor

# Actualizar datos
cursor.execute("UPDATE vehiculos SET modelo = 'Leon' WHERE marca = 'Seat'")
conexion.commit()
print(cursor.rowcount, "registros actualizados")
