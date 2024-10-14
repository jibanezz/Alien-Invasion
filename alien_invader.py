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

    def always_going_left():
        if ship.moving_left == True:
            ship.rect.centerx -= 1

    def always_going_right():
        if ship.moving_right == True:
            ship.rect.centerx += 1

    from alien import Alien
    aliens = pygame.sprite.Group()
    a1 = Alien(screen, ai_settings)
    

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                sys.exit()
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                 elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
             elif event.type == pygame.KEYUP:
                 if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                 elif event.key == pygame.K_LEFT:
                    ship.moving_left = False
                
        # Make the most recently drawn screen visible.
         pygame.display.flip()
         screen.fill(ai_settings.bg_color)
         always_going_left()
         always_going_right()
         ship.blitme()
         a1.blitme()
    
run_game()