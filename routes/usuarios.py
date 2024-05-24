from conexion import *
from models.usuarios import usuarios

@app.route("/login", methods=['POST'])
def login():
    id = request.form['id']
    contra = request.form['contrasena']
    ingresa = usuarios.valida_login(id, contra)
    if ingresa[0]:
        session["login"] = True
        session["id"] = id
        session["nombre"] = ingresa[1]
        return redirect("/principal")
    else:
        return render_template("index.html",msg="Credenciales incorrectas")

@app.route("/principal")
def principal():
    if session.get('login') == True:
        usu = usuarios.consulta()
        nom=session.get('nombre')
        return render_template("principal.html", usuario=usu,nom=nom)
    else:
        return redirect("/")

@app.route("/agregarusuario")
def agregarusuario():
    if session.get('login') == True:
        return render_template("agregarusuario.html",msg="")
    else:
        return redirect("/")

@app.route("/guardausuario", methods=['POST'])
def guardausuario():
    id = request.form['id']
    nombre = request.form['nombre']
    rol = request.form['rol']
    foto = request.files['foto']
    contra = request.form['contrasena']
    confir = request.form['conficontra']
    if not usuarios.buscar(id):
        if contra==confir:
            usuarios.agregar([id,nombre,rol,foto,contra,confir])
            return redirect('/principal')
        else:
            return render_template("agregarusuario.html",msg="Constraseñas no coinciden")    
    else:
        return render_template("agregarusuario.html",msg="Id Usuario ya existe")
