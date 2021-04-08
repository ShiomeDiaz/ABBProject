import pygame
import math
import numpy as np

class Game(object):
    def __init__(self, ancho_juego, alto_juego):
        pygame.display.set_caption('ABB marca ACME')
        self.ancho_juego = ancho_juego
        self.alto_juego = alto_juego
        self.display_juego = pygame.display.set_mode((ancho_juego, alto_juego), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.fondo = pygame.image.load('../Images/background.jpg').convert()
        self.display_juego.blit(self.fondo, (0, 0))


class Camion(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cambio_x = 20
        self.cambio_y = 0
        self.ruta = []
        # self.posicion = []
        # self.posicion.append([self.x, self.y])
        self.camion = pygame.image.load('../Images/camion.png').convert()
        self.camion.set_colorkey([0, 0, 0])

    def displayCamion(self, game):
        game.display_juego.blit(self.camion, (self.x, self.y))

    def asignarDireccionDeMovimiento(self):
        # Esto es operaciones entre vectores, hace que se pueda mover de una cueva a otra
        distancia = math.sqrt(((self.x - self.ruta[0].x) ** 2) + ((self.y - self.ruta[0].y) ** 2))
        self.movimientoX = ((self.x - 10 - (self.ruta[0].x - 10)) / distancia) * 50 * -1
        self.movimientoY = ((self.y - 10 - (self.ruta[0].y - 10)) / distancia) * 50 * -1

    def mover(self):
        self.x += self.movimientoX
        self.y += self.movimientoY
        pygame.display.update()

class Cueva(object):

    def __init__(self,x, y, anchura):
        self.x = x
        self.y = y
        self.posicion = (x, y)
        self.anchura = anchura
        self.cuevaImage = pygame.image.load('../Images/cueva.png')
        self.cuevaImage.set_colorkey([0, 0, 0])

    def displayCueva(self, game):
        game.display_juego.blit(self.cuevaImage, (self.x, self.y))

    def dibujarCuevas(self, cuevas, game):
        for cueva in cuevas:
            cueva.displayCueva(game)

def asignarRutaCarro( camion, cuevas):
        for cueva in cuevas:
            camion.ruta.append(cueva)

def hacerRutaAsignadaCarro(camion):
        # Si hay rutas por hacer
        if len(camion.ruta) > 0:
            # Si el carro esta en la misma posicion de la cueva
            if camion.ruta[0]:
                # Elimina esta ruta, por que ya llego, pero continua con la otra cueva, si hay
                print("Colision, llego a una cueva")
                camion.ruta.pop(0)
            # Si el carro todavia no ha llegado a la cueva
            else:
                camion.asignarDireccionDeMovimiento()
                camion.mover()





# ciclo runner

def run():
    pygame.init()
    clock = pygame.time.Clock()
    encendido = True

    cuevas = []
    # cueva1 = [300, 50, 50]
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
    rutaCueva.append(cueva4)
    game = Game(650, 490)
    camion = Camion(50, 50)
    camion.displayCamion(game)
    cueva = Cueva(0, 0, 0)
    cueva.dibujarCuevas(cuevas, game)
    asignarRutaCarro(camion,rutaCueva)


    while encendido:

        # cueva = Cueva(cueva1[0], cueva1[1], cueva1[2])

        #cueva.displayCueva(game)
        clock.tick(60)
        #pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                encendido = False
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_s]:
                encendido = False
            if teclas[pygame.K_m]:
                hacerRutaAsignadaCarro(camion)

        pygame.display.flip()
        pygame.display.update()


    pygame.quit()


if __name__ == '__main__':
    run()