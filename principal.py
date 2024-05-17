from conexion import *
from routes.usuarios import login

@app.route("/")
def index():
    return render_template("index.html",msg="")

@app.route("/uploads/<nombre>")
def uploads(nombre):
    return send_from_directory(app.config['CARPETAU'],nombre)

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)