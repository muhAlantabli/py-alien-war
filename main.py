"""Startup point
"""

import sys
import pygame
from settings import Settings
from ship import Ship


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
        # Watch the keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Fill the screen with given color & draw ship
        screen.fill(game_settings.bg_color)
        ship.draw()
        
        # Update the screen surface
        pygame.display.flip()


if __name__ == "__main__":
    run_game()
