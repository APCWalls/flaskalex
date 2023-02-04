from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.data.producto_venta import ProductoVenta
from app.data.usuario_aplicacion import UsuarioAplicacion

rutas_usuarios = Blueprint("routes", __name__)


@rutas_usuarios.route('/')
def index():
    return render_template('index.html')

@rutas_usuarios.route('/producto')
def moviles():
    producto_venta = ProductoVenta()

    productos = producto_venta.select_all(db)

    return render_template('producto.html',productos=productos)

@rutas_usuarios.route('/insertProducto',methods=['POST'])
def addProducto():
    Nombre = request.form['producto'] 
    Precio = request.form['precio'] 

    if Nombre and Precio: # ESTA CONDICION SIRVE PARA QUE SI TENEMOS TODOS LOS CAMPOS VAMOS A HACER LA CONSULTA INSERT A LA BASE DE DATOS
        cursor = db.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
        sql = "INSERT INTO producto (producto,precio) VALUES (%s, %s)" # DEFINIMOS LA CONSULTA INSERT DE TIPO STRING %S
        data = (Nombre,Precio) # HACEMOS UNA TUPLA CON LOS DATOS 
        cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
        db.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO
    return redirect(url_for('routes.moviles'))


@rutas_usuarios.route('/borrarProducto',methods=['POST'])
def deleteProducto():
    idproducto = request.form['idproducto'] 

    if idproducto: # ESTA CONDICION SIRVE PARA QUE SI TENEMOS TODOS LOS CAMPOS VAMOS A HACER LA CONSULTA INSERT A LA BASE DE DATOS
        cursor = db.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
        sql = "DELETE FROM producto WHERE idproducto=%s" # DEFINIMOS LA CONSULTA INSERT DE TIPO STRING %S
        data = list(idproducto) # HACEMOS UNA TUPLA CON LOS DATOS 
        cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
        db.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO
    return redirect(url_for('routes.moviles'))

@rutas_usuarios.route('/usuario')
def personas():
    usuario_aplicacion = UsuarioAplicacion()

    usuarios = usuario_aplicacion.select_all(db)

    return render_template('usuarios.html',usuarios=usuarios)



@rutas_usuarios.route('/insertUsuario',methods=['POST'])
def addUser():
    Nombre = request.form['nombre'] 
    Correo = request.form['correo'] 

    if Nombre and Correo: # ESTA CONDICION SIRVE PARA QUE SI TENEMOS TODOS LOS CAMPOS VAMOS A HACER LA CONSULTA INSERT A LA BASE DE DATOS
        cursor = db.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
        sql = "INSERT INTO usuario (nombre,correo) VALUES (%s, %s)" # DEFINIMOS LA CONSULTA INSERT DE TIPO STRING %S
        data = (Nombre,Correo) # HACEMOS UNA TUPLA CON LOS DATOS 
        cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
        db.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO
    return redirect(url_for('routes.personas'))


@rutas_usuarios.route('/borrarUsuario',methods=['POST'])
def delete():
    idusuario = request.form['idusuario'] 

    if idusuario: # ESTA CONDICION SIRVE PARA QUE SI TENEMOS TODOS LOS CAMPOS VAMOS A HACER LA CONSULTA INSERT A LA BASE DE DATOS
        cursor = db.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
        sql = "DELETE FROM usuario WHERE idusuario=%s" # DEFINIMOS LA CONSULTA INSERT DE TIPO STRING %S
        data = list(idusuario) # HACEMOS UNA TUPLA CON LOS DATOS 
        cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
        db.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO
    return redirect(url_for('routes.personas'))

