#
# obrobrius game
#

import pygame
from pygame import QUIT
from obry.obry  import Obry

# define global values
continue_to_play = True
FPS = 60
FramePerSec = pygame.time.Clock()

X = 600
Y = 600

DISPLAYSURF = pygame.display.set_mode((X,Y))

obry = Obry(DISPLAYSURF)

def events_handler():
    for event in pygame.event.get():
        if event.type == QUIT:
            global continue_to_play
            continue_to_play = False

def keyboard_handler():
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_UP]: # move obry up
        obry.move(0,-5)
    if pressed_keys[pygame.K_DOWN]: # move obry down
        obry.move(0,5)
    if pressed_keys[pygame.K_LEFT]: # move obry left
        obry.move(-5,0)
    if pressed_keys[pygame.K_RIGHT]: # move obry right
        obry.move(5,0)
    if pressed_keys[pygame.K_q]: # move obry right
        global continue_to_play
        continue_to_play = False

def main_loop():
    global continue_to_play
    # main loop game
    while continue_to_play:
        # mange input events
        events_handler()
        keyboard_handler()

        DISPLAYSURF.fill(pygame.Color(0,0,0))

        obry.draw()

        # update the main window content
        pygame.display.update()
        # tick
        FramePerSec.tick(FPS)

    # close pygame
    pygame.quit()

if __name__ == "__main__":
    # init paygame
    pygame.init()

    # run main loop
    main_loop()
