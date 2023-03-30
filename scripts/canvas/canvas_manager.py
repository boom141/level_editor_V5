import pygame

from scripts import loaded_images

class init_canvas:
    def __init__(self,canvas_dimension=(0,0),pixel_size=32,layers=10):
        self.tiles = {}
        self.canvas_dimension = canvas_dimension
        self.pixel_size = pixel_size
        self.layers = layers

        self.displacement = [0,0]
        self.pixel_displacement_value = 5
        self.surface_layers = []
        self.current_layer = 0

    def create_grid(self,surface):
        for y in range(0,self.canvas_dimension[1],self.pixel_size):
            for x in range(0,self.canvas_dimension[0],self.pixel_size):
                pygame.draw.rect(surface, (85,85,85), (x,y,self.pixel_size,self.pixel_size),1)
        

    def create_layers(self):
        self.surface_layers = [pygame.Surface(self.canvas_dimension) for _ in range(self.layers)]

        for i, layer in enumerate(self.surface_layers):
            layer.set_colorkey((0,0,0))
            self.create_grid(layer)
            self.tiles[f"LAYERS: {i}"] = []


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
        for layer in self.tiles:
            if tile_attributes not in self.tiles[layer]:
                self.tiles[layer].append(tile_attributes)
    
    def remove_tile(self,tile_attributes):
        pass
    
    def canvas_layering(self):
        if self.current_layer != 0:
            for i, layer in enumerate(self.surface_layers):
                if self.current_layer == i:
                    layer.set_alpha(225)
                else:
                    layer.set_alpha(50)
        else:
            for layer in self.surface_layers:
                layer.set_alpha(255)


    def render_tiles(self):
        for layer in self.tiles:
            for tile in self.tiles[layer]:
                self.surface_layers[tile[4]].blit(loaded_images.image_database[tile[2]][tile[3]],
                                                  (tile[0]*self.pixel_size,tile[1]*self.pixel_size))