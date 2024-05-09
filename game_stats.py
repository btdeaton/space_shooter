from pathlib import Path
import json

class GameStats:
    """Track statistics for Space Shooter"""

    def __init__(self, space_game):
        """Initialize statistics"""
        self.settings = space_game.settings
        self.reset_stats()

        #High score should never be reset
        path = Path('high_score.json')
        if path.exists():
            contents = path.read_text()
            high_score = json.loads(contents)
            self.high_score = high_score
        else:
            self.high_score = 0
    
    def reset_stats(self):
        """Initialize statistics that change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1