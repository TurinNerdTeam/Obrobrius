#
# obrobrius game
#

import pygame
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


# define global values
running = True
FPS = 60
frames_per_second_monitor = pygame.time.Clock()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CELL_EDGE = 30
OFFSET = 15
N_CELL = 19

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

obry = Obry(DISPLAYSURF)
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
    
    old_x = obry.x
    old_y = obry.y

    moved = False
    if pressed_keys[K_UP]:
        print("------------")
        print("premove : ( {}, {} )".format(obry.x, obry.y))
        moved = True
        obry.move(0,-5)
    if pressed_keys[K_DOWN]:
        print("------------")
        print("premove : ( {}, {} )".format(obry.x, obry.y))
        moved = True
        obry.move(0,5)
    if pressed_keys[K_LEFT]:
        print("------------")
        print("premove : ( {}, {} )".format(obry.x, obry.y))
        moved = True
        obry.move(-5,0)
    if pressed_keys[K_RIGHT]:
        print("------------")
        print("premove : ( {}, {} )".format(obry.x, obry.y))
        moved = True
        obry.move(5,0)
    

    if moved :
        print("postmove : ( {}, {} )".format(obry.x, obry.y))

    if moved and maze.is_collided(obry):
        x_off = obry.x - old_x
        y_off = obry.y - old_y

        obry.set_position(old_x,old_y)
        print("collision : ( {}, {} )".format(obry.x, obry.y))

        print("------------")

def main_loop():
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
