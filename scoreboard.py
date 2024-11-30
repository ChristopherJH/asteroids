import pygame
from constants import *

white = (255, 255, 255)

pygame.font.init()
font = pygame.font.Font('assets/PixelifySans.ttf', 32)


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score = 0
    
    def increase_score(self):
        self.score += SCOREBOARD_ASTEROID_POINTS

    def draw(self, screen):
        text = font.render(f'Score: {self.score}', False, white)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, (SCREEN_HEIGHT - text.get_height()) ))

    def update(self, *args):
        pass