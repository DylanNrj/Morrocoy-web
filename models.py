from flask_sqlalchemy import SQLAlchemy
from app import db

class TipoUsuario(db.Model):
    __tablename__ = 'tipo_usuario'
    id_tipo_usuario = db.Column(db.Integer, primary_key=True)
    Rol = db.Column(db.String(50), nullable=False)

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100), nullable=False)
    Apellidos = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(100), unique=True, nullable=False)
    Contraseña = db.Column(db.String(255), nullable=False)
    Telefono = db.Column(db.String(20))
    Cedula = db.Column(db.String(20), unique=True)
    id_tipo_usuario = db.Column(db.Integer, db.ForeignKey('tipo_usuario.id_tipo_usuario'))

class Empleados(db.Model):
    __tablename__ = 'empleados'
    id_empleados = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100), nullable=False)
    Apellidos = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(100), unique=True, nullable=False)
    Telefono = db.Column(db.String(20))
    Rol_empleado = db.Column(db.String(50))

class Posada(db.Model):
    __tablename__ = 'posada'
    id_posada = db.Column(db.Integer, primary_key=True)
    id_empleados = db.Column(db.Integer, db.ForeignKey('empleados.id_empleados'))
    Nombre = db.Column(db.String(100), nullable=False)
    Descripcion = db.Column(db.Text)
    Ubicacion = db.Column(db.String(255))
    Imagen_URL = db.Column(db.String(255))

class TipoHabitacion(db.Model):
    __tablename__ = 'tipo_habitacion'
    id_tipo_habitacion = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100), nullable=False)
    Descripcion = db.Column(db.Text)
    Capacidad = db.Column(db.Integer)
    Precio_base = db.Column(db.Numeric(10,2))

class Habitacion(db.Model):
    __tablename__ = 'habitacion'
    id_habitacion = db.Column(db.Integer, primary_key=True)
    id_posada = db.Column(db.Integer, db.ForeignKey('posada.id_posada'))
    id_tipo_habitacion = db.Column(db.Integer, db.ForeignKey('tipo_habitacion.id_tipo_habitacion'))
    Disponibilidad = db.Column(db.Boolean, default=True)

class Reserva(db.Model):
    __tablename__ = 'reserva'
    id_reserva = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    id_habitacion = db.Column(db.Integer, db.ForeignKey('habitacion.id_habitacion'))
    Fecha_entrada = db.Column(db.Date, nullable=False)
    Fecha_salida = db.Column(db.Date, nullable=False)
    Estado = db.Column(db.String(50))