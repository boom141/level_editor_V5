import pygame, sys, os, random, math
from PIL import Image
from pygame.locals import*
pygame.init()

pygame.display.set_caption("SPRITESHEET GENERATOR")
FPS = pygame.time.Clock()

SCALE = 2

image_path = "tileset/grass-tileset/0.png"
SCREEN = pygame.display.set_mode((200,200), 0, 32)

sample_image = pygame.image.load(image_path).convert()
sample_image.set_colorkey((0,0,0))

click_once = True
image_rects = [pygame.Rect(80,30,sample_image.get_width(),sample_image.get_height()),pygame.Rect(80,60,sample_image.get_width(),sample_image.get_height())]
while 1:    
    # mouse fucntions
    mouse = pygame.mouse.get_pos()
    mouse_clicked = pygame.mouse.get_pressed()
  
    for rect in image_rects:
         if mouse_clicked[0] and rect.collidepoint(mouse) and click_once:
              click_once = False
              SCREEN.fill((0,0,0))
              image_rects.remove(rects)
    
    for rects in image_rects:
        SCREEN.blit(sample_image, rects)
    

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                click_once = True

    FPS.tick(60)
    pygame.display.update()


