from typing import Any
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class that controls the bullets fired from the ship"""

    def __init__(self, space_game):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = space_game.screen
        self.settings = space_game.settings
        self.color = self.settings.bullet_color

        #Create a bullet rect at (0,0) then set it to current position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = space_game.ship.rect.midtop

        #Store the bullet position as a float
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the bullet up the screen"""
        self.y -= self.settings.bullet_speed
        #Update the rect position
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)