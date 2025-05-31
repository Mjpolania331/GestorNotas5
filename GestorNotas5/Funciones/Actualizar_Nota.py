import sys
sys.path.append(".")  # Acceso a módulos del proyecto

from Controller.Controller_GN import Controller_GN
from Model.Model_GN import Nota

def actualizar_nota():
    print("\n✏️ Actualización de Nota")

    usuario = input("Ingrese el nombre de usuario de la nota: ").strip()
    titulo = input("Ingrese el título de la nota a actualizar: ").strip()
    nuevo_contenido = input("Ingrese el nuevo contenido de la nota: ").strip()

    nota_actualizada = Nota(usuario=usuario, titulo=titulo, contenido=nuevo_contenido)

    try:
        Controller_GN.actualizar_nota(titulo, nota_actualizada)
        print(f"\n✅ Nota '{titulo}' actualizada correctamente.\n")
    except Exception as e:
        print(f"\n❌ Error al actualizar la nota: {e}\n")