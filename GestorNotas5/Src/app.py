from flask import Flask, render_template, request, redirect, url_for, flash
from GestorNotas.GestorNotas.View.View_web import view_web_bp
from GestorNotas.GestorNotas.View.View_web import view_web_bp

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'
app.register_blueprint(view_web_bp)

# Simulación de base de datos en memoria
usuarios = [
    {
        "nombre_usuario": "mjpolania",
        "nombre": "Maria Jose Polania",
        "notas": [4.5, 3.8, 5.0]
    }
]

# Página de inicio
@app.route('/')
def inicio():
    return render_template('buscar.html')

# Buscar usuario por nombre de usuario
@app.route('/resultado_busqueda')
def resultado_busqueda():
    nombre_usuario = request.args.get('nombre_usuario')
    usuario = next((u for u in usuarios if u['nombre_usuario'] == nombre_usuario), None)
    if usuario:
        return render_template('modificar_usuario.html', usuario=usuario)
    else:
        flash('Usuario no encontrado.')
        return redirect(url_for('inicio'))

#Crear tablas (simulado)
@app.route('/crear_tablas', methods=['GET', 'POST'])
def crear_tablas():
    if request.method == 'POST':
        flash('¡Tablas creadas correctamente!')
        return redirect(url_for('inicio'))
    return render_template('crear_tabla.html')

# Modificar usuario y sus notas
@app.route('/modificar_usuario', methods=['POST'])
def modificar_usuario():
    nombre_usuario = request.form['nombre_usuario']
    usuario = next((u for u in usuarios if u['nombre_usuario'] == nombre_usuario), None)
    if usuario:
        usuario['nombre'] = request.form['nombre']
        notas_str = request.form.get('notas', '')
        if notas_str:
            usuario['notas'] = [float(n.strip()) for n in notas_str.split(',') if n.strip()]
        else:
            usuario['notas'] = []
        flash('Usuario modificado correctamente.')
    else:
        flash('Usuario no encontrado.')
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)