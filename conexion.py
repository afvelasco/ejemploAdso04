from random import randint
from flask import Flask, render_template,request,redirect,send_from_directory,session
import mysql.connector
import os
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = str(randint(10000,99999))
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)
mi_DB = mysql.connector.connect(host="localhost",
                                port="3306",
                                user="root",
                                password="",
                                database="db_prueba")

app.config['CARPETAU'] = os.path.join('uploads')

