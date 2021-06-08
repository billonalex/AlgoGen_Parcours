import pygame

RESOLUTION = (1000, 1000)
WINDOW = pygame.display.set_mode(RESOLUTION)

class Level:
    def __init__(self, fichier):
        self.fichier = fichier
        self.tiles = []
        self.other_tiles = []
        self.start_pos = (0, 0)
        self.end_pos = (0, 0)

        self.generate()

    def generate(self):
        fichier_texte = open(self.fichier, "r")
        contenu = fichier_texte.read()
        j = 0
        k = 0
        for i in contenu:
            if i == "\n":
                j += 1
                k = 0
            if i == "#":
                self.tiles.append(pygame.Rect(k * 30, j * 30, 30, 30))
            if i == "*":
                self.start_pos = (k * 30, j*30)
                self.other_tiles.append(pygame.Rect(k * 30, j * 30, 30, 30))
            if i == "+":
                self.end_pos = (k * 30, j*30)
                self.other_tiles.append(pygame.Rect(k * 30, j * 30, 30, 30))
            k += 1
        fichier_texte.close()

    def draw(self):
        for i in self.tiles:
            pygame.draw.rect(WINDOW, (255, 0, 0), i)

        for i in self.other_tiles:
            pygame.draw.rect(WINDOW, (0, 255, 0), i)