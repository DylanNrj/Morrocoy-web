from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/reservasdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'tu_clave_secreta'
db = SQLAlchemy(app)

from models import *

@app.route('/')
def index():
    return render_template('pantalla_carga.html')

@app.route('/posadas')
def posadas():
    return render_template('posadas.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        telefono = request.form['telefono']
        cedula = request.form['cedula']
        tipo_usuario = 1  
        if Usuario.query.filter_by(Email=email).first():
            flash('El email ya está registrado')
            return redirect(url_for('registro'))
        usuario = Usuario(Nombre=nombre, Apellidos=apellidos, Email=email, Contraseña=password, Telefono=telefono, Cedula=cedula, id_tipo_usuario=tipo_usuario)
        db.session.add(usuario)
        db.session.commit()
        flash('Registro exitoso, ahora puedes iniciar sesión')
        return redirect(url_for('login'))
    return render_template('registro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        usuario = Usuario.query.filter_by(Email=email).first()
        if usuario and check_password_hash(usuario.Contraseña, password):
            session['usuario_id'] = usuario.id_usuario
            session['usuario_nombre'] = usuario.Nombre
            return redirect(url_for('index'))
        else:
            flash('Credenciales incorrectas')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/reservas', methods=['GET', 'POST'])
def reservas():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        id_habitacion = request.form['id_habitacion']
        fecha_entrada = request.form['fecha_entrada']
        fecha_salida = request.form['fecha_salida']
        reserva = Reserva(
            id_usuario=session['usuario_id'],
            id_habitacion=id_habitacion,
            Fecha_entrada=fecha_entrada,
            Fecha_salida=fecha_salida,
            Estado='Pendiente'
        )
        db.session.add(reserva)
        db.session.commit()
        flash('Reserva realizada con éxito')
        return redirect(url_for('reservas'))
    habitaciones = Habitacion.query.filter_by(Disponibilidad=True).all()
    return render_template('reservas.html', habitaciones=habitaciones)

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/preguntas_frecuentes')
def preguntas_frecuentes():
    return render_template('preguntas_frecuentes.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


if __name__ == '__main__':
    app.run(debug=True)