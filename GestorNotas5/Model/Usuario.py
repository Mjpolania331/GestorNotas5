from Model.Lista_notas import ListaNotas

# Clase Usuario
class Usuario:
    """
    Representa un usuario del sistema de gestión de notas.

    Atributos:
    ----------
    nombre_usuario : str
        Nombre de usuario utilizado para iniciar sesión.
    contrasena : str
        Contraseña del usuario.
    notas : ListaNotas
        Estructura de datos que almacena las notas del usuario en una lista doblemente enlazada circular.
    """

    def __init__(self, nombre_usuario, contrasena):
        """
        Inicializa un nuevo usuario con un nombre de usuario, una contraseña y una lista de notas vacía.

        Parámetros:
        -----------
        nombre_usuario : str
            Nombre de usuario que identifica al usuario.
        contrasena : str
            Contraseña que el usuario utilizará para autenticarse.
        """
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.notas = ListaNotas()