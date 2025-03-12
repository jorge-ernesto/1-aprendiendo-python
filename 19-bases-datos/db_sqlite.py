"""
Dentro de Python viene un sistema gestor de BD, basado en SQL, llamado SQLite
https://www.sqlite.org/
"""

# Importamos modulo que nos permite trabajar con SQLite dentro de Python
import sqlite3

# Configurar conexion a la base de datos SQLite
conexion = sqlite3.connect("pruebas_sqlite.db")

# Creamos cursor
# Un cursor es un objeto de acceso a datos que se puede utilizar para recorrer el conjunto de filas de una tabla o insertar nuevas filas en una tabla. Los cursores tienen tres formas: búsqueda, inserción y actualización.
# https://desktop.arcgis.com/es/arcmap/latest/analyze/python/data-access-using-cursors.htm#:~:text=Un%20cursor%20es%20un%20objeto,%3A%20b%C3%BAsqueda%2C%20inserci%C3%B3n%20y%20actualizaci%C3%B3n.
cursor = conexion.cursor()

# Creamos tabla
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    titulo VARCHAR(255),
    description TEXT,
    precio INT(255)
);
"""
)

# Guardamos cambios
conexion.commit()

# Insertamos datos y guardamos cambios
# cursor.execute("INSERT INTO productos VALUES (NULL, 'Primer producto', 'Descripcion de mi producto', 550);")
# conexion.commit()

# Borramos registros y guardamos cambios
# cursor.execute("DELETE FROM productos;")
# conexion.commit()

# Insertamos muchos registros de golpe
productos = [
    ("Ordenador portatil", "Buen PC", 700),
    ("Telefono movil", "Buen telefono", 140),
    ("Placa base", "Buena placa", 80),
    ("Tablet", "Buena tablet", 300),
]
# print("Productos:", productos)
# cursor.executemany("INSERT INTO productos VALUES (NULL, ?, ?, ?)", productos)
# conexion.commit()

# Actualizamos registros
cursor.execute("UPDATE productos SET precio = 90 WHERE precio = 80;")
conexion.commit()

# Listamos datos:
# - Ejecutamos consulta SQL con el cursor
# - Obtenemos array de productos
cursor.execute("SELECT * FROM productos /*WHERE precio >= 300*/;")
print("Cursor:", cursor)
productos = cursor.fetchall()
print("Productos:", productos)

# Recorremos array de productos
print("\n")
for producto in productos:
    print("---- Producto -----")
    print("ID:", producto[0])
    print("Titulo:", producto[1])
    print("Descripcion:", producto[2])
    print("Precio:", producto[3])
    print("\n")

# Obtenemos array de productos
cursor.execute("SELECT titulo FROM productos;")
productos = cursor.fetchall()
print("Productos:", productos)

# Cerramos conexion
conexion.close()
