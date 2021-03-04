class Settings:
    '''to store all the setting for alien_invasion.py'''

    def __init__(self):
        """Initialize the game settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,200,100)

        # Ship settings
        self.ship_limit = 3
        self.ship_width = 70
        self.ship_height = 70

        # bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 4

        # alien settings
        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 3.0

        self.fleet_dir = 1 # 1 is right -1 is left

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points*self.score_scale)

