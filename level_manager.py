import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Level:
    def __init__(self, grid, image):
        self.image_string = image
        self.image = pygame.image.load(image).convert_alpha()
        self.grid = grid
        self.rect = self.image.get_rect()

    def printGrid(self, root):
        self.rect.centerx = 25
        self.rect.y = -50
        platform_group = pygame.sprite.Group()
        for row in self.grid:

            for column in row:

                if column == 1:
                    pl = Platform(self.image_string, self.rect.x, self.rect.y)
                    platform_group.add(pl)
                    # root.blit(self.image, self.rect)
                self.rect.centerx += 50
            self.rect.centerx = 25
            self.rect.centery += 50
        platform_group.draw(root)
        return platform_group
