import random
import pygame

from src.ui.circle_shape import CircleShape
from src.utils.constants import *
from src.utils.sounds import explosion_2_sound, explosion_1_sound

explosion_2_sound.set_volume(0.2)

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.vertices = self.generate_vertices()

    def generate_vertices(self):
        vertices = []
        for i in range(ASTEROID_VERTICES_RESOLUTION):  # Number of vertices
            angle = i * (360 / ASTEROID_VERTICES_RESOLUTION)
            distance = random.uniform(self.radius * 0.7, self.radius * 1.3)
            vertex = pygame.Vector2(distance, 0).rotate(angle) + self.position
            vertices.append(vertex)
        return vertices
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.vertices, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.vertices = [vertex + self.velocity * dt for vertex in self.vertices]

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            explosion_2_sound.play()
            return
        
        explosion_1_sound.play()
        breakoff_angle = random.uniform(20, 50)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid_1.velocity = self.velocity.rotate(breakoff_angle) * 1.2
        asteroid_2.velocity = self.velocity.rotate(-breakoff_angle) * 1.2

    def collide_with_asteroid(self, asteroid_2):
        explosion_2_sound.play()

        if self.radius <= asteroid_2.radius:
            self.kill()
        elif asteroid_2.radius <= self.radius:
            asteroid_2.kill()
        else:
            self.kill()
            asteroid_2.kill()


