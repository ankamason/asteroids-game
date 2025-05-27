import pygame

from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    
    # Initialize delta time
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Set up Player to automatically join both groups
    Player.containers = (updatable, drawable)
    
    # Create the player - it will automatically join the groups!
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Game loop
    while True:
        # Handle events (like closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update ALL updatable objects with one line!
        updatable.update(dt)
        
        # Fill screen with black
        screen.fill("black")
        
        # Draw ALL drawable objects
        for sprite in drawable:
            sprite.draw(screen)
        
        # Refresh the display
        pygame.display.flip()
        
        # Limit to 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
