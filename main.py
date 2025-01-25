import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField 

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))   
    clock = pygame.time.Clock()  # Ensure clock is defined here
    dt = 0

    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids  = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    player = Player( (SCREEN_WIDTH / 2) , (SCREEN_HEIGHT / 2) )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for update_obj in updatable:
            update_obj.update(dt)
        
        screen.fill("black")
        
        for draw_object in drawable:
            draw_object.draw(screen)
            
        # player.draw(screen)        
        pygame.display.flip()

        # Cap the frame rate to 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000.0 
        
if __name__ == "__main__":
    main()