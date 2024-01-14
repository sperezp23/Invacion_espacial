# %% Importar librarías
import pygame
import random

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
velocidad_jugador = 0.3

#Función
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))

# %% Enemigo_1
enemigo_1 = Enemigo(
    pygame.image.load('assets\Enemigos\Pulpo.png'),
    random.randint(0,width-Enemigo.size),
    random.randint(0,64),
    0.3, 64)

# %% Enemigo_2
enemigo_2 = Enemigo(
    pygame.image.load('assets\Enemigos\Extraterrestre.png'),
    random.randint(0,width-Enemigo.size),
    random.randint(84,128),
    0.4, 64)

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

            # Desplazamiento vertical
            if evento.key == pygame.K_UP:
                jugador_cambio_y = -velocidad_jugador
            elif evento.key == pygame.K_DOWN:
                jugador_cambio_y = velocidad_jugador

        # Tecla sin precionar
        if evento.type == pygame.KEYUP:
            
            # Frenado
            if (evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT or
                evento.key == pygame.K_UP or evento.key == pygame.K_DOWN):

                jugador_cambio_x = 0
                jugador_cambio_y = 0

    # %% Desplazamiento

    # Desplazamineto del jugador
    jugador_x += jugador_cambio_x
    jugador_y += jugador_cambio_y

    # # Desplazamiento de los enemigos
    enemigo_1.acelerar()
    enemigo_2.acelerar()

    # %% Mantener dentro de la pantalla 

    # Mantener ancho al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x > width - nave_size:
        jugador_x = width - nave_size

    # Mantener alto al jugador
    if jugador_y <= 0:
        jugador_y = 0
    elif jugador_y > heigth - nave_size:
        jugador_y = heigth - nave_size
    
    # Mantener ancho al enemigo_1
    enemigo_1.margen_x(width, 0.3)    

    # Mantener ancho al enemigo_2
    enemigo_2.margen_x(width, 0.4)

    # %% Imprimir a los pesojanes en pantalla
    jugador(jugador_x,jugador_y)
    enemigo_1.imprimir(pantalla)
    enemigo_2.imprimir(pantalla)

    pygame.display.update()        