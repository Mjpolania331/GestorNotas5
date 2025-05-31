from flask import Blueprint, render_template, redirect, url_for, flash

# Suponiendo que tienes una lista de usuarios en tu app principal o puedes importarla aquí
# from ...app import usuarios

view_web_bp = Blueprint('view_web', __name__, template_folder='../../Templates')

# Simulación de base de datos en memoria (puedes importar usuarios reales si lo prefieres)
usuarios = [
    {
        "nombre_usuario": "mjpolania",
        "nombre": "Maria Jose Polania",
        "notas": [4.5, 3.8, 5.0]
    }
]

@view_web_bp.route('/ver_usuario/<nombre_usuario>')
def ver_usuario(nombre_usuario):
    usuario = next((u for u in usuarios if u['nombre_usuario'] == nombre_usuario), None)
    if usuario:
        return render_template('view_web.html', usuario=usuario)
    else:
        flash('Usuario no encontrado.')
        return redirect(url_for('inicio'))