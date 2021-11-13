# 
#

import pygame
from pygame import Color
from pygame.sprite import Sprite

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)

class Obry(Sprite):
    def __init__(self, surface):
        super().__init__()
        self.color = Color(255,255,255); # White
        self.surface = surface
        self.radius = 5
        self.width = 5
        #slef.shape = None
        self.x=300
        self.y=300

    def move(self, x:int, y:int):
        self.x += x
        self.y += y

        if self.x < 0:
            self.x = 0
        if self.x > self.surface.get_width():
            self.x = self.surface.get_width()
        if self.y <0:
            self.y = 0
        if self.y > self.surface.get_height():
            self.y = self.surface.get_height()

        pygame.draw.circle(self.surface, self.color, (self.x,self.y), self.radius, self.width)

    def update_position(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.move(0,-5)
        if pressed_keys[K_DOWN]:
            self.move(0,5)
        if pressed_keys[K_LEFT]:
            self.move(-5,0)
        if pressed_keys[K_RIGHT]:
            self.move(5,0)

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x,self.y), self.radius, self.width)

