"""Ship module
"""
import pygame

class Ship:
    def __init__(self, screen):
        """Initilize the ship and set its starting position."""
        self.screen = screen

        # Load the ship image and its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        # Start each ship at the bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def draw(self):
        """Draw ship at its current location."""
        self.screen.blit(self.image, self.rect)
