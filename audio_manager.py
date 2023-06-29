import pygame


def play_background_music(filename, volume=1):
    if not pygame.mixer.get_init(): pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)


def play_sound_effects(filename, volume=1):
    if not pygame.mixer.get_init(): pygame.mixer.init()
    sound_effect = pygame.mixer.Sound(filename)
    sound_effect.set_volume(volume)
    sound_effect.play()
