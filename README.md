# Invasión Espacial

¡Bienvenido a Invasión Espacial! Un juego simple desarrollado en Python utilizando la biblioteca Pygame. Prepárate para una emocionante batalla en el espacio, donde deberás esquivar enemigos y disparar para acumular puntos.

## Requisitos

- Python 3.x
- Pygame

## Instrucciones de Uso

1. Asegúrate de tener Python instalado en tu sistema.
2. Instala la dependencia necesaria ejecutando el siguiente comando en la terminal:

    ```bash
    pip install pygame
    ```

3. Ejecuta el script utilizando el siguiente comando:

    ```bash
    python nombre_del_script.py
    ```

4. Usa las teclas de flecha izquierda y derecha para mover tu nave espacial.
5. Presiona la tecla de espacio para disparar y destruir a los enemigos.
6. ¡Acumula la mayor cantidad de puntos posible antes de que los enemigos lleguen demasiado cerca!

## Estructura del Código

- **Importar librerías y modulos propios:** El código comienza importando las librerías necesarias y módulos personalizados que contienen las clases y funciones para el juego.
  
- **Estética del juego:** Configuración de la ventana de juego, título, icono, fondo de pantalla, música, puntaje y funciones para mostrar el puntaje y el estado de "Game Over".

- **Jugador:** Se crea el jugador con su respectiva imagen y configuración.

- **Enemigos:** Se generan enemigos aleatorios con diferentes tipos y configuraciones.

- **Bala:** Se define la clase para las balas disparadas por el jugador.

- **Sonidos:** Se cargan los efectos de sonido para disparos y colisiones.

- **Loop del juego:** La función principal `main_game` inicia un bucle que maneja eventos de teclado, actualiza las posiciones de los objetos, detecta colisiones, reproduce sonidos y actualiza la pantalla.

## Recursos

- Imágenes de fondo, icono de nave y enemigos se encuentran en la carpeta 'assets'.
- Archivos de sonido están ubicados en 'assets\Sonido'.
- La fuente utilizada para el texto se encuentra en 'assets\Fonts'.

¡Buena suerte en tu misión espacial! 🚀🎮

---

# Pygame GUI Menu

Este es un simple menú implementado en Python utilizando la biblioteca Pygame y Pygame_GUI. El menú presenta dos botones: "Play" y "Exit". Al presionar el botón "Play", el menú se cierra y se inicia el juego principal.

## Requisitos

- Python 3.x
- Pygame 2.x
- Pygame_GUI

## Instrucciones de Uso

1. Asegúrate de tener Python instalado en tu sistema.
2. Instala las dependencias ejecutando el siguiente comando en la terminal:

    ```bash
    pip install pygame pygame_gui
    ```

3. Ejecuta el script utilizando el siguiente comando:

    ```bash
    python nombre_del_script.py
    ```

4. En el menú, puedes hacer clic en el botón "Play" para iniciar el juego o en el botón "Exit" para cerrar la aplicación.

## Estructura del Código

- `import pygame`: Importa la biblioteca principal para el desarrollo de juegos.
- `import pygame_gui`: Importa la extensión para interfaces gráficas de usuario en Pygame.
- `from pygame.locals import QUIT`: Importa la constante QUIT para manejar el evento de cierre de la aplicación.
- `from game import main_game`: Importa la función `main_game` del módulo `game`.
- Inicializa Pygame y configura la pantalla.
- Inicializa Pygame_GUI y establece un administrador de interfaz de usuario.
- Define colores y carga una imagen de fondo.
- Crea botones ("Play" y "Exit") utilizando Pygame_GUI.
- Entra en un bucle principal que maneja eventos, actualiza la interfaz y muestra la pantalla.
- Al presionar el botón "Play", el menú se cierra y se inicia la función `main_game`.
- Al presionar el botón "Exit", el menú se cierra.

## Recursos

- La imagen de fondo del menú se carga desde el archivo 'assets\Fondo\Estrellas.jpg'.
