import pygame

from Game import Game

GO = True
COUNT = 0

game = Game("level1.txt")

while GO:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GO = False

    game.move_particles(COUNT)

    COUNT += 1
    if(COUNT >= 99):
        COUNT = 0

    game.draw_window()
    
game.quitAlgo()