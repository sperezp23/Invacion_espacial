# %% Importar librarías
import pygame
from random import randint
from math import sqrt
from pygame import mixer

# %% Importar módulos propios
from objetos.enemigo import Enemigo
from objetos.jugador import Jugador
from objetos.bala import Bala
from funciones.colision import detectar_colision

# %% Estética del juego

# Inicializar Pygame
pygame.init()

# Tamaño de la ventana de juego
width = 800; height = 632
pantalla = pygame.display.set_mode((width,height))

# Titulo e Icono
pygame.display.set_caption('Invasión Espacial')
icono = pygame.image.load('assets\icono\ovni.png')
pygame.display.set_icon(icono)

# Fondo de pantalla
bg_image = pygame.image.load('assets\Fondo\Estrellas.jpg')

# Musica
mixer.music.load('assets\Sonido\MusicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# %% Puntaje
puntaje = 0
fuente = pygame.font.Font('assets\\Fonts\\font.ttf',32)
texto_x = 10
texto_y = 10
color = (255,255,255)

# Mostrar puntaje
def mostrar_puntaje(x,y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, color)
    pantalla.blit(texto,(x,y))

# %% Game Over
fuente_final = pygame.font.Font('assets\\Fonts\\font.ttf',64)

def game_over():
    mi_fuente_final = fuente_final.render('GAME OVER',True,color)
    pantalla.blit(mi_fuente_final,(width/8+10,height/2-20))

# %% Jugador
tamaño = 64

jugador = Jugador(
    pygame.image.load('assets\\Nave\\Nave_espacial.png'),
    (width-64)/2, height - tamaño, 0, 0, 3, 64)

velocidad_jugador = 0.6

# %% Enemigos
enemigos = []
cantidad_enemigos = 4

for i in range(cantidad_enemigos):
    enemigos.append(Enemigo(
    pygame.image.load('assets\Enemigos\Pulpo.png'),
    randint(0,width-tamaño), randint(32,96), 0.3, 64, 1, 32))

    enemigos.append(Enemigo(
    pygame.image.load('assets\Enemigos\Extraterrestre.png'),
    randint(0,width-tamaño), randint(84,160), 0.4, 64, 2, 32))

# %% Bala
bala = Bala(pygame.image.load('assets\\Bala\\laser.png'),
    0, height - tamaño, 0, 2, 4, 32, False)

# Sonido Colisiones   
sonido_bala = mixer.Sound('assets\Sonido\disparo.mp3')    
sonido_colision = mixer.Sound('assets\Sonido\Golpe.mp3')
sonido_colision.set_volume(0.3)

# %% Loop del juego
def main_game():
    global puntaje

    se_ejecuta = True

    while se_ejecuta:
        # Establecer el fondo de pantalla 
        pantalla.blit(bg_image,(0,0))

        # Iterar eventos
        for evento in pygame.event.get():

            # Salir del programa
            if evento.type == pygame.QUIT:
                se_ejecuta = False

            # Tecla presionada
            if evento.type == pygame.KEYDOWN:
                
                # Desplazamiento horizontal
                if evento.key == pygame.K_LEFT:
                    jugador.cambio_x = -velocidad_jugador
                
                elif evento.key == pygame.K_RIGHT:
                    jugador.cambio_x = velocidad_jugador
                
                elif evento.key == pygame.K_SPACE and not bala.visible:
                    sonido_bala.play()
                    bala.x = jugador.x
                    bala.disparar(pantalla)

            # Tecla sin presionar
            if evento.type == pygame.KEYUP:
                
                # Frenado
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    jugador.cambio_x = 0

        # Desplazamiento del jugador
        jugador.acelerar()

        # Movimiento Bala
        if bala.y <= -bala.size:
            bala.y = jugador.y
            bala.visible = False

        if bala.visible:
            bala.disparar(pantalla)
            bala. y -= bala.cambio_y

        # Desplazamiento de los enemigos
        for enemigo in enemigos:
            if enemigo.y >= jugador.y - enemigo.size:
                for k in range(cantidad_enemigos*2):
                    enemigos[k].y = 1000
                game_over()
                break

            enemigo.acelerar()

            # Colision
            impacto = detectar_colision(enemigo.x, enemigo.y, bala.x, bala.y)    

            # Impacto enemigo
            if impacto:
                sonido_colision.play()
                bala.y = jugador.y
                bala.visible = False
                puntaje += 1

                if enemigo.tipo == 1:
                    enemigo.respawm(width,32,96)
                else:
                    enemigo.respawm(width,84,160) 
                
            if enemigo.tipo == 1:
                enemigo.margen_x(width, 0.3)
            else:    
                enemigo.margen_x(width, 0.4)

        # Mantener ancho al jugador
        jugador.margen_x(width)

        # Imprimir a los personajes y el puntaje en pantalla
        mostrar_puntaje(texto_x, texto_y) 

        jugador.imprimir(pantalla)

        for enemigo in enemigos:
            enemigo.imprimir(pantalla)
        
        # Actualizar pantalla
        pygame.display.update()
   