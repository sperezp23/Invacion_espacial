import pygame
import pygame_gui
from pygame.locals import QUIT
from game import main_game

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 632
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menú con Pygame_GUI")

# Inicializar Pygame_GUI
gui_manager = pygame_gui.UIManager((WIDTH, HEIGHT))

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Fondo de pantalla
bg_image = pygame.image.load('assets\Fondo\Estrellas.jpg')

# Botones
button_play = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((WIDTH // 2 - 100, HEIGHT // 2 - 50), (200, 50)),
    text="Play",
    manager=gui_manager,
)

button_exit = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((WIDTH // 2 - 100, HEIGHT // 2 + 50), (200, 50)),
    text="Exit",
    manager=gui_manager,
)

# Bucle principal
running_menu = True
while running_menu:
    time_delta = pygame.time.Clock().tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == QUIT:
            running_menu = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button_play:
                    running_menu = False
                    main_game()
                elif event.ui_element == button_exit:
                    running_menu = False

        gui_manager.process_events(event)

    gui_manager.update(time_delta)

    screen.blit(bg_image,(0,0))
    gui_manager.draw_ui(screen)
    pygame.display.flip()

pygame.quit()
