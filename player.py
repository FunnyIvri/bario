import pygame
import keyboard


class Player:
    def __init__(self, image, speed, jump_height, start_pos, size, gravity):
        self.gravity = gravity
        self.image = image
        self.speed = speed
        self.jump_height = jump_height
        self.start_pos = start_pos
        self.player = pygame.image.load(self.image).convert_alpha()
        self.size = size
        self.player = pygame.transform.scale(self.player, size)
        self.rect = self.player.get_rect()
        self.rect.x = self.start_pos[0]
        self.rect.y = self.start_pos[1]

    def show(self, root):
        root.blit(self.player, self.rect)

    def move(self, platform_list, root):
        root_size = [root.get_height(), root.get_width()]
        dx = 0
        dy = self.gravity

        # if keyboard.is_pressed("left") and not self.rect.left <= 1 and self.rect.colliderect(platform.rect.x,platform.rect.y+10,platform.rect.width,platform.rect.height) and platform.rect.left <= self.rect.left <= platform.rect.left + 80:

        if keyboard.is_pressed("right") and not self.rect.right >= root_size[0]:
            dx = self.speed
        elif keyboard.is_pressed("left") and not self.rect.left <= 1:
            dx = -self.speed
        for platform in platform_list:

            if self.rect.colliderect(
                    (platform.rect.x + 10, platform.rect.y + 30, platform.rect.width, platform.rect.height)):
                print("right hit")
                dx = 0
            if self.rect.colliderect(
                    (platform.rect.x, platform.rect.y + 30, platform.rect.width, platform.rect.height)):
                print("left hit")
                dx = 0
            if self.rect.colliderect(platform.rect):
                dy = 0
        if keyboard.is_pressed("up"):
            for platform in platform_list:
                if self.rect.colliderect(platform.rect) and self.rect.bottom <= platform.rect.centery:
                    dy = -self.jump_height
        self.rect.x += dx
        self.rect.y += dy
