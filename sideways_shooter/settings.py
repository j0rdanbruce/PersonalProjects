class Settings:
    """the settings for the game"""
    def __init__(self):
        """the game setting attributes for each instance of game"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 70
        self.fleet_direction = 1

        



