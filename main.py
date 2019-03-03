"""Startup point
"""

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """Initialize game, settings and create screen object."""
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption(game_settings.game_name)

    # Make the ship
    ship = Ship(screen)

    # The main loop of the game
    while True:
        gf.check_events()
        gf.update_screen(game_settings, screen, ship)


if __name__ == "__main__":
    run_game()
