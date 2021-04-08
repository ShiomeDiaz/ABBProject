import pygame
import random
import math


class Cueva:
    def __init__(self, xPos, yPos, anchura):
        self.x = xPos
        self.y = yPos
        self.anchura = anchura
        self.color = (100, 100, 100)
        # Es importante para detectar colisiones
        self.rect = pygame.Rect(self.x, self.y, self.anchura, self.anchura)

    def dibujar(self, pantalla):
        # Dibuja un cuadrado (pantalla,color,x,y,anchura,altura)
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.anchura, self.anchura))


class Carro:
    def __init__(self, xPos, yPos):
        self.x = xPos
        self.y = yPos
        self.anchura = 50
        self.color = (200, 150, 200)
        self.x_pivote = 0
        self.y_pivote = 0
        self.ruta = []
        # Es importante para detectar colisiones
        #  self.rect = pygame.Rect(self.x, self.y, self.anchura, self.anchura)
        self.carro = pygame.image.load("camion.png").convert()


    def dibujar(self, pantalla):
        # Dibuja un cuadrado (pantalla,color,x,y,anchura,altura)
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.anchura, self.anchura))

    def asignarDireccionDeMovimiento(self):
        # Esto es operaciones entre vectores, hace que se pueda mover de una cueva a otra
        distancia = math.sqrt(((self.x - self.ruta[0].x) ** 2) + ((self.y - self.ruta[0].y) ** 2))
        self.movimientoX = ((self.x - 10 - (self.ruta[0].x - 10)) / distancia) * 50 * -1
        self.movimientoY = ((self.y - 10 - (self.ruta[0].y - 10)) / distancia) * 50 * -1

    def mover(self):
        self.x += self.movimientoX
        self.y += self.movimientoY
        # self.rect = pygame.Rect(self.x, self.y, self.anchura, self.anchura)
        #self.carro


def dibujarCuevas(cuevas, pantalla):
    for cueva in cuevas:
        cueva.dibujar(pantalla)


def asignarRutaCarro(carro, cuevas):
    for cueva in cuevas:
        carro.ruta.append(cueva)


def hacerRutaAsignadaCarro(carro):
    # Si hay rutas por hacer
    if len(carro.ruta) > 0:
        # Si el carro esta en la misma posicion de la cueva
        if carro.ruta[0].rect.colliderect(carro.rect):
            # Elimina esta ruta, por que ya llego, pero continua con la otra cueva, si hay
            print("Colision, llego a una cueva")
            carro.ruta.pop(0)
        # Si el carro todavia no ha llegado a la cueva
        else:
            carro.asignarDireccionDeMovimiento()
            carro.mover()


pygame.init()
pantalla = pygame.display.set_mode((650, 490))
background = pygame.image.load("background.jpg").convert()
carrito = pygame.image.load("camion.png").convert()
carrito.set_colorkey([0, 0, 0])
pygame.display.set_caption("")
reloj = pygame.time.Clock()
encendido = True

cuevas = []

cueva1 = Cueva(300, 50, 50)
cueva2 = Cueva(200, 150, 50)
cueva3 = Cueva(400, 150, 50)
cueva4 = Cueva(100, 250, 50)
cueva5 = Cueva(250, 250, 50)
cueva6 = Cueva(350, 250, 50)
cueva7 = Cueva(500, 250, 50)

cuevas.append(cueva1)
cuevas.append(cueva2)
cuevas.append(cueva3)
cuevas.append(cueva4)
cuevas.append(cueva5)
cuevas.append(cueva6)
cuevas.append(cueva7)

rutaCueva = []
rutaCueva.append(cueva1)
rutaCueva.append(cueva2)
rutaCueva.append(cueva3)


carro = Carro(50, 50)
asignarRutaCarro(carro, rutaCueva)

print("Presione s para salir")
print("Presione m para mover carro")

while encendido:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            encendido = False
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_s]:
            encendido = False
        if teclas[pygame.K_m]:
            hacerRutaAsignadaCarro(carro)

    pantalla.blit(background, [0, 0])
    pantalla.blit(carrito, [carro.x, carro.y])
    reloj.tick(30)
    dibujarCuevas(cuevas, pantalla)
    #carro.dibujar(pantalla)

    pygame.display.flip()
pygame.quit()
