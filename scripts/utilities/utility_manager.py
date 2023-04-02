import pygame
from scripts import loaded_images, draw_text

class utility:
    def __init__(self):
        self.current_folder = "None Selected"
        self.current_index = -1
        self.folders_button = []
        self.tiles_button = []
        self.utilities_button = []

    def render_folders(self,surface):
        self.folders_button = []
        for i, folder in enumerate(loaded_images.image_database):
           if folder != self.current_folder:
               color = (255,255,255)
           else: 
               color = (0,255,0)

           button = draw_text(surface,(5,i*17),"Minecraft.ttf",15,color,text=folder)
           self.folders_button.append([button,folder])

    def render_tileset(self,surface):
        self.tiles_button = []
        if self.current_folder != "None Selected":
            for i, tile in enumerate(loaded_images.image_database[self.current_folder]):
                if i != self.current_index:
                    color = (45,45,45)
                else: 
                    color = (0,255,0)

                button = surface.blit(pygame.transform.scale(tile,(30,30)),(5, 170 + int(i*35)))
                pygame.draw.rect(surface, color, button, 1)
                self.tiles_button.append([button,i])
