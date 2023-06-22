import pygame
from level_manager import Level
from levels import level_grids
level = Level(level_grids[0], "ground.jpg", "lava.png", "coin.png", "door.png")
pygame.init()

clock = pygame.time.Clock()
fps = 60

width = 1200
height = 900

root = pygame.display.set_mode((width, height))


class Enemy:
    def __init__(self, image, size, startpos, speed, gravity):
        self.start_pos = startpos
        self.image = image
        self.enemy = pygame.image.load(self.image).convert_alpha()
        self.size = size
        self.enemy = pygame.transform.scale(self.enemy, size)
        self.rect = self.enemy.get_rect()
        self.rect.x = self.start_pos[0]
        self.rect.y = self.start_pos[1]
        self.speed = speed
        self.gravity = gravity

    def show(self, root):
        root.blit(self.enemy, self.rect)

    def move(self, platform_list, root):
        dx = 0
        dy = self.gravity
        if self.rect.x >= root.get_width() - 55:
            self.speed = -self.speed
        elif self.rect.x <= 0:
            self.speed = -self.speed
        for platform in platform_list:
            if(self.rect.colliderect(
                    (platform.rect.x, platform.rect.y + 30, platform.rect.width,
                     platform.rect.height))):
                dx = 1.2
                dy = -60
                break
            if self.rect.colliderect(platform):
                dx = self.speed
                dy = 0
                break

        self.rect.x += dx
        self.rect.y += dy


enemy = Enemy('enemy.png', [52, 72], [10, 500], 5, 4)

run = True
while run:

    root.fill((0,0,0))
    platform_list = level.printGrid(root)
    enemy.show(root)
    enemy.move(platform_list, root)
    clock.tick(fps)
    pygame.display.update()
