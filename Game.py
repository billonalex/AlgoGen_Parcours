import pygame

from Level import Level
from Particle import Particle

RESOLUTION = (1500, 1000)
WINDOW = pygame.display.set_mode(RESOLUTION)

BLACK = (0, 0, 0)

POPULATION_SIZE = 1000
SIZE = 5

class Game:
    def __init__(self, path):
        self.level = Level(path)
        self.population = []
        self.generation = 1

        self.generate_first_population()

    def generate_first_population(self):
        for i in range(POPULATION_SIZE):
            self.population.append(Particle(pygame.Rect(self.level.start_pos[0], self.level.start_pos[1], SIZE, SIZE)))

        for j in self.population:
            j.generate_random_moves()

        return self.population

    def draw_particles(self):
        for i in self.population:
            i.draw()

    def move_particles(self, count):
        for i in self.population:
            i.move(self.level.tiles, count)

    def draw_window(self):
        WINDOW.fill(BLACK)
        self.level.draw()
        self.draw_particles()
        pygame.display.update()

    def quitAlgo(self):
        pygame.quit()
        quit()