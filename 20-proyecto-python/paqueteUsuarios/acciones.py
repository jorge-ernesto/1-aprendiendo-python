# Desde el paquete "paqueteUsuarios" importamos el modulo "usuario"
import paqueteUsuarios.usuario as modelo

# Desde el paquete "paqueteNotas" importamos el modulo "acciones"
import paqueteNotas.acciones


class Acciones:
    def registro(self):
        print("\nOk!! Vamos a registrate en el sistema...")

        # Obtenemos informacion del usuario
        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        # Creamos el objeto Usuario
        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        # Validamos que el registro sea correcto
        if registro[0] >= 1:
            print(
                f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}"
            )
        else:
            print("\nNo te haz registrado correctamente")

    def login(self):
        print("\nVale!! Identificate en el sistema...")

        # Obtenemos informacion del usuario
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        # Creamos el objeto Usuario
        usuario = modelo.Usuario("", "", email, password)
        login = usuario.identificar()

        # Validamos que el login sea correcto
        if login:
            if email == login[3]:
                print(
                    f"\nBienvenido {login[1]}, te has registrado en el sistema en la fecha {login[5]}"
                )
                self.proximasAcciones(login)
            else:
                print("\nLogin incorrecto!! Intentalo más tarde")
        else:
            print("\nLogin incorrecto!! Intentalo más tarde")

        """
        try:
            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema en el {login[5]}")
                self.proximasAcciones(login)
            else:
                print("\nLogin incorrecto!! Intentalo más tarde")
        except Exception as e:
            print(e)
            print(type(e))
            print(type(e).__name__)
            print("Login incorrecto!! Intentalo más tarde")

            # Imprimir una excepcion como lo hace el controlador
            # https://stackoverflow.com/questions/1483429/how-do-i-print-an-exception-in-python
            print("\n---- Traceback como lo hace el controlador ----")
            import traceback
            traceback.print_exc()
        """

    def proximasAcciones(self, usuario):
        print(
            """
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """
        )

        accion = input("¿Que quieres hacer?: ")
        hazEl = paqueteNotas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(f"Ok, {usuario[1]}, hasta pronto!!!")
            exit()
