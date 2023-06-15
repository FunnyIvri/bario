import random
from text import Textcreator
import pygame
import keyboard
from levels import level_grids


class Player:
    def __init__(self, image, speed, jump_height, start_pos, size, gravity):
        self.gravity = gravity
        self.image = image
        self.coinCount = 0
        self.currentLevel = 1
        self.speed = speed
        self.jump_height = jump_height
        self.start_pos = start_pos
        self.player = pygame.image.load(self.image).convert_alpha()
        self.size = size
        self.player = pygame.transform.scale(self.player, size)
        self.rect = self.player.get_rect()
        self.rect.x = self.start_pos[0]
        self.rect.y = self.start_pos[1]
        self.cointouch = False
        self.velocity = 0.1
        self.start_pos = level_grids[self.currentLevel - 1][0][1], level_grids[self.currentLevel - 1][0][2]
        self.rect.x = self.start_pos[0]
        self.rect.y = self.start_pos[1]
        self.deathCount = 0

    def die(self, root):
        time = 0
        dead = True
        root.fill("red")
        font = pygame.font.SysFont("inkfree", 200)
        text = font.render("YOU", True, "black")
        text1 = font.render("ARE", True, "black")
        text2 = font.render("DEAD", True, "black")
        # RECT
        textRect = text.get_rect()
        textRect.center = (400, 200)
        # RECT1
        textRect1 = text1.get_rect()
        textRect1.center = (400, 400)
        # RECT2
        textRect2 = text2.get_rect()
        textRect2.center = (400, 600)
        # Clock
        fps = pygame.time.Clock()
        Max_Fps = 2
        change = True
        while dead:
            if time >= 3:
                self.start_pos = level_grids[self.currentLevel - 1][0][1], level_grids[self.currentLevel - 1][0][2]
                self.rect.x = self.start_pos[0]
                self.rect.y = self.start_pos[1]
                self.coinCount = 0
                self.deathCount += 1
                break
            time = time + 1
            if change:
                root.fill("white")
            else:
                root.fill("red")
            change = not change
            root.blit(text, textRect)
            root.blit(text1, textRect1)
            root.blit(text2, textRect2)
            fps.tick(Max_Fps)
            pygame.display.update()

    def win(self,root):
        root.fill((51, 106, 92))
        wintext = Textcreator("YOU WIN!", 100, (root.get_width() // 2, root.get_height() // 2 - 200), root, (0, 255, 0))
        wintext.createText()
        won = True
        rect = pygame.image.load("win.png").get_rect()
        while won:
            rect.centerx = root.get_width() // 2
            rect.centery = root.get_height() // 2
            root.blit(pygame.image.load("win.png"), rect)
            pygame.display.update()

    def show(self, root):
        root.blit(self.player, self.rect)

    def checks(self, platform, root):

        if platform.rawImage == "coin.png" and not self.cointouch:
            level_grids[self.currentLevel - 1][platform.grid_spot[0]][platform.grid_spot[1]] = 0
            self.cointouch = True
            self.coinCount += 1
        if platform.rawImage == "door.png":
            if self.currentLevel+1 == len(level_grids)+1: self.win(root)
            self.start_pos = level_grids[self.currentLevel][0][1], level_grids[self.currentLevel][0][2]
            self.rect.x = self.start_pos[0]
            self.rect.y = self.start_pos[1]
            print(self.currentLevel == len(level_grids))
            self.currentLevel += 1

    def move(self, platform_list, root):
        coinCounter = Textcreator("coins: " + str(self.coinCount), 50, (70, 70), root)
        deathCounter = Textcreator("deaths: " + str(self.deathCount), 50, (80, 140), root)
        deathCounter.createText()
        coinCounter.createText()

        root_size = [root.get_width(), root.get_height()]
        if self.velocity >= 5:
            self.velocity = 5
        dx = 0
        dy = self.velocity
        self.velocity += self.gravity

        # if keyboard.is_pressed("left") and not self.rect.left <= 1 and self.rect.colliderect(platform.rect.x,platform.rect.y+10,platform.rect.width,platform.rect.height) and platform.rect.left <= self.rect.left <= platform.rect.left + 80:

        if keyboard.is_pressed("right") and not self.rect.right >= root_size[0]:
            dx = self.speed
        elif keyboard.is_pressed("left") and not self.rect.left <= 1:
            dx = -self.speed

        self.cointouch = False
        for platform in platform_list:

            # right
            if self.rect.colliderect(
                    (platform.rect.x + 10, platform.rect.y + 30, platform.rect.width,
                     platform.rect.height)) and not platform.rawImage == "none.png":
                # right hit

                self.checks(platform, root)
                dx = 1

            # left
            if self.rect.colliderect(
                    (platform.rect.x, platform.rect.y + 30, platform.rect.width,
                     platform.rect.height)) and not platform.rawImage == "none.png":
                self.checks(platform, root)
                dx = -1

            if self.rect.colliderect(platform.rect) and self.rect.bottom <= platform.rect.centery:
                self.checks(platform, root)
                self.velocity = 0

                if platform.rawImage == "lava.png":
                    self.die(root)
        if keyboard.is_pressed("up"):
            for platform in platform_list:
                if self.rect.colliderect(platform.rect) and self.rect.bottom <= platform.rect.centery:
                    self.velocity += -self.jump_height
        coinCounter.createText()
        self.rect.x += dx
        self.rect.y += dy
