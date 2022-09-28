import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """manages the bullets that the ship fires"""
    def __init__(self, ss_game):
        """creates bullet object and manages bullet position"""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
            self.settings.bullet_height)
        self.rect.midright = ss_game.ship.rect.midright
        
        #bullets position as a decimal through float
        self.x = float(self.rect.x)
    
    def draw_bullet(self):
        """draws bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        """updates the bullet position"""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x











