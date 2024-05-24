from conexion import *
import hashlib

class Usuarios:
    def __init__(self,app, miDB):
        self.app=app
        self.mi_DB = miDB
        self.cursor = mi_DB.cursor()
    
    def valida_login(self, id, contra):
        cifrada = hashlib.sha512(contra.encode("utf-8")).hexdigest()
        sql = f"SELECT nombre FROM usuarios WHERE id_usuario='{id}' and contrasena='{cifrada}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        if len(resultado)>0:
            return [True,resultado[0][0]]
        else:
            return [False,""]
    
    def consulta(self):
        sql="SELECT * FROM usuarios"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar(self,id):
        sql = f"SELECT nombre FROM usuarios WHERE id_usuario='{id}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return len(resultado)>0
    
    def agregar(self,nuevo):
        ahora = datetime.now()
        tiempo = ahora.strftime("%Y%m%d%H%M%S")
        if nuevo[3].filename != "":
            nombre,extension = os.path.splitext(nuevo[3].filename)
            nuevonombre = "U" + tiempo + extension
            nuevo[3].save("uploads/"+nuevonombre)
        sql = f"INSERT INTO usuarios (id_usuario,contrasena,nombre,rol,foto) VALUES ('{nuevo[0]}','{nuevo[4]}','{nuevo[1]}',{nuevo[2]},'{nuevonombre}')"
        self.cursor.execute(sql)
        self.mi_DB.commit()


    
usuarios = Usuarios(app,mi_DB)