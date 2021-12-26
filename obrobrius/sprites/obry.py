# 
#

import pygame
from pygame import Color
from pygame.sprite import Sprite

class Obry(Sprite):
    def __init__(self, surface):
        Sprite.__init__(self)

        self.color = Color(255,255,255); # White
        self.surface = surface
        self.radius = 4
        self.width = 2
        #slef.shape = None
        self.x=300
        self.y=300
        self.draw()
        
    def set_position(self, x:int, y:int):
        self.x = x
        self.y = y

    def move(self, x:int, y:int):
        self.x += x
        self.y += y

        if self.x < 0:
            self.x = self.radius
        if self.x > self.surface.get_width():
            self.x = self.surface.get_width() - self.radius
        if self.y < 0:
            self.y = self.radius
        if self.y > self.surface.get_height():
            self.y = self.surface.get_height() - self.radius

    def draw(self):
        self.rect = pygame.draw.circle(self.surface, self.color, (self.x,self.y), self.radius, self.width)

