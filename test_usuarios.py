from conexion import *
from models.usuarios import usuarios
import hashlib
import pytest

class Test_usuarios:
    def setup_class(self):
        # Prepreparar entorno de prueba
        cifrada = hashlib.sha512("hola".encode("UTF-8")).hexdigest()
        sql = f"INSERT INTO usuarios (id_usuario,contrasena) VALUES ('afv','{cifrada}')"
        cursor = mi_DB.cursor()
        cursor.execute(sql)
        mi_DB.commit()

    def teardown_class(self):
        # Limpiar la base de datos
        sql=f"DELETE FROM usuarios WHERE id_usuario='afv'"
        cursor = mi_DB.cursor()
        cursor.execute(sql)
        mi_DB.commit()

    @pytest.mark.parametrize(
        ["id_entrada","contra_entrada","esperado"],
        [("afv","hola",True),
        ("afv","1234",False),
        ("dsa","2342",False)]
    )

    def test_valida_login(self, id_entrada, contra_entrada, esperado):
        # Ejecutar el método a probar (la prueba)
        resultado = usuarios.valida_login(id_entrada, contra_entrada)
        # Verificar resultados
        assert resultado[0] == esperado













'''


class Test_Usuarios:
    @pytest.mark.parametrize(
            ["id","contra","id_entrada","contra_entrada","esperado"],
            [("afv","hola","afv","hola",True),
            ("afv","hola","afv","1234",False),
            ("afv","hola","dsa","2342",False)]
    )

    def test_valida_login(id,contra,id_entrada,contra_entrada,esperado):
        # Prepreparar entorno de prueba
        cifrada = hashlib.sha512(contra.encode("UTF-8")).hexdigest()
        sql = f"INSERT INTO usuarios (id,contrasena,nombre,rol) VALUES ('{id}','{cifrada}','AF Velaso',1)"
        cursor = mi_DB.cursor()
        cursor.execute(sql)
        mi_DB.commit()
        # Ejecutar el método a probar (la prueba)
        resultado = usuarios.valida_login(id_entrada, contra_entrada)
        # Limpiar la base de datos
        sql=f"DELETE FROM usuarios WHERE id='{id}'"
        cursor.execute(sql)
        mi_DB.commit()
        # Verificar resultados
        assert resultado == esperado
'''
