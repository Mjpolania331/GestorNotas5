import re

# Clase Validar
class Validar:
    """
    Clase estática para validar diferentes tipos de entrada del usuario.

    Métodos:
    --------
    validar_entrada(mensaje, tipo):
        Solicita y valida una entrada del usuario según el tipo especificado.
        Tipos admitidos: 'usuario', 'contraseña', 'titulo', 'contenido'.
    """

    @staticmethod
    def validar_entrada(mensaje, tipo):
        """
        Solicita y valida una entrada del usuario desde la consola, dependiendo del tipo.

        Parámetros:
        -----------
        mensaje : str
            Texto que se muestra para pedir la entrada al usuario.
        tipo : str
            Tipo de dato a validar. Puede ser:
              - "usuario": entre 3 y 12 caracteres alfanuméricos o guion bajo.
              - "contraseña": entre 4 y 6 caracteres alfanuméricos.
              - "titulo": entre 3 y 50 caracteres de longitud.
              - "contenido": número decimal entre 0.0 y 5.0.

        Retorna:
        --------
        str o float:
            El valor validado si cumple con las condiciones del tipo correspondiente.
        """
        while True:
            valor = input(mensaje).strip()
            if not valor:
                print("❌ El campo no puede estar vacío.")
                continue

            if tipo == "usuario":
                if re.match(r"^[a-zA-Z0-9_]{3,12}$", valor):
                    return valor
                print("❌ El nombre de usuario debe tener entre 3 y 12 caracteres alfanuméricos o guion bajo (_).")

            elif tipo == "contraseña":
                if re.match(r"^[a-zA-Z0-9]{4,6}$", valor):
                    return valor
                print("❌ La contraseña debe tener entre 4 y 6 caracteres alfanuméricos.")

            elif tipo == "titulo":
                if 3 <= len(valor) <= 50:
                    return valor
                print("❌ El título debe tener entre 3 y 50 caracteres.")

            elif tipo == "contenido":  # Contenido de la nota ahora es un número entre 0.0 y 5.0
                try:
                    numero = float(valor)
                    if 0.0 <= numero <= 5.0:
                        return numero
                    print("❌ El contenido debe ser un número entre 0.0 y 5.0.")
                except ValueError:
                    print("❌ Debe ingresar un número válido entre 0.0 y 5.0.")
