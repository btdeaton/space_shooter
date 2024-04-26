import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

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
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Create the main loop to run the game"""
        #Watch for keyboard and mouse events
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                    
    def _check_keydown_events(self, event):
        """If key is pressed down, update the flags"""
        #If right key is pressed, move ship over 1 pixel
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        #If left key is pressed, move left 1 pixel
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        #If Q is pressed quit the game
        elif event.key == pygame.K_q:
            sys.exit()
        #If spacebar is pressed fire bullet
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """If key is released, update the flags"""
        #If right key released, stop moving
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        #If left key released, stop moving
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        #Update bullet positions
        self.bullets.update()

        #Get rid of bullets that have gone off screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
                


    def _update_screen(self):
        """Update image on the screen, flip to new screen"""
        self.screen.fill(self.settings.background_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet() 
        self.ship.blitme()

        #Make most recent screen visible
        pygame.display.flip()
         

if __name__ == '__main__':
    #Create a game instance and run the game
    ai = SpaceShooter()
    ai.run_game()