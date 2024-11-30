import pygame

from circleshape import CircleShape
from shot import Shot
from constants import *
from sounds import shoot_sound, collision_sound

white = (255, 255, 255)

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0
        self.health = PLAYER_HEALTH
        self.damage_cooldown = 0
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        player_damage_cooldown_timer_factor = ((PLAYER_DAMAGE_COOLDOWN - self.damage_cooldown) / PLAYER_DAMAGE_COOLDOWN)
        player_colour = (255, 255 * player_damage_cooldown_timer_factor, 255 * player_damage_cooldown_timer_factor)
        pygame.draw.polygon(screen, player_colour, self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
       
        # Decrement shoot cooldown
        if self.shoot_cooldown - dt < 0:
            self.shoot_cooldown = 0
        else: 
             self.shoot_cooldown -= dt

        # Decrement damage cooldown
        if self.damage_cooldown - dt < 0:
            self.damage_cooldown = 0
        else: 
             self.damage_cooldown -= dt

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.shoot_cooldown > 0:
            return
        
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        shoot_sound.play()  # Play shooting sound

    def damage(self, damage):
        if self.damage_cooldown > 0:
            return
        self.health -= damage
        collision_sound.play()
        self.damage_cooldown = PLAYER_DAMAGE_COOLDOWN
        if self.health <= 0:
            self.kill()