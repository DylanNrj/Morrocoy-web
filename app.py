from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/reservasdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'tu_clave_secreta'
db = SQLAlchemy(app)

from models import *

# Rutas principales
@app.route('/')
@app.route('/inicio')
def inicio():
    return render_template('base.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/opiniones')
def opiniones():
    return render_template('opiniones.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        # Procesar datos del formulario de contacto
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')
        # Aquí podrías guardar los datos o enviarlos por correo
        flash('Mensaje enviado correctamente. ¡Gracias por contactarnos!')
        return redirect(url_for('mensaje_enviado'))
    return render_template('contacto.html')

@app.route('/mensaje_enviado')
def mensaje_enviado():
    return render_template('mensaje_enviado.html')

@app.route('/pantalla_carga')
def pantalla_carga():
    return render_template('pantalla_carga.html')

@app.route('/posadas')
def posadas():
    return render_template('posadas.html')

if __name__ == '__main__':
    app.run(debug=True)