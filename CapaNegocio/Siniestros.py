import pymysql
from CapaNegocio.Database import *

class Siniestro(Database):
    def __init__(self):
        super().__init__()
    
    def getInforme(self,id):
        sql="SELECT * FROM aseguradora.informeaccidente where idInformeAccidente='{}'".format(id)
        self.cursor.execute(sql)
        informe=self.cursor.fetchone()
        return informe
       
    def getTodos(self): 
        sql= 'SELECT * FROM aseguradora.informeaccidente'
        try:
            self.cursor.execute(sql)
            ListaInformes=self.cursor.fetchall()
            return ListaInformes
        except Exception as e:
            raise
# 1	2021-05-24	esquina brown y irigoyen punta alta
# 2	2022-01-01	esquina paso y irigoyen punta alta
# 3	2022-04-05	brown  1245

    def getInformesdeLista(self,ListaIdInformes):
        # Dada una lista con numeros de IdInformes 
        # Retorna otra lista de Tuplas de los informes pedidos
        # por ejemplo :
        # lista = getInformesdeLista([1,3])
        # print(lista) --> [(1,2021-05-24,"esquina brown y irigoyen punta alta"),(3,2022-04-05,"brown  1245")]
        listaInformes=[]
        for idInforme in ListaIdInformes:
            listaInformes.append(self.getUnInformeAccidente(idInforme))
        return listaInformes
    
    def traerProximoNroInforme(self):
        sql=" SELECT  idInformeAccidente as 'last' FROM aseguradora.informeaccidente  order by idInformeAccidente DESC LIMIT 1" 
        
        self.cursor.execute(sql)
        last =  self.cursor.fetchone()
        return int(last[0]) + 1
    
    def insertarInforme(self, idInforme, fecha, lugar):
        try :
            sql="INSERT INTO aseguradora.informeaccidente VALUES ({},'{}','{}')".format(idInforme, fecha , lugar)
            print(sql)
            self.cursor.execute(sql)
            self.cursor.commit()
            return "Informe insertado exitosamente"
        except Exception as e:
            raise 