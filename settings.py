class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 3.5
        self.ship_limit = 5

        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 0, 0)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 5
        self.fleet_direction = 1