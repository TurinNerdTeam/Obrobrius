import pygame
from pygame import *
from pygame import Surface

from time import sleep

def show_splash_screen(screen: Surface):
    
    game_logo = pygame.image.load('.\game_assets\splash_screen\Logo.png')
    game_logo = pygame.transform.scale(game_logo, (640, 480))
    
    x,y = pygame.display.get_surface().get_size()
    rect = game_logo.get_rect()
    rect.center = (x / 2. , y / 2.)

    alphaSurface = Surface((1024,768)) # The custom-surface of the size of the screen.
    alphaSurface.fill((255,255,255)) # Fill it with whole white before the main-loop.
    alphaSurface.set_alpha(0) # Set alpha to 0 before the main-loop. 
    alph = 0 # The increment-variable.
    
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                return

        alph += 0.1 # Increment alpha by a really small value (To make it slower, try 0.01)
        game_logo.set_alpha(alph) # Set the incremented alpha-value to the custom surface.
        screen.blit(game_logo, rect)
        sleep(0.1)
        
        
        #screen.blit()

        #screen.fill((0,0,0)) # At each main-loop fill the whole screen with black.
        #alph += 0.1 # Increment alpha by a really small value (To make it slower, try 0.01)
        #alphaSurface.set_alpha(alph) # Set the incremented alpha-value to the custom surface.
        #screen.blit(alphaSurface,(0,0)) # Blit it to the screen-surface (Make them separate)

        display.flip() # Flip the whole screen at each frame.
    



    # gamedisplay.fill(WHITE)
    # largeText = pygame.font.Font('Arial',155)
    # textSurf, textRect = text_objects("test", largeText)
    # textRect.centre = ((display_width/2), (display_height/2))
    # gamedisplay.blit(textSurf, textRect)
    # pygame.display.update()
    # clock.tick(15)






