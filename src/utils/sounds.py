import pygame

pygame.mixer.init()
pygame.mixer.set_num_channels(16)

# Load sound files
shoot_sound = pygame.mixer.Sound('assets/sounds/shoot.wav')
explosion_1_sound = pygame.mixer.Sound('assets/sounds/explosion.wav')
explosion_2_sound = pygame.mixer.Sound('assets/sounds/explosion_2.wav')
rocket_engine_sound = pygame.mixer.Sound('assets/sounds/rocket_engine.wav')
background_music_1 = pygame.mixer.Sound('assets/sounds/background_music_1.wav')
collision_sound = pygame.mixer.Sound('assets/sounds/collision.wav')