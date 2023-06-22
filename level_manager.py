import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, image, x, y, gridspot):
        pygame.sprite.Sprite.__init__(self)
        self.grid_spot = gridspot
        self.rawImage = image
        self.image = pygame.transform.scale(pygame.image.load(self.rawImage).convert_alpha(), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Level:
    def __init__(self, grid, platformImage, fireImage, coinImage, winImage, eleavtorImage):
        self.platform_image = platformImage
        self.fire_image = fireImage
        self.coin_image = coinImage
        self.win_image = winImage
        self.eleavtor_image = eleavtorImage
        self.image = pygame.image.load(platformImage)
        self.grid = grid
        self.rect = self.image.get_rect()

    def printGrid(self, root):
        self.rect.centerx = 25
        self.rect.y = -50

        platform_group = pygame.sprite.Group()
        for i, row in enumerate(self.grid):
            if row[0] == "pos":
                continue

            for j, column in enumerate(row):

                if column == 1:

                    pl = Platform(self.platform_image, self.rect.x, self.rect.y, [i, j])
                    platform_group.add(pl)
                elif column == 2:
                    pl = Platform(self.fire_image, self.rect.x, self.rect.y, [i, j])
                    platform_group.add(pl)
                elif column == 3:
                    pl = Platform(self.coin_image, self.rect.x, self.rect.y, [i, j])
                    platform_group.add(pl)
                elif column == 4:
                    pl = Platform(self.win_image, self.rect.x, self.rect.y, [i, j])
                    platform_group.add(pl)
                elif column == 6:
                    pl = Platform(self.eleavtor_image, self.rect.x, self.rect.y, [i, j])
                    platform_group.add(pl)
                self.rect.centerx += 50
            self.rect.centerx = 25
            self.rect.centery += 50
        platform_group.draw(root)
        return platform_group



