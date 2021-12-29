import pygame
from pygame import *

from enum import Enum
from os import path

current_dir = "."
asset_dir = "game_assets"
splash_dir = "splash_screen"
game_logo_file = "Logo.png"
team_logo_file = "Team_Logo.jpg"

class ImageState(Enum):
    FADE_IN = 0
    SHOW_LOGO = 1
    FADE_OUT = 2

def show_splash_screen(screen: Surface) -> bool:

    game_logo = pygame.image.load(path.join(current_dir,asset_dir,splash_dir,game_logo_file))
    game_logo = pygame.transform.scale(game_logo, (640, 480))

    team_logo = pygame.image.load(path.join(current_dir,asset_dir,splash_dir,team_logo_file))
    team_logo = pygame.transform.scale(team_logo, (640, 480))

    x,y = pygame.display.get_surface().get_size()
    game_logo_rect = game_logo.get_rect()
    game_logo_rect.center = (int(x / 2) , int(y / 2))

    team_logo_rect = team_logo.get_rect()
    team_logo_rect.center = (int(x / 2) , int(y / 2))

    alpha = 0 # The increment-variable.

    static_image_counter = 0
    image_state = ImageState.FADE_IN
    image_num = 1 # Count backward

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                return True
            if event.type == QUIT:
                return False

        screen.fill((0,0,0)) # Reset the image

        if image_state == ImageState.FADE_IN:
            alpha = alpha + 4.25  # 60 fps -> 1s -> 255 / 60 = 4.25 
            if alpha >= 255: image_state = ImageState.SHOW_LOGO

        elif image_state == ImageState.SHOW_LOGO:
            alpha = 255
            static_image_counter += 1
            if static_image_counter >= 120: # 60 fps -> 2s -> 60 * 2 = 120 
                static_image_counter = 0
                image_state = ImageState.FADE_OUT

        elif image_state == ImageState.FADE_OUT:
            alpha = alpha - 4.25 # 60 fps -> 1s -> 255 / 60 = 4.25 
            if alpha < 0:
                alpha = 0
                image_num -= 1
                if (image_num < 0): return True
                image_state = ImageState.FADE_IN


        if image_num == 1:
            game_logo.set_alpha(alpha)
            screen.blit(game_logo, game_logo_rect)
        if image_num == 0:
            team_logo.set_alpha(alpha)
            screen.blit(team_logo, team_logo_rect)

        pygame.time.Clock().tick(60) #60 fps
        display.flip()



