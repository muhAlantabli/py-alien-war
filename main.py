"""Startup point
"""

import sys
import pygame


def run_game():
    """Initialize game and create screen object."""
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien War")

    # Set the background color (light grey)
    bg_color = (230, 230, 230)

    # The main loop of the game
    while True:
        # Watch the keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Fill the screen with given color
        screen.fill(bg_color)

        # Update the screen surface
        pygame.display.flip()


if __name__ == "__main__":
    run_game()
