import sys
import pygame
from settings import Settings
from ship import Ship

class SpaceShooter:
    """A class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, create game resources"""
        pygame.init()

        #Set game's frame rate as clock
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        #Set game screen to 1200 x 800 pixels
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Space Shooter")

        self.ship = Ship(self)

    def run_game(self):
        """Create the main loop to run the game"""
        #Watch for keyboard and mouse events
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        """Update image on the screen, flip to new screen"""
        self.screen.fill(self.settings.background_color) 
        self.ship.blitme()

        #Make most recent screen visible
        pygame.display.flip()
         
         
if __name__ == '__main__':
    #Create a game instance and run the game
    ai = SpaceShooter()
    ai.run_game()