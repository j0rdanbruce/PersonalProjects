import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """class that represents single alien"""
    def __init__(self, ss_game):
        """defines attributes of a single ship"""
        super().__init__()
        self.settings = ss_game.settings
        self.screen = ss_game.screen

        self.image = pygame.image.load('images/green_alien.png')
        self.rect = self.image.get_rect()

        #starting position of alien ship
        self.rect.x = self.settings.screen_width - self.rect.width
        self.rect.y = self.rect.height

        #store aliens x and y position as float
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """updates the position of alien fleet"""
        self.y += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.y = self.y

    def check_edges(self):
        """returns true if alien has hit the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True

        








