import pygame
from level_manager import Level
from level1 import level1_grid
from player import Player
pygame.init()

clock = pygame.time.Clock()
fps = 60

width = 900
height = 900

root = pygame.display.set_mode((width, height))

run = True
level1 = Level(level1_grid,"ground.jpg")
player = Player("bario.png", 15, 150, [100, 0], (59,76),10)

while run:
    root.fill("black")
    platform_list = level1.printGrid(root)
    player.show(root)
    player.move(platform_list, root)


    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
