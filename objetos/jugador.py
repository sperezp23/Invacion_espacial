from random import randint

class Jugador():

    def __init__(self, skin, x, y, cambio_x, cambio_y, tipo, size) -> None:
        self.skin = skin
        self.x = x
        self.y = y
        self.cambio_x = cambio_x 
        self.cambio_y = cambio_y
        self.tipo = tipo
        self.size = size
    
    def imprimir(self, display) -> None:
        display.blit(self.skin,(self.x,self.y))

    def margen_x(self, width):
        if self.x <= 0:
            self.cambio_x = 0
            
        elif self.x >= width - self.size:
            self.x = width - self.size
    
    def acelerar(self):
        self.x += self.cambio_x
