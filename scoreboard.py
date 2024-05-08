import pygame.font

class Scoredboard:
    """A class to display the score, level, and lives"""
    def __init__(self, space_game):
        """Initialize scoreboard information"""
        self.screen = space_game.screen
        self.screen_rect = space_game.screen.get_rect()
        self.settings = space_game.settings
        self.stats = space_game.stats

        #Font settings for score display
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #Prepare initial score image
        self.prep_score()
        self.prep_high_score()
    
    def prep_score(self):
        """Turn the score into a rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.background_color)

        #Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def show_score(self):
        """Draw the score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)