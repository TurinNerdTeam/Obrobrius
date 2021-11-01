import pygame

class Obry():
    def __init__(self, surface):
        super().__init__()
        self.color = pygame.Color(255,255,255); # White
        self.surface = surface
        self.radius = 5
        self.width = 5
        #slef.shape = None
        self.x=300
        self.y=300

    def move(self, x:int, y:int):
        self.x += x
        self.y += y
        pygame.draw.circle(self.surface, self.color, (self.x,self.y), self.radius, self.width)

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x,self.y), self.radius, self.width)



