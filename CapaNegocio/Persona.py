from ast import Str
import pymysql
from CapaNegocio.Database import *
#comentario prueba para github
class Personas(Database):
    def __init__(self):
        super().__init__()
    
    def getPersona(self,id):
        sql="SELECT * FROM aseguradora.persona where idpersona='{}'".format(id)
        print(sql)
        try:
            self.cursor.execute(sql)
            auto=self.cursor.fetchone()
            return auto
           
        except Exception as e:
            raise 
        
    def getPersonaxCarnet(self,carnet):
        # creo este metodo para poder buscar persona por carnet
        sql="SELECT * FROM aseguradora.persona where personaCarnetConductor ='{}'".format(carnet)
        try:
            self.cursor.execute(sql)
            persona=self.cursor.fetchone()
            return persona
        except Exception as e:
            raise 
    def getTodos(self):
        sql= 'SELECT * FROM aseguradora.persona'
        try:
            self.cursor.execute(sql)
            ListaPersonas=self.cursor.fetchall()
            return ListaPersonas 
        except Exception as e:
            raise
    
    def insertPersona(self,idPersona,carnetConductor,Nombre,Apellido,Direccion):
        sql="INSERT INTO aseguradora.persona VALUES ('{}','{}','{}','{}','{}')".format(idPersona,carnetConductor,Nombre,Apellido,Direccion)
        try:
            self.cursor.execute(sql)
            self.connection.commit()    
        except Exception as e:
            raise

    def updatePersona(self,idPersona,carnetConductor,Nombre,Apellido,Direccion):
        sql="UPDATE aseguradora.persona SET personaCarnetConductor ='{}', personaNombre = '{}' , personaApellido = '{}', personaDireccion = '{}' WHERE idpersona = '{}'".format(carnetConductor,Nombre,Apellido,Direccion,idPersona)
        try:
            self.cursor.execute(sql)
            self.connection.commit()    
        except Exception as e:
            raise
    
    def deletePersona(self,idPersona): 
        sql="DELETE FROM  aseguradora.persona  WHERE idpersona = '{}'".format(idPersona)
        try:
            self.cursor.execute(sql)
            self.connection.commit()    
        except Exception as e:
            raise
    
    def existePersona(self,idPersona):
        sql="SELECT * FROM aseguradora.persona where idpersona='{}'".format(idPersona)
        persona=self.cursor.fetchone()
        return persona != None
    
           
    #OTROS METODOS 
    def tieneAutosPersona(self,IdPersona):
        sql="SELECT * FROM aseguradora.persona_has_auto WHERE ='{}'".format(IdPersona)
        try:
            self.cursor.execute(sql)
            autos=self.cursor.fetchone()
            return autos!=None
        
        except Exception as e:
            raise
        
    def getMatriculasDeAutosDePersona(self,IdPersona):
        sql= "SELECT auto_matricula FROM aseguradora.persona_has_auto WHERE persona_idpersona='{}'".format(IdPersona)
        try:
            self.cursor.execute(sql)
            ListaMatriculas=self.cursor.fetchall()
            return ListaMatriculas
        
        except Exception as e:
            raise 