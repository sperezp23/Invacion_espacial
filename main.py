# %% Importar librarías
import pygame
import random

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
# Imagen
img_enemigo_1 = pygame.image.load('assets\Enemigos\Pulpo.png')

# Posición inicial
enemigo_1_size = 64
enemigo_1_x = random.randint(0,width-enemigo_1_size)
enemigo_1_y = random.randint(0,64)

# Variables de desplazamiento
enemigo_1_cambio_x = 0.3
enemigo_1_cambio_y = 64

#Función
def enemigo_1(x,y):
    pantalla.blit(img_enemigo_1,(x,y))

# %% Enemigo_2
# Imagen
img_enemigo_2 = pygame.image.load('assets\Enemigos\Extraterrestre.png')

# Posición inicial
enemigo_2_size = 64
enemigo_2_x = random.randint(0,width-enemigo_2_size)
enemigo_2_y = random.randint(64,128)

# Variables de desplazamiento
enemigo_2_cambio_x = 0.4
enemigo_2_cambio_y = 64

#Función
def enemigo_2(x,y):
    pantalla.blit(img_enemigo_2,(x,y))

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
    enemigo_1_x += enemigo_1_cambio_x
    enemigo_2_x += enemigo_2_cambio_x

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
    if enemigo_1_x <= 0:
        enemigo_1_cambio_x = 0.3
        enemigo_1_y += enemigo_1_cambio_y
    elif enemigo_1_x >= width - enemigo_1_size:
        enemigo_1_cambio_x = -0.3
        enemigo_1_y += enemigo_1_cambio_y

    # Mantener ancho al enemigo_2
    if enemigo_2_x <= 0:
        enemigo_2_cambio_x = 0.4
        enemigo_2_y += enemigo_2_cambio_y
    elif enemigo_2_x >= width - enemigo_2_size:
        enemigo_2_cambio_x = -0.4
        enemigo_2_y += enemigo_2_cambio_y

    # %% Imprimir a los pesojanes en pantalla
    jugador(jugador_x,jugador_y)
    enemigo_1(enemigo_1_x,enemigo_1_y)
    enemigo_2(enemigo_2_x,enemigo_2_y)

    pygame.display.update()        