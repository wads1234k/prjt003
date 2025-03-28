import pygame
import sys
from game.game_logic import GameLogic

def main():
    pygame.init()
    
    # Set up the game window
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Brick Breaker Game")
    
    # Initialize the game logic
    game = GameLogic(screen, ball_speed=5, lives=1)  # Increase ball speed and set lives to 1
    
    # Set background color to light sky blue
    screen.fill((220, 240, 255))  # RGB for light sky blue
    
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        game.update()
        game.draw()
        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()