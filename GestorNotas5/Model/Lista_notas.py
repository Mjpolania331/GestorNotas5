from GestorNotas.GestorNotas.Model.Nodo_nota import NodoNota
from Model.Validar import Validar
import datetime

# Clase ListaNotas:
# Implementa una lista doblemente enlazada circular para gestionar notas académicas.
class ListaNotas:
    def __init__(self):
        # Nodo cabeza de la lista (inicio de la lista circular)
        self.head = None

    # Método para agregar una nueva nota al inicio de la lista
    def agregar_nota(self, nota):
        nuevo_nodo = NodoNota(nota)
        if self.head is None:
            # Si la lista está vacía, se inicializa el primer nodo apuntando a sí mismo (circular)
            self.head = nuevo_nodo
            nuevo_nodo.prev = nuevo_nodo
            nuevo_nodo.next = nuevo_nodo
        else:
            # Inserta el nuevo nodo antes del nodo cabeza y actualiza punteros
            last = self.head.prev
            nuevo_nodo.prev = last
            nuevo_nodo.next = self.head
            self.head.prev = nuevo_nodo
            last.next = nuevo_nodo
            self.head = nuevo_nodo  # Se actualiza la cabeza a la nueva nota

    # Método para eliminar una nota por su título
    def eliminar_nota(self, titulo):
        if self.head is None:
            print("⚠ No hay notas registradas.")
            return

        current = self.head
        while True:
            if current.nota.titulo == titulo:
                if current.next == current:
                    # Solo había una nota, se elimina
                    self.head = None
                else:
                    # Se eliminan enlaces al nodo actual
                    if current == self.head:
                        self.head = current.next
                    current.prev.next = current.next
                    current.next.prev = current.prev
                print(f"✅ Nota '{titulo}' eliminada.")
                return
            current = current.next
            if current == self.head:
                break

        print(f"❌ No se encontró una nota con el título '{titulo}'.")

    # Método para editar el contenido de una nota por su título (versión simplificada)
    def editar_nota(self, titulo, nuevo_valor):
        actual = self.head
        if actual:
            while True:
                if actual.nota.titulo == titulo:
                    # Se actualiza el contenido de la nota
                    actual.nota.contenido = nuevo_valor
                    return True
                actual = actual.next
                if actual == self.head:
                    break
        return False

        # --- Código muerto (no se ejecutará nunca) ---
        # Este fragmento parece una versión anterior o alternativa de edición
        current = self.head
        while True:
            if current.nota.titulo == titulo:
                print(f"✏ Editando nota: {titulo}")
                nuevo_contenido = validar.validar_entrada("Nuevo contenido (0.0 - 5.0): ", "contenido")
                current.nota.contenido = nuevo_contenido
                current.nota.fecha_creacion = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("✅ Nota actualizada correctamente.")
                return
            current = current.next
            if current == self.head:
                break

        print(f"❌ No se encontró una nota con el título '{titulo}'.")

    # Método para mostrar todas las notas almacenadas
    def mostrar_notas(self):
        if self.head is None:
            print("⚠ No hay notas registradas.")
            return

        current = self.head
        print("\n📋 --- Tus Notas ---")
        while True:
            nota = current.nota
            print(f"📌 Título: {nota.titulo}\n📊 Contenido (calificación): {nota.contenido}\n📅 Fecha: {nota.fecha_creacion}\n")
            current = current.next
            if current == self.head:
                break
