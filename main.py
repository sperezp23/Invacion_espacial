# %% Importar librarías
import pygame
from random import randint
from math import sqrt

# %% Importar modulos
from Enemigo import Enemigo

# %% Inicializar Pygame
pygame.init()

# Tamaño de la ventana de juego
width = 800; heigth = 600
pantalla = pygame.display.set_mode((width,heigth))

# %% Titulo e Icono
pygame.display.set_caption('Invasión Espacial')
icono = pygame.image.load('assets\icono\ovni.png')
pygame.display.set_icon(icono)

# %% Fondo de pantalla
bg_image = pygame.image.load('assets\Fondo\Estrellas.jpg')

# %% Inicializar variables
puntaje = 0

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
velocidad_jugador = 0.4

#Función
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))

# %% Enemigo_1
enemigo_1 = Enemigo(
    pygame.image.load('assets\Enemigos\Pulpo.png'),
    randint(0,width-Enemigo.size), randint(0,64), 0.3, 64)

# %% Enemigo_2
enemigo_2 = Enemigo(
    pygame.image.load('assets\Enemigos\Extraterrestre.png'),
    randint(0,width-Enemigo.size), randint(84,128), 0.4, 64)

# %% Bala
# Imagen
img_bala = pygame.image.load('assets\\Bala\\bala.png')

# Posición inicial
bala_size = 32
bala_x = 0
bala_y = heigth - nave_size

# Variables de desplazamiento
bala_cambio_x = 0
bala_cambio_y = 0.9
bala_visible = False

def disparar(x,y):
    global bala_visible
    bala_visible= True
    pantalla.blit(img_bala,(x + nave_size/4, y + 10))

# %% Colisiones
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

    # # Desplazamiento de los enemigos
    enemigo_1.acelerar()
    enemigo_2.acelerar()

    # Movimiento Bala
    if bala_y <= -bala_size:
        bala_y = jugador_y
        bala_visible = False

    if bala_visible:
        disparar(bala_x,bala_y)
        bala_y -= bala_cambio_y

    # %% Colision
    impacto_1 = colision(enemigo_1.x, enemigo_1.y, bala_x, bala_y)
    impacto_2 = colision(enemigo_2.x, enemigo_2.y, bala_x, bala_y)

    # Impacto enemigo 1
    if impacto_1:
        bala_y = jugador_y
        bala_visible = False
        enemigo_1.respawm(width,0,64)
        puntaje += 1
        print(puntaje)

    # Impacto enemigo 2
    if impacto_2:
        bala_y = jugador_y
        bala_visible = False
        enemigo_2.respawm(width,84,128)
        puntaje += 1
        print(puntaje)

    # %% Mantener dentro de la pantalla 

    # Mantener ancho al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x > width - nave_size:
        jugador_x = width - nave_size
    
    # Mantener ancho al enemigo_1
    enemigo_1.margen_x(width, 0.3)    

    # Mantener ancho al enemigo_2
    enemigo_2.margen_x(width, 0.4)

    # %% Imprimir a los pesojanes en pantalla
    jugador(jugador_x,jugador_y)
    enemigo_1.imprimir(pantalla)
    enemigo_2.imprimir(pantalla)

    pygame.display.update()        