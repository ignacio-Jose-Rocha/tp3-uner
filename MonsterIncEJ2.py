from Monstruo import Monstruo
from Humano import Humano
from Puerta import Puerta
class MonstersInc:
    monstruos = []
    humanos = []

    def __init__(self):
        self.monstruos = []
        self.puertas = []

    def agregarMonstruo(self, mon):
        if (isinstance(mon, dict) and "asustador"
             in mon and "asistente" in mon):
            asustador=mon["asustador"]
            asistente=mon["asistente"]
            if (isinstance(asustador,Monstruo) 
                and isinstance(asistente,Monstruo)):
                if(asustador.pareja==asistente and
                   asistente.pareja==asustador):
                    if(asustador.tipo=="asustador" and 
                       asistente.tipo=="asistente"):
                        
                        self.monstruos.append(mon)

    def agregarPuerta(self, pue):
        if isinstance(pue, Puerta):
            self.puertas.append(pue)

    def eliminarMonstruo(self, mon):
        if mon in self.monstruos:
            self.monstruos.remove(mon)

    def eliminarPuerta(self, pue):
        for puerta in self.monstruos:
            if puerta.equals(pue):
                self.puertas.remove(puerta)
                break

    def obtenerMonstruos(self):
        return self.monstruos

    def obtenerHumanos(self):
        return self.humanos