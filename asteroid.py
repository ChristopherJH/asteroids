import random
import pygame

from circleshape import CircleShape
from constants import *
from sounds import explosion_2_sound, explosion_1_sound

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        # Simply kill asteroid if min radius
        if (self.radius <= ASTEROID_MIN_RADIUS):
            explosion_2_sound.play()
            return
        
        explosion_1_sound.play()        
        breakoff_angle = random.uniform(20, 50)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid_1.velocity = self.velocity.rotate(breakoff_angle) * 1.2
        asteroid_2.velocity = self.velocity.rotate(-breakoff_angle) * 1.2
