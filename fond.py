import pygame

class space():
    def __init__(self, screen):
        """Initialize the ship and set its startign position."""
        self.screen = screen

        # Load the fond image and get it's rect.
        self.image = pygame.image.load("./images/Space.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def blitme(self):
        """Draw the fond."""
        self.screen.blit(self.image, self.rect)