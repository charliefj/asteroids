import pygame
from logger import log_state
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player

def main():
    #initialise pygame
    pygame.init()

    #screen object from display class, setting size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #create an object to help track time, helps fps
    clock = pygame.time.Clock()
    dt= 0.0
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

        player.draw(screen)
        player.update(dt)


        pygame.display.flip()

        dt = clock.tick(60) / 1000    

if __name__ == "__main__":
    main()
