from flask import Flask, render_template,request,redirect,send_from_directory
import mysql.connector
import os
from datetime import datetime

app = Flask(__name__)
mi_DB = mysql.connector.connect(host="localhost",
                                port="3306",
                                user="root",
                                password="",
                                database="db_prueba")

app.config['CARPETAU'] = os.path.join('uploads')

