import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for entity in updatable:
            entity.update(dt)
        
        for asteriod in asteroids:
            if asteriod.collision(player):
                sys.exit("Game over!")
            for shot in shots:
                if shot.collision(asteriod):
                    asteriod.split()
                    shot.kill()

        screen.fill("black")
        
        for entity in drawable:
            entity.draw(screen)

        for entity in asteroids:
            entity.draw(screen)

        for entity in shots:
            entity.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()