from Humano import Humano
class Monstruo:
    maxEnergia = 100
    
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.energia = self.maxEnergia  
        self.estadoDormido = False 

    def asustar(self, humano:Humano):
        if self.estadoDormido==False:
            if(humano.estadoAsustado==False):
                if self.energia>=10:
                    self.energia -= 10
                else:
                    self.energia=0
                Humano.estadoAsustado = True
        
    def divertir(self, humano:Humano):
        if self.estadoDormido==False:
            if humano.estadoAsustado:
                    self.energia -= 20
                    Humano.estadoAsustado = False

    def dormir(self):
        self.estadoDormido = True
        self.energia += 15
        if self.energia > self.maxEnergia:
            self.energia = self.maxEnergia

    def establecerEnergia(self, energia):
        if(energia>self.maxEnergia):
            self.energia=self.maxEnergia
        elif(energia<0):
            self.energia=0
        else:
            self.energia=energia


    def establecerNombre(self, nombre):
        self.nombre = nombre

    def establecerEspecie(self, especie):
        self.especie = especie

    def establecerEstadoDormido(self, estado):
        self.estadoDormido = estado

    def obtenerNombre(self):
        return self.nombre

    def obtenerEspecie(self):
        return self.especie

    def obtenerEnergia(self):
        return self.energia

    def obtenerEstadoDormido(self):
        return self.estadoDormido
    
    def despertar(self):
        self.estadoDormido = False