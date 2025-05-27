
import pygame

from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    
    pygame.init()
    
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
   
    clock = pygame.time.Clock()
    
   
    dt = 0
    
    # Game loop
    while True:
        # Handle events (like closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill screen with black
        screen.fill("black")
        
        # Refresh the display
        pygame.display.flip()
        
        # Limit to 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()


