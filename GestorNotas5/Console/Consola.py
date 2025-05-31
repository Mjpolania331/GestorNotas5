import tkinter as tk
from tkinter import messagebox
from Model.GestorUsuarios import GestorUsuarios
from Model.Nota import Nota

# Instancia del gestor de usuarios
gestor = GestorUsuarios()

# ---------------------- INTERFAZ GRÁFICA ----------------------

def iniciar_interfaz():
    """
    Inicia la interfaz gráfica para el sistema de gestión de notas.
    Permite al usuario iniciar sesión o registrarse mediante una ventana con Tkinter.
    """
    ventana = tk.Tk()
    ventana.title("Gestor de Notas - Inicio")
    ventana.geometry("300x200")

    def login():
        """
        Lógica para iniciar sesión desde la interfaz gráfica.
        """
        nombre = entry_nombre.get()
        contrasena = entry_contrasena.get()
        usuario = gestor.iniciar_sesion_interfaz(nombre, contrasena)
        if usuario:
            messagebox.showinfo("Éxito", "Sesión iniciada correctamente")
            ventana.destroy()
            mostrar_menu(usuario)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrecta")

    def registrar():
        """
        Lógica para registrar un nuevo usuario desde la interfaz gráfica.
        """
        nombre = entry_nombre.get()
        contrasena = entry_contrasena.get()
        if gestor.registrar_usuario_interfaz(nombre, contrasena):
            messagebox.showinfo("Éxito", "Usuario registrado exitosamente")
        else:
            messagebox.showerror("Error", "Usuario ya existe")

    # Elementos del formulario
    tk.Label(ventana, text="Nombre de usuario").pack()
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()

    tk.Label(ventana, text="Contraseña").pack()
    entry_contrasena = tk.Entry(ventana, show="*")
    entry_contrasena.pack()

    tk.Button(ventana, text="Iniciar sesión", command=login).pack(pady=5)
    tk.Button(ventana, text="Registrarse", command=registrar).pack()

    ventana.mainloop()


def mostrar_menu(usuario):
    """
    Muestra el menú principal de la interfaz gráfica luego del inicio de sesión.
    Permite al usuario crear, ver, editar, eliminar notas y cambiar contraseña.
    """
    ventana_menu = tk.Tk()
    ventana_menu.title("Gestor de Notas - Menú Principal")
    ventana_menu.geometry("400x300")

    def crear_nota():
        """
        Ventana para crear una nueva nota.
        """
        nueva = tk.Toplevel(ventana_menu)
        nueva.title("Crear Nota")

        tk.Label(nueva, text="Título").pack()
        entrada_titulo = tk.Entry(nueva)
        entrada_titulo.pack()

        tk.Label(nueva, text="Nota (0.0 a 5.0)").pack()
        entrada_contenido = tk.Entry(nueva)
        entrada_contenido.pack()

        def guardar():
            """
            Guarda la nueva nota creada.
            """
            titulo = entrada_titulo.get().strip()
            contenido_str = entrada_contenido.get().strip().replace(",", ".")
            if not titulo or not contenido_str:
                messagebox.showerror("Error", "Los campos no pueden estar vacíos")
                return
            try:
                contenido = float(contenido_str)
                if 0.0 <= contenido <= 5.0:
                    nota = Nota(titulo, contenido)
                    usuario.notas.agregar_nota(nota)
                    messagebox.showinfo("Nota creada", "✅ Nota guardada con éxito")
                    nueva.destroy()
                else:
                    messagebox.showerror("Error", "La nota debe estar entre 0.0 y 5.0")
            except ValueError:
                messagebox.showerror("Error", "Ingrese un número válido")

        tk.Button(nueva, text="Guardar", command=guardar).pack(pady=5)

    def ver_notas():
        """
        Muestra todas las notas del usuario actual en una ventana emergente.
        """
        notas = usuario.notas
        actual = notas.head
        texto = ""
        if actual:
            while True:
                n = actual.nota
                texto += f"{n.titulo}: {n.contenido} ({n.fecha_creacion})\n"
                actual = actual.next
                if actual == notas.head:
                    break
        else:
            texto = "No hay notas registradas."

        messagebox.showinfo("Notas", texto)

    def eliminar_nota():
        """
        Ventana para eliminar una nota especificando el título.
        """
        elim = tk.Toplevel(ventana_menu)
        elim.title("Eliminar Nota")

        tk.Label(elim, text="Título de la nota a eliminar").pack()
        entrada = tk.Entry(elim)
        entrada.pack()

        def eliminar():
            """
            Ejecuta la eliminación de la nota indicada.
            """
            titulo = entrada.get().strip()
            if titulo:
                usuario.notas.eliminar_nota(titulo)
                messagebox.showinfo("Eliminar", f"Intento de eliminación de '{titulo}' completado.")
                elim.destroy()
            else:
                messagebox.showerror("Error", "Debe ingresar un título válido")

        tk.Button(elim, text="Eliminar", command=eliminar).pack(pady=5)

    def editar_nota():
        """
        Ventana para editar el contenido de una nota existente.
        """
        editar = tk.Toplevel(ventana_menu)
        editar.title("Editar Nota")

        tk.Label(editar, text="Título de la nota a editar").pack()
        entrada_titulo = tk.Entry(editar)
        entrada_titulo.pack()

        tk.Label(editar, text="Nuevo contenido (0.0 a 5.0)").pack()
        entrada_nuevo = tk.Entry(editar)
        entrada_nuevo.pack()

        def actualizar():
            """
            Guarda los cambios en la nota editada.
            """
            titulo = entrada_titulo.get().strip()
            nuevo_str = entrada_nuevo.get().strip().replace(",", ".")
            if not titulo or not nuevo_str:
                messagebox.showerror("Error", "Los campos no pueden estar vacíos")
                return