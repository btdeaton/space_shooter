class Settings:
    """A class to store all settings for Space Shooter"""

    def __init__(self):
        """Initialize the settings for Space Shooter"""

        #Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        #Screen settings for width, height, and color
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230, 230, 230)

        #Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction where 1 represents right, -1 represents left
        self.fleet_direction = 1