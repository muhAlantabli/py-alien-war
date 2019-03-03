"""Game settings module
"""


class Settings:
    """Class to store all settings of the game."""

    def __init__(self):
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.game_name = "Alien War"