import pygame

class canvas:
    def __init__(self,canvas_dimension=(0,0),pixel_size=32):
        self.tiles = []
        self.canvas_dimension = canvas_dimension
        self.pixel_size = pixel_size

    def create_grid(self,surface):
        for y in range(0,self.canvas_dimension[1],self.pixel_size):
            for x in range(0,self.canvas_dimension[0],self.pixel_size):
                pygame.draw.rect(surface, (15,15,15), (x,y,self.pixel_size,self.pixel_size),1)

    def render_tiles(self,surface):
        pass