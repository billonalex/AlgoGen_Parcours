import pygame
import random

RESOLUTION = (1000, 1000)
WINDOW = pygame.display.set_mode(RESOLUTION)

SPEED_X = 1
SPEED_Y = 1

NUMBER_OF_MOVES = 100

def get_random_pos(a, b):
    return random.randint(a, b)

class Particle:
    ID = 0
    def __init__(self, rect):
        Particle.ID += 1
        self.color = (get_random_pos(0,255), get_random_pos(0,255), get_random_pos(0,255))
        self.ID = Particle.ID
        self.rect = rect
        self.moves = []

    def move(self, tiles, count):
        self.rect.x += self.moves[count][0]
        self.rect.y += self.moves[count][1]

        coll = False
        for tile in tiles:
            if self.rect.colliderect(tile):
                coll = True

    def draw(self):
        pygame.draw.rect(WINDOW, self.color, self.rect)

    def collide(self, rect):
        return self.rect.colliderect(rect)
        
    def generate_random_moves(self):
        for i in range(NUMBER_OF_MOVES):
            self.moves.append((get_random_pos(-SPEED_X, SPEED_X), get_random_pos(-SPEED_Y, SPEED_Y)))

