import pygame
from setting import Settings
import sys
from ship import Ship

def run_game():
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                sys.exit()
                
        # Make the most recently drawn screen visible.
         pygame.display.flip()
         screen.fill(ai_settings.bg_color)
         ship.blitme()
    
run_game()