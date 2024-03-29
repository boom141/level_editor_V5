import pygame, sys, os, random, time, json
from pygame.locals import*
pygame.init()

DIMENSIONS = (800,500)
SCREEN = pygame.display.set_mode(DIMENSIONS, 0, 32)
pygame.display.set_caption("LEVEL EDITOR V5")

UTIL_DIMENSIONS = (200,500)
UTILITIES = pygame.Surface(UTIL_DIMENSIONS)

CANVAS_DIMENSIONS = (3000,3000)
CANVAS = pygame.Surface(CANVAS_DIMENSIONS)

FPS = pygame.time.Clock()

def draw_text(surface,position=(0,0),font=None,font_size=15,font_color=(255,255,255),text='hello world!'):
    font = pygame.font.Font("./fonts/"+font,font_size)
    message = font.render(text,False,font_color)
    return surface.blit(message,position)

from scripts.utilities.tileset_loader import tileset_init
loaded_images = tileset_init('./images/tileset',scale=26)
loaded_images.load()


from scripts.canvas.canvas_manager import init_canvas
canvas = init_canvas(canvas_dimension=CANVAS_DIMENSIONS,pixel_size=26)

from scripts.utilities.utility_manager import utility
utils = utility()

