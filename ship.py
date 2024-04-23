import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, space_game):
        """Initialize a ship and set its starting position"""
        
        self.screen = space_game.screen
        self.screen_rect = space_game.screen.get_rect()

        #Get the ship image and draw it's rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start new ship at center of bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)