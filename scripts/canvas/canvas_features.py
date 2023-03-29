import pygame
from pygame.locals import*
from scripts import init_canvas

class features:
    def __init__(self):
        self.displacement = [0,0]
        self.pixel_displacement_value = 5

    def canvas_displacement(self,keys,delta_time=False):
        move_pixels = [0,0]
        if keys["LEFT"]:
            move_pixels[0] -= self.pixel_displacement_value
        if keys["RIGHT"]:
            move_pixels[0] += self.pixel_displacement_value
        if keys["UP"]:
            move_pixels[1] -= self.pixel_displacement_value
        if keys["DOWN"]:
            move_pixels[1] += self.pixel_displacement_value     
        
        self.displacement[0] -= move_pixels[0] 
        self.displacement[1] -= move_pixels[1] 
    
    def place_tile(self,tile_attributes):
        if tile_attributes not in init_canvas.tiles:
            init_canvas.tiles.append(tile_attributes)
    
    def remove_tile(self,tile_attributes):
        pass
