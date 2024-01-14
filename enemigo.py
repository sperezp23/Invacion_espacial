from random import randint

class Enemigo():
    size = 64

    def __init__(self, skin, x, y, cambio_x, cambio_y, tipo) -> None:
        self.skin = skin
        self.x = x
        self.y = y
        self.cambio_x = cambio_x 
        self.cambio_y = cambio_y
        self.tipo = tipo
    
    def imprimir(self, display) -> None:
        display.blit(self.skin,(self.x,self.y))

    def margen_x(self, width, cambio):
        if self.x <= 0:
            self.cambio_x = cambio
            self.y += self.cambio_y
            
        elif self.x >= width - self.size:
            self.cambio_x = -cambio
            self.y += self.cambio_y
    
    def acelerar(self):
        self.x += self.cambio_x

    def respawm(self, width, y_inf, y_sup):
        self.x = randint(0,width-Enemigo.size)
        self.y = randint(y_inf,y_sup)
