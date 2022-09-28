from sys import setdlopenflags


class GameStats:
    """initializes class for game statistics"""
    def __init__(self, ss_game):
        """initializes stats for the shooter game"""
        self.settings = ss_game.settings
        self.game_active = True
        self.reset_stats()
    
    def reset_stats(self):
        """initializes potentntail game stats that could be reset"""
        self.ships_left = self.settings.ship_limit
        self.hit_counter = 0
        self.score_count = 0









