# 
#

import pygame
from pygame import Color, Surface
from pygame.sprite import Sprite

class Obry(Sprite):
    def __init__(self, surface:Surface, x:int=0, y:int=0, radius:int=5, width:int=2):
        Sprite.__init__(self)

        self.surface = surface
        self.radius = radius
        self.width = width
        self.x=x
        self.y=y
        self.draw()
        
    def set_position(self, x:int, y:int):
        self.x = x
        self.y = y

    def move(self, x:int, y:int):
        self.draw(Color(0,0,0))
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
        
        self.draw()

    def draw(self, color:Color = Color(255,255,255)):
        self.rect = pygame.draw.circle(self.surface, color, (self.x,self.y), self.radius, self.width)

