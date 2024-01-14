from objetos.jugador import Jugador

class Bala(Jugador):
    def __init__(self, skin, x, y, cambio_x, cambio_y, tipo, size, visible) -> None:
        super().__init__(skin, x, y, cambio_x, cambio_y, tipo, size)

        self.visible = visible
    
    def disparar(self, pantalla):       
        self.visible= True
        pantalla.blit(self.skin,(self.x + self.size/4, self.y + 10))