# import pygame, sys, os, random, math
# from PIL import Image
# from pygame.locals import*
# pygame.init()

# pygame.display.set_caption("SPRITESHEET GENERATOR")
# FPS = pygame.time.Clock()

# SCALE = 2

# image_path = "sketch.png"
# sketch = Image.open(image_path)
# sketch_dimension = sketch.size

# SCREEN = pygame.display.set_mode(sketch_dimension, 0, 32)

# spritesheet = pygame.image.load(image_path).convert()
# spritesheet.set_colorkey((0,0,0))



# click_once = True
# selector_dimension = [0,0] 
# selector_point = [0,0]
# distance = 0
# while 1:
#     SCREEN.fill((0,0,0))
#     SCREEN.blit(spritesheet,(0,0))
    
#     # events
#     mouse = pygame.mouse.get_pos()
#     mouse_clicked = pygame.mouse.get_pressed()

    
#     selector = pygame.draw.rect(SCREEN, (0,255,0), (100,200,distance,distance), 1)

#     distance = math.hypot(mouse[0] - selector.bottomright[0], mouse[1] - selector.bottomright[1]))

    
#     for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#             if event.type == pygame.MOUSEBUTTONUP:
#                 click_once = True

#     FPS.tick(60)
#     pygame.display.update()


