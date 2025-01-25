import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))   
    clock = pygame.time.Clock()  # Ensure clock is defined here
    player = Player( (SCREEN_WIDTH / 2) , (SCREEN_HEIGHT / 2) )

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)

        screen.fill("black")
        player.draw(screen)        
        pygame.display.flip()

        # Cap the frame rate to 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000.0 
        
if __name__ == "__main__":
    main()