import pygame
from level_manager import Level
from levels import level_grids
from player import Player
from enemy_manager import Enemies

pygame.init()

clock = pygame.time.Clock()
fps = 60

width = 1200
height = 900

root = pygame.display.set_mode((width, height))

run = True
level = Level(level_grids[0], "ground.jpg", "lava.png", "coin.png", "door.png", "eleavtor.png")
previous_level = 1
enemies = Enemies(level_grids[0], "enemy.png")
enemy_group = enemies.get_enemies()
player = Player("bario.png", 12, 24, [100, 0], (59, 76), 2.3)

while run:

    root.fill("black")
    platform_list = level.printGrid(root)

    for enemy in enemy_group:
        if player.rect.colliderect(enemy.rect):
            enemy.speed = enemy.start_speed
            player.die(root, enemy_group)
            break
        enemy.show(root)
        enemy.move(platform_list, root)
    player.show(root)
    player.move(platform_list, enemy_group, root)

    if previous_level != player.currentLevel:
        enemies = Enemies(level_grids[player.currentLevel - 1], "enemy.png")
        enemy_group = enemies.get_enemies()

    previous_level = player.currentLevel

    level = Level(level_grids[player.currentLevel - 1], "ground.jpg", "lava.png", "coin.png", "door.png", "eleavtor.png")

    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
