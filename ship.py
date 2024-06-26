import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship"""

    def __init__(self, space_game):
        """Initialize a ship and set its starting position"""
        super().__init__()

        self.screen = space_game.screen
        self.settings = space_game.settings
        self.screen_rect = space_game.screen.get_rect()

        #Get the ship image and draw it's rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start new ship at center of bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a float for ship's exact horizontal position
        self.x = float(self.rect.x)

        #Flag for ship movement, start with not moving
        self.moving_right = False
        self.moving_left = False

        #Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

    def update(self):
        """Update the ship's position based on the movement flag"""
        #Update ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #Update ship's rect based off x position
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship in the middle bottom of screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)