# -*- coding: utf-8 -*-

import random
import pygame
from pygame.sprite import Sprite
from pygame import Color
from pygame.surface import Surface
from pygame.draw import line as Line

# Strongly inspired to https://github.com/boppreh/maze/blob/master/maze.py

# Easy to read representation for each cardinal direction.
N, S, W, E = ('n', 's', 'w', 'e')

# size of the cell
CELL_WIDTH = 6
CELL_HEIGHT = 6

# default colors
CELL_BORDER_COLOR = Color(188,188,188) # Gray
CELL_BG_COLOR = Color(0,0,0) # Black

# lines width
CELL_LINE_WIDTH = 1

class Cell(Sprite):
    """
    Class for each individual cell. Knows only its position and which walls are
    still standing.

    the cell wall are drawn at :
        * CELL_HEIGHT/2 at N and S
        * CELL_WIDTH at W and E
    """

    def __init__(self, surface:Surface, x:int, y:int,
            walls:list=[N, S, E, W],
            line_width:int=CELL_LINE_WIDTH,
            border_color:Color=CELL_BORDER_COLOR,
            bg_color:Color=CELL_BG_COLOR
            ):
        self.x = x
        self.y = y
        self.line_width = line_width
        self.rects = []
        self.surface = surface
        self.border_color =  border_color
        self.bg_color =  bg_color
        self.walls = set(walls)

    def __repr__(self):
        # <15, 25 (es  )>
        return '<{}, {} ({:4})>'.format(self.x, self.y, ''.join(sorted(self.walls)))

    def __contains__(self, item):
        # N in cell
        return item in self.walls

    def is_full(self):
        """
        Returns True if all walls are still standing.
        """
        return len(self.walls) == 4

    def _wall_to(self, other):
        """
        Returns the direction to the given cell from the current one.
        Must be one cell away only.
        """
        assert abs(self.x - other.x) + abs(self.y - other.y) == 1, '{}, {}'.format(self, other)
        if other.y < self.y:
            return N
        elif other.y > self.y:
            return S
        elif other.x < self.x:
            return W
        elif other.x > self.x:
            return E
        else:
            assert False

    def connect(self, other):
        """
        Removes the wall between two adjacent cells.
        """
        other.walls.remove(other._wall_to(self))
        self.walls.remove(self._wall_to(other))

    def draw(self):
        """
        references :
        https://www.pygame.org/docs/ref/draw.html#pygame.draw.lines
        the cell have following points:
            * NE up, right
            * NW up, left
            * SE down, rigth
            * SW down, left

        we figure the walls in this way:
            * N wall starts from NW to NE
            * E wall starts from NE to SE
            * S wall starts from SE to WE
            * W wall starts from SE to NE

        position (x,y) of the points are calculated using the center of the cell
            * NE = (self.x + (CELL_WIDTH/2), self.y + (CELL_HEIGHT/2))
            * NW = (self.x - (CELL_WIDTH/2), self.y + (CELL_HEIGHT/2))
            * SE = (self.x + (CELL_WIDTH/2), self.y - (CELL_HEIGHT/2))
            * SW = (self.x - (CELL_WIDTH/2), self.y - (CELL_HEIGHT/2))
        """

        ne = (self.x + (CELL_WIDTH/2), self.y + (CELL_HEIGHT/2))
        nw = (self.x - (CELL_WIDTH/2), self.y + (CELL_HEIGHT/2))
        se = (self.x + (CELL_WIDTH/2), self.y - (CELL_HEIGHT/2))
        sw = (self.x - (CELL_WIDTH/2), self.y - (CELL_HEIGHT/2))

        if self.__contains__(N):
            line = Line(self.surface,self.border_color, nw, ne, self.line_width)
            self.rects.append(line)

        if self.__contains__(E):
            line = Line(self.surface,self.border_color, ne, se, self.line_width)
            self.rects.append(line)

        if self.__contains__(S):
            line = Line(self.surface,self.border_color, se, sw, self.line_width)
            self.rects.append(line)

        if self.__contains__(W):
            line = Line(self.surface,self.border_color, sw, nw, self.line_width)
            self.rects.append(line)

