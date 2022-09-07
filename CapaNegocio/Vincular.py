from ast import Str
import pymysql
from CapaNegocio.Database import *
from CapaNegocio.Persona import *
from CapaNegocio.Autos import *
from CapaNegocio.Siniestros import *

class Vincular(Database):
    def __init__(self):
        super().__init__()
        
    def existeVinculoPersonAuto(self,idPersona,IdAuto):
        sql="SELECT * FROM aseguradora.persona_has_auto where persona_idpersona={} and auto_matricula='{}'".format(idPersona,IdAuto)
        self.cursor.execute(sql)
        vinculo=self.cursor.fetchone()
        return vinculo != None   
        
    def vincularPersonaAuto(self,idPersona,IdAuto):
        # verificar que la persona existe en la DB 
        # msmo para auto
        # insertar en tabla correspondiente 
        tpersona=Personas()
        tauto=Autos()
        if tpersona.existePersona(idPersona):
            if tauto.getAuto(IdAuto) != None:
                sql="INSERT INTO aseguradora.persona_has_auto VALUES ({},'{}')",format(idPersona,IdAuto)
                self.cursor.execute(sql)
                self.cursor.commit()
                return "Se inserto exitosamnete"
            else:
              return "La matricula no existe"
        else:
            return "La persona no existe"
    
    def existeVinculoPersonAutoInforme(self,idPersona,IdAuto,IdInforme):
        sql="SELECT * FROM aseguradora.persona_has_auto_has_informeaccidente where persona_has_auto_persona_idpersona={} and persona_has_auto_auto_matricula='{}' and InformeAccidente_idInformeAccidente={}".format(idPersona,IdAuto,IdInforme)
        self.cursor.execute(sql)
        vinculo=self.cursor.fetchone()
        return vinculo != None 
    
    def vincularAutoInforme(self,IdAuto,IdInforme,importeDaño):
        # verificar si existe el auto, y traer el conductor asociado
        # verificar si existe informe 
        # insertar en la tabla correspondiente
        tpersona=Personas()
        tauto=Autos()
        tinforme=Siniestro()
        if tauto.getAuto(IdAuto) != None:
            idPersona=self.traerIdConductor(IdAuto)
            if idPersona != None:
                if tinforme.getInforme(IdInforme) != None:
                    sql="INSERT INTO aseguradora.persona_has_auto_has_informeaccidente VALUES ({},'{}',{},{})".format(idPersona,IdAuto,IdInforme,importeDaño)
                    self.cursor.execute(sql)
                    self.cursor.commit()
                    return "Se inserto exitosamnete"
                else:
                   return "el Informe no existe" 
            else:
              return "El auto no tiene conductor asignado"
        else:
            return "La matricula no existe"
    
    def traerIdConductor(self,idAuto):
        sql="SELECT persona_idpersona FROM aseguradora.persona_has_auto where auto_matricula='{}'".format(idAuto)
        self.cursor.execute(sql)
        return self.cursor.fetchone()
        