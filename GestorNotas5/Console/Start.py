from UI.Menu import Menu
from Model.Validar import Validar
from Model.GestorUsuarios import GestorUsuarios
from Model.Nota import Nota


class Start:
    """
    Clase encargada de iniciar y gestionar el flujo principal del sistema
    de gestión de notas. Controla el ciclo de inicio de sesión, registro,
    manejo de notas y cierre de sesión.
    """

    @staticmethod
    def start():
        """
        Método principal que ejecuta el ciclo del sistema. Permite al usuario:
        - Iniciar sesión
        - Registrarse
        - Crear, editar, eliminar y ver notas
        - Cambiar contraseña
        - Cerrar sesión

        Este método se ejecuta en un bucle continuo hasta que el usuario elige salir.
        """
        menu = Menu()
        gestor = GestorUsuarios()
        usuario_actual = None

        while True:
            if usuario_actual is None:
                # Menú de bienvenida para usuarios no autenticados
                print("\n🔑 --- Sistema de Gestión de Notas ---")
                print("1️⃣ Iniciar sesión")
                print("2️⃣ Registrarse")
                print("3️⃣ Salir")
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    usuario_actual = gestor.iniciar_sesion()
                elif opcion == "2":
                    usuario_actual = gestor.registrar_usuario()
                elif opcion == "3":
                    print("👋 Saliendo del programa.")
                    break
                else:
                    print("❌ Opción no válida.")
            else:
                # Menú principal para usuarios autenticados
                opcion = menu.menu()

                if opcion == "1":
                    # Crear nueva nota
                    titulo = Validar.validar_entrada("Ingrese título de la nota: ", "titulo")
                    contenido = Validar.validar_entrada("Ingrese contenido (0.0 - 5.0): ", "contenido")
                    nueva_nota = Nota(titulo, contenido)
                    usuario_actual.notas.agregar_nota(nueva_nota)
                    print("✅ Nota creada con éxito.")

                elif opcion == "2":
                    # Editar nota existente
                    titulo = Validar.validar_entrada("Ingrese el título de la nota a editar: ", "titulo")
                    usuario_actual.notas.editar_nota(titulo)

                elif opcion == "3":
                    # Eliminar nota
                    titulo = Validar.validar_entrada("Ingrese el título de la nota a eliminar: ", "titulo")
                    usuario_actual.notas.eliminar_nota(titulo)

                elif opcion == "4":
                    # Mostrar todas las notas
                    usuario_actual.notas.mostrar_notas()

                elif opcion == "5":
                    # Cambiar contraseña del usuario actual
                    gestor.cambiar_contrasena(usuario_actual)

                elif opcion == "6":
                    # Cerrar sesión
                    print("🔒 Cerrando sesión...")
                    usuario_actual = None

                else:
                    print("❌ Opción no válida.")