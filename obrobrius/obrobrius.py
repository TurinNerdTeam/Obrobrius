#
# obrobrius game
#

import pygame
from pygame.color import Color
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

from splash_screen import show_splash_screen


# define global values
running = True
FPS = 15
frames_per_second_monitor = pygame.time.Clock()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CELL_EDGE = 30
OFFSET = 15
N_CELL = 19

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

obry = Obry(DISPLAYSURF, 30, 30)
maze = Maze.generate(
    surface=DISPLAYSURF,
    width=N_CELL,
    height=N_CELL,
    cell_edge=CELL_EDGE,
    offset=OFFSET
    )

def events_handler():
    for event in pygame.event.get():
        global running
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        if event.type == QUIT:
            running = False

def keyboard_handler():
    pressed_keys = pygame.key.get_pressed()
    
    x_offset = 0
    y_offset = 0
    need2move = False

    if pressed_keys[K_UP]:
        y_offset = - OFFSET
        need2move = True

    if pressed_keys[K_DOWN]:
        y_offset = OFFSET
        need2move = True

    if pressed_keys[K_LEFT]:
        x_offset = - OFFSET
        need2move = True

    if pressed_keys[K_RIGHT]:
        x_offset = OFFSET
        need2move = True

    if need2move :
        print("\npre move position: ( {} , {} ) - offsets to apply : ( {} , {} )".format(obry.x,obry.y, x_offset, y_offset))
        obry.move(x_offset,y_offset)

        print("post move : ( {} , {} )- offsets applyed : ( {} , {} )".format(obry.x,obry.y, x_offset, y_offset))
        if maze.is_collided(obry):
            x_offset*=-1
            y_offset*=-1
            print("post collision  : ( {} , {} ) - offsets to apply : ( {} , {} )".format(obry.x,obry.y, x_offset, y_offset))
            obry.move(x_offset,y_offset)
        

def main_loop():
    global running

    if show_splash_screen(DISPLAYSURF) == False:
        running = False

    # main loop game
    while running:
        # mange input events
        events_handler()
        keyboard_handler()

        maze.draw()

        # update the main window content
        pygame.display.update()
        # tick
        frames_per_second_monitor.tick(FPS)

    # close pygame
    pygame.quit()

if __name__ == "__main__":
    # init paygame
    pygame.init()

    # set background color
    DISPLAYSURF.fill(pygame.Color(0,0,0))

    # draw the maze
    maze.draw()

    # run main loop
    main_loop()
