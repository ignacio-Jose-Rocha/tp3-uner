from Puerta import Puerta
class Monstruo:
    maxEnergia = 100
    minEnergia=15
    
    def __init__(self, nombre, especie,tipo):
        self.nombre = nombre
        self.especie = especie
        if (tipo=="asustador" or tipo=="asistente"):
            self.tipo=tipo
        else:
            tipo="asustador"
            self.tipo=tipo
        
        self.pareja=None
        self.energia = self.maxEnergia  
        self.estadoDormido = False 

    def establecerNombre(self, nom):
        self.nombre = nom

    def establecerEspecie(self, esp):
        self.especie = esp

    def establecerPareja(self, mou):
        if mou and mou.tipo != self.tipo :
            self.pareja = mou

    def establecerEnergia(self, ene):
        if 0 <= ene <= 100:
            self.energia = ene

    def establecerEstadoDormido(self, est):
        self.estadoDormido = est

        
    def activarPuerta(self, pue, mou):
        if pue and mou and not pue.obtenerEstadoEnUso():
            if self.tipo == "asistente":
                pue.establecerEstadoActiva(True)
                if self.pareja:
                    pue.establecerMonstruo(self.pareja)
                else:
                    pue.establecerMonstruo(self)

    def asustar(self, pue):
        if (pue and pue.obtenerEstadoActiva() and 
        pue.obtenerHumano() and pue.obtenerMonstruo()):
            if self.tipo == "asustador":
                if pue.obtenerMonstruo() == self:
                    if self.energia >= Monstruo.minEnergia:
                            self.energia -= 10
                            pue.obtenerHumano().asustarse()

    def divertir(self, pue):
        if (pue and pue.obtenerEstadoActiva() and 
        pue.obtenerHumano() and pue.obtenerMonstruo()):
            if pue.obtenerMonstruo() == self:
                if self.energia >= Monstruo.minEnergia:
                    self.energia -= 10
                    pue.obtenerHumano().divertirse()
        


    def dormir(self):
        self.establecerEstadoDormido(True)

    def despertar(self):
        self.establecerEstadoDormido(False)


    def obtenerNombre(self):
        return self.nombre

    def obtenerEspecie(self):
        return self.especie

    def obtenerEnergia(self):
        return self.energia

    def obtenerEstadoDormido(self):
        return self.estadoDormido