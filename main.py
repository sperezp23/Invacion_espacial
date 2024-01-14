# %% Importar librarías
import pygame
from random import randint
from math import sqrt
from pygame import mixer

# %% Importar modulos propios
from enemigo import Enemigo

# %% Inicializar Pygame
pygame.init()

# Tamaño de la ventana de juego
width = 800; heigth = 632
pantalla = pygame.display.set_mode((width,heigth))

# %% Titulo e Icono
pygame.display.set_caption('Invasión Espacial')
icono = pygame.image.load('assets\icono\ovni.png')
pygame.display.set_icon(icono)

# %% Fondo de pantalla
bg_image = pygame.image.load('assets\Fondo\Estrellas.jpg')

# %% Musica
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
    pantalla.blit(mi_fuente_final,(width/8+10,heigth/2-20))

# %% Jugador
# Imagen
img_jugador = pygame.image.load('assets\\Nave\\Nave_espacial.png')

# Posición inicial
nave_size = 64
jugador_x = (width-nave_size)/2
jugador_y = heigth - nave_size

# Variables de desplazamiento
jugador_cambio_x = 0
jugador_cambio_y = 0
velocidad_jugador = 0.6

#Función
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))

# %% Enemigos
enemigos = []
cantidad_enemigos = 4

for i in range(cantidad_enemigos):
    enemigos.append(Enemigo(
    pygame.image.load('assets\Enemigos\Pulpo.png'),
    randint(0,width-Enemigo.size), randint(32,96), 0.3, 64, 1))

    enemigos.append(Enemigo(
    pygame.image.load('assets\Enemigos\Extraterrestre.png'),
    randint(0,width-Enemigo.size), randint(84,160), 0.4, 64, 2))

# %% Bala
# Sonido    
sonido_bala = mixer.Sound('assets\Sonido\disparo.mp3')
# Imagen
img_bala = pygame.image.load('assets\\Bala\\laser.png')

# Posición inicial
bala_size = 32
bala_x = 0
bala_y = heigth - nave_size

# Variables de desplazamiento
bala_cambio_x = 0
bala_cambio_y = 2
bala_visible = False

def disparar(x,y):
    global bala_visible
    bala_visible= True
    pantalla.blit(img_bala,(x + nave_size/4, y + 10))

# %% Colisiones
sonido_colision = mixer.Sound('assets\Sonido\Golpe.mp3')
sonido_colision.set_volume(0.3)

def colision(x_1, y_1, x_2, y_2):
    distancia = sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
    if distancia < 27:
        return True
    else: 
        return False
    
# %% Loop del juego
se_ejecuta = True

while se_ejecuta:
    # Estableser el fondo de pantalla 
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
                jugador_cambio_x = -velocidad_jugador
            
            elif evento.key == pygame.K_RIGHT:
                jugador_cambio_x = velocidad_jugador
            
            elif evento.key == pygame.K_SPACE and not bala_visible:
                sonido_bala.play()
                bala_x = jugador_x
                disparar(bala_x, bala_y)

        # Tecla sin precionar
        if evento.type == pygame.KEYUP:
            
            # Frenado
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_cambio_x = 0

    # %% Desplazamiento

    # Desplazamineto del jugador
    jugador_x += jugador_cambio_x

        # Movimiento Bala
    if bala_y <= -bala_size:
        bala_y = jugador_y
        bala_visible = False

    if bala_visible:
        disparar(bala_x,bala_y)
        bala_y -= bala_cambio_y

    # # Desplazamiento de los enemigos
    for enemigo in enemigos:
        if enemigo.y >= jugador_y - nave_size:
            for k in range(cantidad_enemigos*2):
                enemigos[k].y = 1000
            game_over()
            break

        enemigo.acelerar()

        # %% Colision
        impacto = colision(enemigo.x, enemigo.y, bala_x, bala_y)    

        # Impacto enemigo
        if impacto:
            sonido_colision.play()
            bala_y = jugador_y
            bala_visible = False
            puntaje += 1
            print(puntaje)

            if enemigo.tipo == 1:
                enemigo.respawm(width,32,96)
            else:
                enemigo.respawm(width,84,160) 
            
        if enemigo.tipo == 1:
            enemigo.margen_x(width, 0.3)
        else:    
            enemigo.margen_x(width, 0.4)

    # %% Mantener ancho al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x > width - nave_size:
        jugador_x = width - nave_size

    # %% Imprimir a los pesojanes y el puntaje en pantalla
    mostrar_puntaje(texto_x, texto_y)    
    jugador(jugador_x,jugador_y)

    for enemigo in enemigos:
        enemigo.imprimir(pantalla)

    pygame.display.update()        