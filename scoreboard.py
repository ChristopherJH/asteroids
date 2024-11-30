import pygame
from constants import *
from fonts import base_font

white = (255, 255, 255)
off_white = (240, 240, 240)
dark_grey = (50, 50, 50)
health_red = (220, 20, 20)


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score = 0
    
    def increase_score(self):
        self.score += SCOREBOARD_ASTEROID_POINTS

    def draw(self, screen, health_percent):
        # Draw score
        score_text = base_font.render(f'Score: {self.score}', False, white)
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, (SCREEN_HEIGHT - score_text.get_height()) ))

        # Draw health bar
        health_bar_left = (SCREEN_WIDTH - HEALTHBAR_WIDTH) // 2
        health_bar_top = 50
        health_bar_background_border = pygame.Rect(health_bar_left - 4, health_bar_top - 4, HEALTHBAR_WIDTH + 8, HEALTHBAR_HEIGHT + 8)
        health_bar_background = pygame.Rect(health_bar_left,health_bar_top,  HEALTHBAR_WIDTH, HEALTHBAR_HEIGHT)
        health_bar_health = pygame.Rect(health_bar_left, health_bar_top, HEALTHBAR_WIDTH * (health_percent / 100), HEALTHBAR_HEIGHT)
        pygame.draw.rect(screen, off_white, health_bar_background_border, 0, 0) 
        pygame.draw.rect(screen, dark_grey, health_bar_background, 0, 0)
        pygame.draw.rect(screen, health_red, health_bar_health, 0, 0)

        # Draw health text
        health_text = base_font.render(f'{int(health_percent)}%', False, white)
        screen.blit(health_text, (SCREEN_WIDTH // 2 - health_text.get_width() // 2, health_bar_top - health_text.get_height() - 5))

    def update(self, *args):
        pass