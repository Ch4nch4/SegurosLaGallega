from ast import Str
import pymysql
from CapaNegocio.Database import *

class Autos(Database):
    def __init__(self):
        super().__init__()
        
    def getAuto(self,id):
        sql="SELECT * FROM aseguradora.auto where matricula='{}'".format(id)
        print(sql)
        try:
            self.cursor.execute(sql)
            auto=self.cursor.fetchone()
            return auto
           
            
           
        except Exception as e:
            raise 

    def getTodos(self):
        sql= 'SELECT * FROM aseguradora.auto'
        try:
            self.cursor.execute(sql)
            ListaAutos=self.cursor.fetchall()
            return ListaAutos     
        except Exception as e:
            raise
    
    def insertAuto(self,matricula,modelo,anio):
        sql="INSERT INTO aseguradora.auto VALUES('{}','{}',{})".format(matricula,modelo,anio)
        try:
            self.cursor.execute(sql)
            self.connection.commit()    
        except Exception as e:
            raise

    def updateAuto(self,matricula,modelo,anio):
        sql="UPDATE aseguradora.auto SET autoModelo ='{}', autoAño = '{}'  WHERE matricula = '{}'".format(modelo,anio,matricula)
        try:
            self.cursor.execute(sql)
            self.connection.commit()    
        except Exception as e:
            raise
    
    def deleteAuto(self,matricula):
        sql="DELETE FROM  aseguradora.auto  WHERE matricula = '{}'".format(matricula)
        try:
            self.cursor.execute(sql)
            self.connection.commit()    
        except Exception as e:
            raise
        
    #OTROS METODOS 
    def tieneInformeAccidente(self,matricula):
        sql="SELECT * FROM aseguradora.persona_has_auto_has_informeaccidente WHERE persona_has_auto_auto_matricula='{}'".format(matricula)
        try:
            self.cursor.execute(sql)
            informe=self.cursor.fetchone()
            return informe!=None
        
        except Exception as e:
            raise
    
    def getIdInformesAccidentesDeAuto(self,matricula):
        sql= "SELECT InformeAccidente_idInformeAccidente FROM aseguradora.persona_has_auto_has_informeaccidente WHERE persona_has_auto_auto_matricula='{}'".format(matricula)
        try:
            self.cursor.execute(sql)
            ListaIdInformes=self.cursor.fetchall()
            return ListaIdInformes
         
        except Exception as e:
            raise