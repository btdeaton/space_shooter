class GameStats:
    """Track statistics for Space Shooter"""

    def __init__(self, space_game):
        """Initialize statistics"""
        self.settings = space_game.settings
        self.reset_stats()
    
    def reset_stats(self):
        """Initialize statistics that change during the game"""
        self.ships_left = self.settings.ship_limit