import pygame
from constants import *
from fonts import base_font, heading_font, sub_heading_font

white = (255, 255, 255)

class IntroScreen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def draw(self, screen, final_score, highscore):
        if highscore:
            # Conditionally draw final score
            highscore_text = sub_heading_font.render(f'High score: {highscore}', False, white)
            screen.blit(highscore_text, ((SCREEN_WIDTH - highscore_text.get_width()) // 2, 100))
    
        if final_score:
            # Conditionally draw final score
            final_score_text = base_font.render(f'Score: {final_score}', False, white)
            screen.blit(final_score_text, ((SCREEN_WIDTH - final_score_text.get_width()) // 2, (SCREEN_HEIGHT - final_score_text.get_height()) //2 + 50))

        # Draw heading
        heading = heading_font.render('Asteroids' if not final_score else 'Game Over', False, white)
        screen.blit(heading, ((SCREEN_WIDTH - heading.get_width()) // 2, (SCREEN_HEIGHT - heading.get_height()) //2))

        # Draw space to start text
        intructions = base_font.render('Press Space to start', False, white)
        screen.blit(intructions, ((SCREEN_WIDTH - intructions.get_width()) // 2, (SCREEN_HEIGHT - intructions.get_height()) //2 + 100))


    def update(self, *args):
        pass