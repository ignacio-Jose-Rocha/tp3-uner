from Humano import Humano
from Monstruo import Monstruo
class Puerta:
    
    def __init__(self,num:int,hum:Humano):
        self.numero = num
        self.humano = hum
        self.monstruo = None 
        self.estadoActiva=False

        def establecerHumano(self, hum:Humano):
            if hum is not None: 
                self.humano = hum
            else:
                print("El objeto Humano no está ligado.")

        def establecerMonstruo(self, mon:Monstruo):
            if mon is not None: 
                self.mon = mon
            else:
                print("El objeto Humano no está ligado.")
        def establecerEstadoActiva(self, est:bool):
            self.estadoActiva = est
        def obtenerNumero(self) :
            return self.numero
        def obtenerHumano(self) :
            return self.humano
        def obtenerMonstruo(self):
            return self.monstruo
        def obtenerEstadoActiva(self):
            return self.estadoActiva
        def obtenerEstadoEnUso(self):
            if self.estadoActiva == True and self.monstruo != None:
                return True
        def equals(self, puerta):
            return self.humano ==puerta.obtenerHumano() and self.estadoActiva == puerta.obtenerEstadoActiva() and self.monstruo==puerta.obtenerMonstruo()
