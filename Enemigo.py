class Enemigo():

    size = 64

    def __init__(self, skin, x, y, cambio_x, cambio_y) -> None:
        self.skin = skin
        self.x = x
        self.y = y
        self.cambio_x = cambio_x 
        self.cambio_y = cambio_y
    
    def imprimir(self, display) -> None:
        display.blit(self.skin,(self.x,self.y))