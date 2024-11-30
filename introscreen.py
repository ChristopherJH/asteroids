import pygame
from constants import *
from fonts import base_font, heading_font

white = (255, 255, 255)

class IntroScreen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def draw(self, screen):
        # Draw heading
        heading = heading_font.render('Asteroids', False, white)
        screen.blit(heading, ((SCREEN_WIDTH - heading.get_width()) // 2, (SCREEN_HEIGHT - heading.get_height()) //2))

        # Draw space to start text
        intructions = base_font.render('Press \'Space\' to start', False, white)
        screen.blit(intructions, ((SCREEN_WIDTH - intructions.get_width()) // 2, (SCREEN_HEIGHT - intructions.get_height()) //2 + 100))


    def update(self, *args):
        pass