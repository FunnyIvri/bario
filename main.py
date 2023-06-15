import pygame
from level_manager import Level
from levels import level_grids
from player import Player


pygame.init()

clock = pygame.time.Clock()
fps = 60

width = 1200
height = 900

root = pygame.display.set_mode((width, height))

run = True
level = Level(level_grids[0], "ground.jpg", "lava.png", "coin.png", "door.png")

player = Player("bario.png", 12, 12, [100, 0], (59, 76), 2)

while run:

    root.fill("black")
    platform_list = level.printGrid(root)
    player.show(root)
    player.move(platform_list, root)

    level = Level(level_grids[player.currentLevel - 1], "ground.jpg", "lava.png", "coin.png", "door.png")


    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
