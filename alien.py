import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""
    def __init__(self, space_game):
        super().__init__()
        self.screen = space_game.screen

        #Load the alien image and set its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the aliens exact horizontal position as a float
        self.x = float(self.rect.x)