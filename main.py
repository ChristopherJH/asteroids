import pygame

from sounds import background_music_1
from asteroid import Asteroid
from scoreboard import Scoreboard
from shot import Shot
from asteroidfield import AsteroidField
from constants import *
from player import Player

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Asteroids')


dt = 0


def main():
    print("Starting asteroids!")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids: list[Asteroid] = pygame.sprite.Group()
    shots: list[Shot] = pygame.sprite.Group()

    Scoreboard.containers = (updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    scoreboard = Scoreboard()
    updatable.add(scoreboard)
    drawable.add(scoreboard)
    asteroid_field = AsteroidField()

    dt = 0 

    background_music_1.play(-1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)

        screen.fill("black")
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over! High score: ", scoreboard.score)
                return
            
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    scoreboard.increase_score()
                    asteroid.split()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
