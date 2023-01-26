import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its startign position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get it's rect.
        self.image = pygame.image.load("./images/Ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start eat new hsip at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 20

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position besed on the Movement flag."""
        # Update the ship's center value, not the rect.
        if (self.moving_right == True) and (self.rect.right <= 1200):
            self.center += self.ai_settings.ship_speed_factor

        if (self.moving_left == True) and (self.rect.left >= 0):
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at this current loacation."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx