import pygame


class Enemies:
    def __init__(self, grid, enemy_image):

        self.image_path = enemy_image
        self.image = pygame.image.load("src/ground.jpg")
        self.grid = grid
        self.rect = self.image.get_rect()

    def get_enemies(self):
        self.rect.centerx = 25
        self.rect.y = -50

        enemy_group = []
        for i, row in enumerate(self.grid):
            if row[0] == "pos":
                continue

            for j, column in enumerate(row):
                if column == 5:
                    enemy_group.append(Enemy(self.image_path, [52, 72], [self.rect.x, self.rect.y], 5, 4))
                self.rect.centerx += 50
            self.rect.centerx = 25
            self.rect.centery += 50
        return enemy_group


class Enemy:
    def __init__(self, image, size, startpos, speed, gravity):
        self.start_speed = speed
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
            if platform.rawImage == "src/coin.png": continue
            elif platform.rawImage == "src/door.png": continue

            if (self.rect.colliderect(
                    (platform.rect.x, platform.rect.y + 30, platform.rect.width,
                     platform.rect.height))):
                dx = 1.2
                dy = -60
                break
            if self.rect.colliderect(platform):
                if platform.rawImage == "src/eleavtor.png":
                    self.rect.y -= 135
                    self.speed = -self.speed
                    continue
                dx = self.speed
                dy = 0
                break

        self.rect.x += dx
        self.rect.y += dy