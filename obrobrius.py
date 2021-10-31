#
# obrobrius game
#

import pygame
from pygame import QUIT

# define global values
continue_to_play = True
FPS = 60
FramePerSec = pygame.time.Clock()

X = 600
Y = 600

DISPLAYSURF = pygame.display.set_mode((X,Y))

def events_handler():
    for event in pygame.event.get():
        if event.type == QUIT:
            global continue_to_play
            continue_to_play = False

def main_loop():
	global continue_to_play
	# main loop game
	while continue_to_play:
        # mange input events
		events_handler()
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
