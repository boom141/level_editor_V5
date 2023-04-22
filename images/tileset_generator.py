import pygame, sys, os, random, math
from PIL import Image
from pygame.locals import*
pygame.init()

pygame.display.set_caption("SPRITESHEET GENERATOR")
FPS = pygame.time.Clock()

SCALE = 2
BLACK = (0,0,0,255)

image_path = "d2.png"
SCREEN = pygame.display.set_mode((200,200), 0, 32)

session_image = pygame.image.load(image_path).convert()
SCREEN_DIMENSION = [session_image.get_width()*SCALE,session_image.get_height()*SCALE]
SCREEN = SCREEN = pygame.display.set_mode(SCREEN_DIMENSION, 0, 32)

image = session_image.copy()

click_once = True

initial_point = None
current_selection = None

selection_list = []
while 1:
    # mouse fucntions
    image.fill((0,0,0))
    image.blit(session_image,(0,0))
    mx, my = pygame.mouse.get_pos()
    mx = mx//SCALE
    my = my//SCALE

    mouse_clicked = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()

    #rectangular selector
    if mouse_clicked[2]:
         if click_once:
            click_once = False
            initial_point = [mx,my]
         if pygame.MOUSEMOTION:
            rect_scale = math.hypot(mx-initial_point[0], my-initial_point[1])
            current_selection = pygame.Rect(initial_point[0],initial_point[1],rect_scale,rect_scale)
            pygame.draw.rect(image, (255,0,0), current_selection, 1)

    if selection_list:
        for selection in selection_list:
            pygame.draw.rect(image, (255,0,0), selection, 1)

    if keys[K_z] and click_once:
        click_once = False
        selection_list = selection_list[:-1]

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                click_once = True
                selection_list.append(current_selection)

            if event.type == pygame.KEYUP:
                 click_once = True

    SCREEN.blit(pygame.transform.scale(image,SCREEN_DIMENSION),(0,0))
    FPS.tick(100)
    pygame.display.update()


