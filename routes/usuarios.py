from conexion import *
from models.usuarios import usuarios

@app.route("/login", methods=['POST'])
def login():
    id = request.form['id']
    contra = request.form['contrasena']
    ingresa = usuarios.valida_login(id, contra)
    if ingresa:
        return redirect("/principal")
    else:
        return render_template("index.html",msg="Credenciales incorrectas")

@app.route("/principal")
def principal():
    usu = usuarios.consulta()
    return render_template("principal.html", usuario=usu)

@app.route("/agregarusuario")
def agregarusuario():
    return render_template("agregarusuario.html",msg="")

@app.route("/guardausuario", methods=['POST'])
def guardausuario():
    id = request.form['id']
    nombre = request.form['nombre']
    rol = request.form['rol']
    foto = request.files['foto']
    contra = request.form['contrasena']
    confir = request.form['conficontra']
    if not usuarios.buscar(id):
        usuarios.agregar([id,nombre,rol,foto,contra,confir])
        return redirect('/principal')
    else:
        return render_template(agregarusuario,msg="Id Usuario ya existe")