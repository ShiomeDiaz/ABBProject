import pygame, sys

pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = (800, 500)


# Crear ventana

screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # Logica

    # Color de fondo
    screen.fill(WHITE)

    # ------- ZONA DE DIBUJO

    pygame.draw.rect(screen, BLACK, (400,230,50,50))




    # actualizar pantalla
    pygame.display.flip()