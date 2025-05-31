import sys
sys.path.append(".")  # Acceso a módulos del proyecto

from Controller.Controller_GN import Controller_GN

def actualizar_contrasena_usuario():
    print("\n🔐 Actualización de Contraseña de Usuario")

    username = input("Ingrese el nombre de usuario existente: ").strip()
    nueva_contrasena = input("Ingrese la nueva contraseña: ").strip()

    try:
        Controller_GN.actualizar_contrasena_usuario(username, nueva_contrasena)
        print(f"\n✅ Contraseña de '{username}' actualizada correctamente.\n")
    except Exception as e:
        print(f"\n❌ Error al actualizar la contraseña: {e}\n")