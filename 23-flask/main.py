# Importar librerias
from flask import Flask, flash, redirect, url_for, render_template, request
from flask_mysqldb import MySQL
from datetime import datetime

# Crear el app
app = Flask(__name__)
app.secret_key = "clave_secreta_flask"

# Configurar conexion a la base de datos MySQL
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "proyectoflask"

# Inicializar conexion a la base de datos MySQL
mysql = MySQL(app)


# Context processors
@app.context_processor
def date_now():
    # Fecha en formato YYYY-MM-DD hh:mm:ss.ffffff -- now (sin parentesis) asegura que siempre se obtenga la fecha y hora actualizada
    return {"now": datetime.now}


# Endpoints
@app.route("/")
def index():
    edad = 101
    personas = ["Víctor", "Paco", "Francisco", "David"]

    return render_template(
        "index.html",
        edad=edad,
        dato1="Valor",
        dato2="Valor2",
        lista=["uno", "dos", "tres"],
        personas=personas,
    )


@app.route("/informacion")
@app.route("/informacion/<string:nombre>")
@app.route("/informacion/<string:nombre>/<apellidos>")
def informacion(nombre=None, apellidos=None):
    texto = ""
    if nombre != None and apellidos != None:
        texto = f"Bienvenido, {nombre} {apellidos}"

    return render_template("informacion.html", texto=texto)


@app.route("/contacto")
@app.route("/contacto/<redireccion>")
def contacto(redireccion=None):
    if redireccion is not None:
        return redirect(url_for("lenguajes"))

    return render_template("contacto.html")


@app.route("/lenguajes-de-programacion")
def lenguajes():
    return render_template("lenguajes.html")


@app.route("/crear-coche", methods=["GET", "POST"])
def crear_coche():
    if request.method == "POST":

        marca = request.form["marca"]
        modelo = request.form["modelo"]
        precio = request.form["precio"]
        ciudad = request.form["ciudad"]

        # Validacion
        errores = {}
        if marca == "" or marca == None:
            errores["marca"] = "La marca no es válida"
        if modelo == "" or modelo == None:
            errores["modelo"] = "El modelo no es válido"
        if precio == "" or precio == None:
            errores["precio"] = "El precio no es válido"
        else:
            try:
                precio = float(precio)
                if precio <= 0:
                    errores["precio"] = "El precio debe ser mayor que cero"
            except ValueError:
                errores["precio"] = "El precio debe ser un número válido"
        if ciudad == "" or ciudad == None:
            errores["ciudad"] = "La ciudad no es válida"

        if len(errores) > 0:
            for error in errores:
                flash(
                    errores[error], "error"
                )  # flash con categoría "error" para mostrar mensajes de error. Las categorías más comunes son "success" y "error".
            return redirect(url_for("index"))

        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO coches VALUES(NULL, %s, %s, %s, %s)",
            (marca, modelo, precio, ciudad),
        )
        cursor.connection.commit()

        flash(
            "Has creado el coche correctamente!!"
        )  # flash sin categoría (por defecto "success") para mostrar mensajes de éxito

        return redirect(url_for("index"))

    return render_template("crear_coche.html")


@app.route("/coches")
def coches():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches ORDER BY id DESC")
    coches = cursor.fetchall()
    cursor.close()

    return render_template("coches.html", coches=coches)


@app.route("/coche/<coche_id>")
def coche(coche_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id = %s", (coche_id))
    coche = cursor.fetchall()
    cursor.close()

    return render_template("coche.html", coche=coche[0])


@app.route("/borrar-coche/<coche_id>")
def borrar_coche(coche_id):
    cursor = mysql.connection.cursor()
    cursor.execute(f"DELETE FROM coches WHERE id = {coche_id}")
    mysql.connection.commit()

    flash("El coche ha sido eliminado !!")

    return redirect(url_for("coches"))


@app.route("/editar-coche/<coche_id>", methods=["GET", "POST"])
def editar_coche(coche_id):
    if request.method == "POST":

        marca = request.form["marca"]
        modelo = request.form["modelo"]
        precio = request.form["precio"]
        ciudad = request.form["ciudad"]

        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE coches
            SET marca = %s,
                modelo = %s,
                precio = %s,
                ciudad = %s
            WHERE id = %s
        """,
            (marca, modelo, precio, ciudad, coche_id),
        )
        cursor.connection.commit()

        flash("Has editado el coche correctamente!!")

        return redirect(url_for("coches"))

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id = %s", (coche_id))
    coche = cursor.fetchall()
    cursor.close()

    return render_template("crear_coche.html", coche=coche[0])


# Ejecutar el app
if __name__ == "__main__":
    app.run(debug=True)
