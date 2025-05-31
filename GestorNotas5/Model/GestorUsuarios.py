from Model.Validar import Validar
from Model.Usuario import Usuario

# Clase GestorUsuarios: se encarga de gestionar los usuarios del sistema
class GestorUsuarios:
    def __init__(self):
        # Diccionario para almacenar los usuarios registrados (clave: nombre de usuario, valor: objeto Usuario)
        self.usuarios = {}
        # Instancia del validador para controlar entradas del usuario
        self.validar = Validar()

    # Método para registrar un nuevo usuario en modo consola
    def registrar_usuario(self):
        # Solicita nombre de usuario con validación
        nombre = self.validar.validar_entrada("Ingrese nombre de usuario: ", "usuario")
        # Verifica si el usuario ya existe
        if nombre in self.usuarios:
            print("❌ Este usuario ya existe.")
            return None
        # Solicita contraseña con validación
        contrasena = self.validar.validar_entrada("Ingrese contraseña: ", "contraseña")
        # Crea y almacena el nuevo usuario
        self.usuarios[nombre] = Usuario(nombre, contrasena)
        print("✅ Usuario registrado correctamente.")
        return self.usuarios[nombre]

    # Método para iniciar sesión en modo consola
    def iniciar_sesion(self):
        # Solicita nombre de usuario y contraseña con validación
        nombre = self.validar.validar_entrada("Ingrese nombre de usuario: ", "usuario")
        contrasena = self.validar.validar_entrada("Ingrese contraseña: ", "contraseña")
        # Verifica credenciales
        if nombre in self.usuarios and self.usuarios[nombre].contrasena == contrasena:
            print(f"✅ Bienvenido, {nombre}.")
            return self.usuarios[nombre]
        else:
            print("❌ Credenciales incorrectas.")
            return None

    # Método para cambiar la contraseña de un usuario
    def cambiar_contrasena(self, usuario):
        # Solicita nueva contraseña con validación
        nueva_contra = self.validar.validar_entrada("Ingrese nueva contraseña: ", "contraseña")
        # Actualiza la contraseña del usuario
        usuario.contrasena = nueva_contra
        print("✅ Contraseña actualizada con éxito.")

    # Método para registrar un usuario desde la interfaz gráfica
    def registrar_usuario_interfaz(self, nombre, contrasena):
        # Verifica si el usuario ya existe
        if nombre in self.usuarios:
            return False
        # Crea y almacena el nuevo usuario
        self.usuarios[nombre] = Usuario(nombre, contrasena)
        return True

    # Método para iniciar sesión desde la interfaz gráfica
    def iniciar_sesion_interfaz(self, nombre, contrasena):
        # Verifica credenciales
        if nombre in self.usuarios and self.usuarios[nombre].contrasena == contrasena:
            return self.usuarios[nombre]
        return None