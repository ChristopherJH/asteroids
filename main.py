import pygame

from sounds import background_music_1
from asteroid import Asteroid
from scoreboard import Scoreboard
from introscreen import IntroScreen
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

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    Scoreboard.containers = (updatable, drawable)
    
    scoreboard = Scoreboard()
    updatable.add(scoreboard)
    drawable.add(scoreboard)
    asteroid_field = AsteroidField()
    introScreen = IntroScreen()

    dt = 0
    is_play = False
    player = None

    background_music_1.play(-1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            keys = pygame.key.get_pressed()
            if not is_play and keys[pygame.K_SPACE]:
                player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                is_play = True
                for asteroid in asteroids:
                    asteroid.kill()

        
        for obj in updatable:
            obj.update(dt)

        screen.fill("black")
        for i, asteroid in enumerate(asteroids):
            if player and asteroid.collides_with(player):
                player.damage(asteroid.radius)

                if player.health <= 0:
                    print("Game over! Score:", scoreboard.score)
                    player.kill()
                    asteroid_field.kill()
                    is_play = False
                    
                
            asteroids_list = list(asteroids)
            if i < len(asteroids_list) - 1:
                for asteroid_2 in asteroids_list[i+1:]:
                    if asteroid.collides_with(asteroid_2):
                        asteroid.collide_with_asteroid(asteroid_2)
            
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    scoreboard.increase_score()
                    asteroid.split()

        for obj in drawable:
            if isinstance(obj, Scoreboard):
                if player and is_play is True:
                    obj.draw(screen, player.health / PLAYER_HEALTH * 100)
            else:
                obj.draw(screen)
        
        if not is_play:
            introScreen.draw(screen, scoreboard.score)


        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
