import pygame, os

class animacion:
    def __init__(self):
        self.run = True
        self.screen = None
        self.background = None
        self.font = None
        self.cavern = None
        self.truck = None
        self.business = None
        self.select = ""
        self.text = ""
        self.position_x = None
        self.position_y = None
        self.tree = None
        self.size = self.weight, self.height = 1420, 670
        self.ubicacion_actual = os.path.dirname(__file__)  # Where your .py file is located
        self.ubicacion_imagen = os.path.join(self.ubicacion_actual, '../Images')  # The image folder path
        self.cursor = None
        self.ColorActive = None
        self.ColorInactive = None
        self.Font = None
        self.textoImportante = ''
        self.clock = None
        self.lista_cuevas = []
        self.lista_carreteras = []

    def start(self):
        pygame.init()
        pygame.display.set_caption("Proyecto estructuras")
        self.clock = pygame.time.Clock()
        self.cavern = pygame.image.load(os.path.join(self.ubicacion_imagen))
