#
# obrobrius game
#

import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from sprites.obry import Obry
from sprites.maze import Maze

from splash_screen import show_splash_screen


# define global values
running = True
FPS = 60
frames_per_second_monitor = pygame.time.Clock()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

obry = Obry(DISPLAYSURF)
maze = Maze.generate(DISPLAYSURF,SCREEN_WIDTH,SCREEN_HEIGHT)

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
    obry.update_position(pressed_keys)

def main_loop():

    show_splash_screen(DISPLAYSURF)

    global running
    # main loop game
    while running:
        # mange input events
        events_handler()
        keyboard_handler()

        DISPLAYSURF.fill(pygame.Color(0,0,0))

        obry.draw()
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
    # run main loop
    main_loop()
