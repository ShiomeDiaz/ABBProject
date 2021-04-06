import pygame, sys

pygame.init()

# Definir colores
BLACK = (0, 0, 0)
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 490


class caverns(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../Images/cueva2.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()


class trailer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../Images/camion.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()



# Crear ventana

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

clock = pygame.time.Clock()

done = False

background = pygame.image.load("../Images/background.jpg").convert()
caverna1 = caverns()
caverna2 = caverns()
caverna3 = caverns()
caverna4 = caverns()
caverna5 = caverns()
caverna6 = caverns()
caverna7 = caverns()
caverna1.rect.x = 300
caverna1.rect.y = 50
caverna2.rect.x = 200
caverna2.rect.y = 150
caverna3.rect.x = 400
caverna3.rect.y = 150
caverna4.rect.x = 100
caverna4.rect.y = 250
caverna5.rect.x = 250
caverna5.rect.y = 250
caverna6.rect.x = 350
caverna6.rect.y = 250
caverna7.rect.x = 500
caverna7.rect.y = 250

all_sprite_list = pygame.sprite.Group()
all_sprite_list.add(caverna1, caverna2, caverna3, caverna4, caverna5, caverna6, caverna7)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # Logica

    # Color de fondo
    screen.blit(background, [0, 0])
    pygame.display.set_caption("Proyecto estructura de datos")

    # ------- ZONA DE DIBUJO
    all_sprite_list.draw(screen)

    pygame.draw.line(screen, BLACK, (caverna1.rect.x+20 ,caverna1.rect.y+20),(200+20, 150+20), 10)
    pygame.draw.line(screen, BLACK, (caverna1.rect.x+20, caverna1.rect.y+20), (caverna3.rect.x+20, caverna3.rect.y+20), 10)
    pygame.draw.line(screen, BLACK, (caverna2.rect.x + 20, caverna2.rect.y + 20),(caverna4.rect.x + 20, caverna4.rect.y + 20), 10)
    pygame.draw.line(screen, BLACK, (caverna2.rect.x + 20, caverna2.rect.y + 20),(caverna5.rect.x + 20, caverna5.rect.y + 20), 10)
    pygame.draw.line(screen, BLACK, (caverna3.rect.x + 20, caverna3.rect.y + 20),(caverna6.rect.x + 20, caverna6.rect.y + 20), 10)
    pygame.draw.line(screen, BLACK, (caverna3.rect.x + 20, caverna3.rect.y + 20),(caverna7.rect.x + 20, caverna7.rect.y + 20), 10)


    # actualizar pantalla
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
