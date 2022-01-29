#
# obrobrius game
#

from sqlite3 import Time
from pygame.color import Color
from pygame.time import Clock
from pygame import quit, display, key, event as game_events, init
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)
from sprites.obry import Obry
from sprites.maze import Maze
from splash_screen import show_start_splash_screen, show_end_level_message
from random import randint

class Obrobrius:

    def __init__(self, fps:int=15, screen_width:int=600, screen_height:int=600, cell_edge:int=30, offset:int=15, n_cell:int=19 ) -> None:
        self.running = False
        self.fps = fps
        self.frames_per_second_monitor = Clock()

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_edge = 30
        self.offset = 15
        self.n_cell = 19

        self.displaysurf = display.set_mode((self.screen_width,self.screen_height))

        # set background color
        self.displaysurf.fill(Color(0,0,0))

    def events_handler(self):
        for event in game_events.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
            if event.type == QUIT:
                self.running = False

    def keyboard_handler(self):
        pressed_keys = key.get_pressed()

        x_offset = 0
        y_offset = 0
        need2move = False

        if pressed_keys[K_UP]:
            y_offset = - self.offset
            need2move = True

        if pressed_keys[K_DOWN]:
            y_offset = self.offset
            need2move = True

        if pressed_keys[K_LEFT]:
            x_offset = - self.offset
            need2move = True

        if pressed_keys[K_RIGHT]:
            x_offset = self.offset
            need2move = True

        if need2move :
            self.obry.move(x_offset,y_offset)

            if self.maze.is_collided(self.obry):
                x_offset*=-1
                y_offset*=-1
                self.obry.move(x_offset,y_offset)

    def setup_game(self)->None:

        self.target_cell = None

        self.maze = Maze.generate(
            surface=self.displaysurf,
            width=self.n_cell,
            height=self.n_cell,
            cell_edge=self.cell_edge,
            offset=self.offset
            )

        self.maze.draw()
    
        self.start_cell = self.maze[(0, randint(0,self.n_cell-1))]
    
        self.target_cell = self.maze[(self.n_cell-1, randint(0,self.n_cell-1))]

        self.target_cell.set_color(Color(0,100,100))

        self.obry = Obry(self.displaysurf, self.cell_edge, self.cell_edge)
        self.obry.set_position(self.start_cell.x_surf, self.start_cell.y_surf)
        self.obry.draw()

    def game_loop(self):
        # main loop game
        while self.running:
            # mange input events
            self.events_handler()
            self.keyboard_handler()

            self.maze.draw()

            # update the main window content
            display.update()

            # tick
            self.frames_per_second_monitor.tick(self.fps)

            if self.check_finish():
                self.setup_game()


    def check_finish(self):

        if self.obry.x == self.target_cell.x_surf and self.obry.y == self.target_cell.y_surf:
            show_end_level_message(self.displaysurf)
            return True
        return False
            
    def play(self) -> None :
        self.running = True
        # show the initial spalsh screen
        if show_start_splash_screen(self.displaysurf) == False:
            self.running = False
        
        if self.running:
            # prepare the game
            self.setup_game()

            # run the game
            self.game_loop()

        # close pygame
        quit()

if __name__ == "__main__":
    # init paygame
    init()

    # create the game instance
    game = Obrobrius()

    # play the game
    game.play()

