from random import randint
from objetos.jugador import Jugador

class Enemigo(Jugador):
    def margen_x(self, width, cambio):
        if self.x <= 0:
            self.cambio_x = cambio
            self.y += self.cambio_y
            
        elif self.x >= width - self.size:
            self.cambio_x = -cambio
            self.y += self.cambio_y

    def respawm(self, width, y_inf, y_sup):
        self.x = randint(0,width-self.size)
        self.y = randint(y_inf,y_sup)
