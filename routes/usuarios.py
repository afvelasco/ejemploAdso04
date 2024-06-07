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
            usuarios.agregar([id,nombre,rol,foto,contra])
            return redirect('/principal')
        else:
            return render_template("agregarusuario.html",msg="Constraseñas no coinciden")    
    else:
        return render_template("agregarusuario.html",msg="Id Usuario ya existe")

@app.route('/editausuario/<id>/<err>')
def editausuario(id,err=0):
    if session.get('login') == True:
        usuario = usuarios.consulta_usuario(id)
        if err==0:
            msg=''
        else:
            msg='Contraseñas no coinciden'
        return render_template("editausuario.html",usu=usuario[0],msg=msg)
    else:
        return redirect("/")

@app.route('/actualizausuario', methods=['POST'])
def actualizausuario():
    id = request.form['id']
    nombre = request.form['nombre']
    rol = request.form['rol']
    foto = request.files['foto']
    contra = request.form['contra']
    confir = request.form['confir']
    if contra==confir:
        usuarios.modificar([id,nombre,rol,foto,contra,confir])
        return redirect('/principal')
    else:
        return redirect(f"/editausuario/{id}/1")
    