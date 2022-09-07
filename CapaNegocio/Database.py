from ast import Str
import pymysql

class Database:
    # Genero la apertura y cierre con la Base de Datos 
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='hepatalgina',
            db='aseguradora'
        )
        self.cursor=self.connection.cursor()
        print("Coneccion establecida")

    def close(self):
        self.connection.close()