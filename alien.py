import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent an alien in the fleet."""
    def __init__(self,screen, ai_settings ):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/alien.jpg')
        self.rect = self.image.get_rect()

        # Start each new alien at a random x-coordinate.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)