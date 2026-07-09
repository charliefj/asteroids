import pygame
from logger import log_state, log_event
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    #initialise pygame
    pygame.init()

    #screen object from display class, setting size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #create an object to help track time, helps fps
    clock = pygame.time.Clock()
    dt= 0.0
    
    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #classes in groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    #game loop
    while True:
        #logs data in a jsonl file for bootdev to confirm it works
        log_state()

        #closes the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        #every frame makes screen black, prevents smearing
        screen.fill("Black")

        #player.draw(screen)
        for thing in drawable:
            thing.draw(screen)
        
        #update all in the update group
        updatable.update(dt)

        #when shot hits rock
        for rock in asteroids:
            for shot in shots:
                if rock.collides_with(shot):
                    log_event("asteroid_shot")
                    rock.split()
                    shot.kill()

        #when rock hits a player, game over bro
        for rock in asteroids:
            if rock.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        pygame.display.flip()

        dt = clock.tick(60) / 1000    

if __name__ == "__main__":
    main()
