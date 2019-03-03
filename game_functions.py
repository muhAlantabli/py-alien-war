"""Game function module
"""

import sys
import pygame


def check_events():
    """Watch the keyboard and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(game_settings, screen, ship):
    """Update screen surface."""
    # Fill the screen with given color & draw ship
    screen.fill(game_settings.bg_color)
    ship.draw()

    # Update the screen surface
    pygame.display.flip()
