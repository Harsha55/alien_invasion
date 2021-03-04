import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent the aliens"""

    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        #Load the image for alien and set its rect
        self.image = pygame.image.load("images/alien2.bmp")
        self.image = pygame.transform.scale(self.image,(70,70))
        self.rect = self.image.get_rect()

        #Start each new alien at the top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the aliens exact horizontal position
        self.x = float(self.rect.x)
    
    def check_edges(self):
        if self.rect.right >= self.screen_rect.right or self.rect.left <=0:
            return True
    
    def update(self):
        """Move aliens to right"""
       # move left or right
        self.x += (self.settings.alien_speed*
                        self.settings.fleet_dir)
        self.rect.x = self.x

        

        