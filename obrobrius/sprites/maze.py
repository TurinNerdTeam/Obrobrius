# -*- coding: utf-8 -*-

import time
import random
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group as SpriteGroup
from pygame import Color
from pygame.surface import Surface
from pygame.draw import line as Line

# Strongly inspired to https://github.com/boppreh/maze/blob/master/maze.py

# Easy to read representation for each cardinal direction.
N, S, W, E = ('n', 's', 'w', 'e')

# size of the cell
CELL_WIDTH = 60
CELL_HEIGHT = 60

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
        #TODO re anble this check
        #assert abs(self.x - other.x) + abs(self.y - other.y) == 1, '{}, {}'.format(self, other)
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
        print(other._wall_to(self))
        if other._wall_to(self) in other.walls:
            other.walls.remove(other._wall_to(self))

        print(self._wall_to(other))
        if self._wall_to(other) in self.walls:
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

class Maze(SpriteGroup):
    """
    Maze class containing full board and maze generation algorithms.
    """

    def __init__(self, surface:Surface, width:int=20, height:int=10):
        """
        Creates a new maze with the given sizes, with all walls standing.
        """
        self.width = width
        self.height = height
        self.cells = []
        for y in range(int(self.height/CELL_HEIGHT)):
            for x in range(int(self.width/CELL_WIDTH)):
                x_c = int(CELL_WIDTH/2 + x * CELL_WIDTH)
                y_c = int(CELL_HEIGHT/2 + y * CELL_HEIGHT)
                self.cells.append(Cell(surface, x_c, y_c))

    def __getitem__(self, index):
        """
        Returns the cell at index = (x, y).
        """
        x_c, y_c = index
        if 0 <= x_c < self.width and 0 <= y_c < self.height:
            #return self.cells[x + y * self.width]
            x = int ((2*x_c - CELL_WIDTH) / (2*CELL_WIDTH))
            y = int ((2*y_c - CELL_HEIGHT) / (2*CELL_HEIGHT))
            l = int(self.width/CELL_WIDTH)
            return self.cells[x + y * l]
        else:
            return None

    def neighbors(self, cell):
        """
        Returns the list of neighboring cells, not counting diagonals. Cells on
        borders or corners may have less than 4 neighbors.
        """
        x = cell.x
        y = cell.y

        for new_x, new_y in [(x, y - int(CELL_HEIGHT/2)), (x, y + int(CELL_HEIGHT/2)), (x - int(CELL_WIDTH/2), y), (x + int(CELL_WIDTH/2), y)]:
            neighbor = self[new_x, new_y]
            if neighbor is not None:
                yield neighbor

    def _to_str_matrix(self):
        """
        Returns a matrix with a pretty printed visual representation of this
        maze. Example 5x5:
        OOOOOOOOOOO
        O       O O
        OOO OOO O O
        O O   O   O
        O OOO OOO O
        O   O O   O
        OOO O O OOO
        O   O O O O
        O OOO O O O
        O     O   O
        OOOOOOOOOOO
        """
        str_matrix = [['O'] * (self.width * 2 + 1)
                      for i in range(self.height * 2 + 1)]

        for cell in self.cells:
            x = cell.x * 2 + 1
            y = cell.y * 2 + 1
            str_matrix[y][x] = ' '
            if N not in cell and y > 0:
                str_matrix[y - 1][x + 0] = ' '
            if S not in cell and y + 1 < self.width:
                str_matrix[y + 1][x + 0] = ' '
            if W not in cell and x > 0:
                str_matrix[y][x - 1] = ' '
            if E not in cell and x + 1 < self.width:
                str_matrix[y][x + 1] = ' '

        return str_matrix

    def randomize(self):
        """
        Knocks down random walls to build a random perfect maze.
        Algorithm from http://mazeworks.com/mazegen/mazetut/index.htm
        """
        cell_stack = []
        cell = random.choice(self.cells)
        n_visited_cells = 1
        print(len(self.cells))

        #while n_visited_cells < len(self.cells):
        while n_visited_cells < 20:
            print("\n====\npassing from: ")
            print(cell)

            print(n_visited_cells)
            print(len(self.cells))

            neighbors = [c for c in self.neighbors(cell) if c.is_full()]
            print("\t full  neighbors ")
            print(neighbors)

            if len(neighbors):
                neighbor = random.choice(neighbors)
                print("\t selected neighbors")
                print(neighbor)

                cell.connect(neighbor)
                print("\t cell connected")
                print(cell)
                print(neighbor)

                cell_stack.append(cell)
                print("\t updated cell_stack")
                print(cell_stack)

                cell = neighbor
                n_visited_cells += 1

            else:
                cell = cell_stack.pop()


    def draw(self):
        for cell in self.cells :
            cell.draw()

    @staticmethod
    def generate(surface:Surface, width:int=20, height:int=10):
        """
        Returns a new random perfect maze with the given sizes.
        """
        m = Maze(surface, width, height)
        m.randomize()
        return m
