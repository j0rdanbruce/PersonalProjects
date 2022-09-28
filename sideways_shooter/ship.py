import pygame

class Ship:
    """game resources for each instance of ship"""
    def __init__(self, ss_game):
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        #load ship image and get its rect
        self.image = pygame.image.load('images/cool_ship.png')
        self.rect = self.image.get_rect()

        #ships starting position in game
        self.rect.midleft = self.screen_rect.midleft
        
        #storing ship speed as float
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False
    
    def blitme(self):
        """draws image of ship to its starting position"""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """moves the ships position"""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        
        #update ships position
        self.rect.y = self.y
    
    def recenter_ship(self):
        self.rect.midleft = self.screen_rect.midleft
        




