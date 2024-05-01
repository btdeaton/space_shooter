import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

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

        #Create instance to store game statistics
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Create the main loop to run the game"""
        #Watch for keyboard and mouse events
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
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
            
        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """Respond to alien/bullet collisions"""
        #Check if any bullets have hit aliens, if so get rid of both
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        #If fleet is destroyed, destroy all bullets and create new fleet
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """Create the fleet of aliens"""
        #Create an alien and keep adding aliens until there is no room left
        #Space between aliens is one alien width and one alien height
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            #Finish row, reset x value, increment y value
            current_x = alien_height
            current_y += 2 * alien_height

    def _check_fleet_edges(self):
        """If the fleet hits an edge, respond"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change its direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """Check if fleet is at the edge, then update the postion of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        #Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print('Ship Hit!!!')

    def _update_screen(self):
        """Update image on the screen, flip to new screen"""
        self.screen.fill(self.settings.background_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet() 
        self.ship.blitme()
        self.aliens.draw(self.screen)

        #Make most recent screen visible
        pygame.display.flip()
         

if __name__ == '__main__':
    #Create a game instance and run the game
    ai = SpaceShooter()
    ai.run_game()