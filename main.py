"""Startup point
"""

import sys
import pygame
from settings import Settings

def run_game():
    """Initialize game, settings and create screen object."""
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption(game_settings.game_name)

    # The main loop of the game
    while True:
        # Watch the keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Fill the screen with given color
        screen.fill(game_settings.bg_color)

        # Update the screen surface
        pygame.display.flip()


if __name__ == "__main__":
    run_game()
