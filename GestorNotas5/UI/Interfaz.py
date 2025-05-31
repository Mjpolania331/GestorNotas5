import sys
sys.path.append(".")
sys.path.append("Gestor_De_Notas")

import tkinter as tk
from tkinter import messagebox
from Model.GestorUsuarios import GestorUsuarios
from Model.Validar import Validar
from Model.Nota import Nota
from Controller.Controller_GN import Controller_GN

Controller_GN.CrearTablas()
class InterfazApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Gestor De Notas")
        self.gestor_usuarios = GestorUsuarios()
        self.controlador = Controller_GN()
        self.validar = Validar()
        self.usuario_actual = None

        self.frame_principal()

    def frame_principal(self):
        self.limpiar_ventana()

        tk.Label(self.root, text="Gestor De Notas - Menú Principal", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.root, text="Registrar Usuario", width=25, command=self.registrar_usuario_ventana).pack(pady=5)
        tk.Button(self.root, text="Iniciar Sesión", width=25, command=self.iniciar_sesion_ventana).pack(pady=5)
        tk.Button(self.root, text="Cambiar Contraseña", width=25, command=self.cambiar_contrasena_ventana).pack(pady=5)
        tk.Button(self.root, text="Salir", width=25, command=self.root.quit).pack(pady=20)

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ---------------------- Registro de usuario --------------------
    def registrar_usuario_ventana(self):
        self.limpiar_ventana()

        tk.Label(self.root, text="Registrar Usuario", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Nombre de usuario:").pack()
        entrada_nombre = tk.Entry(self.root)
        entrada_nombre.pack()

        tk.Label(self.root, text="Contraseña:").pack()
        entrada_contra = tk.Entry(self.root, show="*")
        entrada_contra.pack()

        def registrar():
            nombre = entrada_nombre.get().strip()
            contrasena = entrada_contra.get().strip()

            if not nombre or not contrasena:
                messagebox.showerror("Error", "Debe ingresar nombre y contraseña.")
                return

            try:
                from Model.Usuario import Usuario
                usuario = Usuario(nombre, contrasena)
                self.controlador.InsertarUsuario(usuario)
                messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
                self.frame_principal()
            except Exception as e:
                if "ya existe" in str(e).lower():
                    messagebox.showerror("Error", "El usuario ya existe.")
                else:
                    messagebox.showerror("Error BD", f"No se pudo guardar en la BD: {e}")


        tk.Button(self.root, text="Registrar", command=registrar).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.frame_principal).pack()

    # ---------------------- Iniciar sesión --------------------
    def iniciar_sesion_ventana(self):
        self.limpiar_ventana()

        tk.Label(self.root, text="Iniciar Sesión", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Nombre de usuario:").pack()
        entrada_nombre = tk.Entry(self.root)
        entrada_nombre.pack()

        tk.Label(self.root, text="Contraseña:").pack()
        entrada_contra = tk.Entry(self.root, show="*")
        entrada_contra.pack()

        def iniciar():
            nombre = entrada_nombre.get().strip()
            contrasena = entrada_contra.get().strip()

            if not nombre or not contrasena:
                messagebox.showerror("Error", "Debe ingresar nombre y contraseña.")
                return

            try:
                usuario_bd = self.controlador.BuscarUsuario(nombre)
                if usuario_bd and usuario_bd.contrasena == contrasena:
                    self.usuario_actual = usuario_bd
                    messagebox.showinfo("Bienvenido", f"Bienvenido, {nombre}.")
                    self.menu_notas_ventana()
                else:
                    messagebox.showerror("Error", "Credenciales incorrectas.")
            except Exception as e:
                messagebox.showerror("Error", "El usuario no existe.")


        tk.Button(self.root, text="Iniciar Sesión", command=iniciar).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.frame_principal).pack()

    # ---------------------- Cambiar contraseña --------------------
    def cambiar_contrasena_ventana(self):
        self.limpiar_ventana()

        tk.Label(self.root, text="Cambiar Contraseña", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Nombre de usuario:").pack()
        entrada_nombre = tk.Entry(self.root)
        entrada_nombre.pack()

        tk.Label(self.root, text="Nueva contraseña:").pack()
        entrada_nueva_contra = tk.Entry(self.root, show="*")
        entrada_nueva_contra.pack()

        def cambiar():
            nombre = entrada_nombre.get().strip()
            nueva_contra = entrada_nueva_contra.get().strip()

            if not nombre or not nueva_contra:
                messagebox.showerror("Error", "Debe ingresar usuario y nueva contraseña.")
                return

            try:
                usuario_bd = self.controlador.BuscarUsuario(nombre)
                if not usuario_bd:
                    messagebox.showerror("Error", "El usuario no existe.")
                    return

                self.controlador.ActualizarUsuario(nombre, nueva_contra)
                messagebox.showinfo("Éxito", "Contraseña actualizada con éxito.")
                self.frame_principal()
            except Exception as e:
                messagebox.showerror("Error", "El usuario no existe.")

        tk.Button(self.root, text="Cambiar Contraseña", command=cambiar).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.frame_principal).pack()

    # ---------------------- Menú de notas --------------------
    def menu_notas_ventana(self):
        self.limpiar_ventana()

        tk.Label(self.root, text=f"Menú de Notas - Usuario: {self.usuario_actual.nombre_usuario}", font=("Arial", 16)).pack(pady=10)

        # Lista de notas
        self.lista_notas = tk.Listbox(self.root, width=60)
        self.lista_notas.pack(pady=10)

        self.actualizar_lista_notas()

        # Entradas para nueva nota / editar
        tk.Label(self.root, text="Título:").pack()
        self.entrada_titulo = tk.Entry(self.root, width=40)
        self.entrada_titulo.pack()

        tk.Label(self.root, text="Contenido (0 a 5):").pack()
        self.entrada_contenido = tk.Entry(self.root, width=20)
        self.entrada_contenido.pack()

        # Entrada para ID nota (para editar o eliminar)
        tk.Label(self.root, text="ID Nota (para editar o eliminar):").pack()
        self.entrada_idnota = tk.Entry(self.root, width=20)
        self.entrada_idnota.pack()

        # Botones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Insertar Nota", command=self.insertar_nota).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Editar Nota", command=self.editar_nota).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Eliminar Nota", command=self.eliminar_nota).grid(row=0, column=2, padx=5)
        tk.Button(frame_botones, text="Cerrar Sesión", command=self.cerrar_sesion).grid(row=0, column=3, padx=5)

    def actualizar_lista_notas(self):
        self.lista_notas.delete(0, tk.END)
        cursor = Controller_GN.ObtenerCursor()
        cursor.execute("SELECT id_nota, titulo, contenido FROM nota WHERE nombre_usuario = %s ORDER BY id_nota", (self.usuario_actual.nombre_usuario,))
        filas = cursor.fetchall()
        for fila in filas:
            id_nota, titulo, contenido = fila
            self.lista_notas.insert(tk.END, f"ID: {id_nota} | Título: {titulo} | Contenido: {contenido}")

    def insertar_nota(self):
        titulo = self.entrada_titulo.get().strip()
        contenido_str = self.entrada_contenido.get().strip().replace(",", ".")
        if not titulo or not contenido_str:
            messagebox.showerror("Error", "Debe ingresar título y contenido.")
            return
        try:
            contenido = float(contenido_str)
            if not (0 <= contenido <= 5):
                messagebox.showerror("Error", "El contenido debe estar entre 0 y 5.")
                return
            nota = Nota(titulo, contenido, self.usuario_actual.nombre_usuario)
            id_generado = self.controlador.InsertarNota(nota)
            messagebox.showinfo("Éxito", f"Nota insertada con ID: {id_generado}")
            self.actualizar_lista_notas()
            self.entrada_titulo.delete(0, tk.END)
            self.entrada_contenido.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Contenido inválido, debe ser un número decimal.")
        except Exception as e:
            messagebox.showerror("Error BD", f"No se pudo insertar la nota: {e}")

    def editar_nota(self):
        idnota_str = self.entrada_idnota.get().strip()
        titulo = self.entrada_titulo.get().strip()
        contenido_str = self.entrada_contenido.get().strip().replace(",", ".")

        if not idnota_str or not titulo or not contenido_str:
            messagebox.showerror("Error", "Debe ingresar ID, título y contenido para editar.")
            return

        if not idnota_str.isdigit():
            messagebox.showerror("Error", "El ID debe ser un número entero.")
            return

        id_nota = int(idnota_str)

        try:
            if not self.controlador.ExisteNota(id_nota):
                messagebox.showerror("Error", "No existe una nota con ese ID.")
                return

            contenido = float(contenido_str)
            if not (0 <= contenido <= 5):
                messagebox.showerror("Error", "El contenido debe estar entre 0 y 5.")
                return

            nota_editada = Nota(titulo, contenido, self.usuario_actual.nombre_usuario)
            self.controlador.EditarNota(id_nota, nota_editada)
            messagebox.showinfo("Éxito", "Nota editada correctamente.")
            self.actualizar_lista_notas()
            self.entrada_idnota.delete(0, tk.END)
            self.entrada_titulo.delete(0, tk.END)
            self.entrada_contenido.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Contenido inválido, debe ser un número decimal.")
        except Exception as e:
            messagebox.showerror("Error BD", f"No se pudo editar la nota: {e}")

    def eliminar_nota(self):
        idnota_str = self.entrada_idnota.get().strip()

        if not idnota_str:
            messagebox.showerror("Error", "Debe ingresar el ID de la nota a eliminar.")
            return

        if not idnota_str.isdigit():
            messagebox.showerror("Error", "El ID debe ser un número entero.")
            return

        id_nota = int(idnota_str)

        try:
            if not self.controlador.ExisteNota(id_nota):
                messagebox.showerror("Error", "No existe una nota con ese ID.")
                return

            self.controlador.EliminarNota(id_nota)
            messagebox.showinfo("Éxito", "Nota eliminada correctamente.")
            self.actualizar_lista_notas()
            self.entrada_idnota.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error BD", f"No se pudo eliminar la nota: {e}")

    def cerrar_sesion(self):
        self.usuario_actual = None
        self.frame_principal()


if _name_ == "_main_":
    root = tk.Tk()
    app = InterfazApp(root)
    root.mainloop()