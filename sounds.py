import pygame

pygame.mixer.init()
pygame.mixer.set_num_channels(16)  # Set the number of channels

# Load sound files
shoot_sound = pygame.mixer.Sound('assets/shoot.wav')
explosion_1_sound = pygame.mixer.Sound('assets/explosion.wav')
explosion_2_sound = pygame.mixer.Sound('assets/explosion_2.wav')
rocket_engine_sound = pygame.mixer.Sound('assets/rocket_engine.wav')
background_music_1 = pygame.mixer.Sound('assets/background_music_1.wav')
collision_sound = pygame.mixer.Sound('assets/collision.wav')