class Settings:
    """A class to store all settings for Space Shooter"""

    def __init__(self):
        """Initialize the settings for Space Shooter"""

        #Ship settings
        self.ship_speed = 1.5
        
        #Screen settings for width, height, and color
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230, 230, 230)

        #Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
