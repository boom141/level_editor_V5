import pygame, sys, os, random, math
from PIL import Image
from pygame.locals import*
pygame.init()

pygame.display.set_caption("SPRITESHEET GENERATOR")
FPS = pygame.time.Clock()

SCALE = 2
BLACK = (0,0,0,255)

image_path = "sketch.png"
SCREEN = pygame.display.set_mode((200,200), 0, 32)

session_image = pygame.image.load(image_path).convert()
SCREEN_DIMENSION = [session_image.get_width()*SCALE,session_image.get_height()*SCALE]
SCREEN = pygame.display.set_mode(SCREEN_DIMENSION, 0, 32)

image = session_image.copy()

click_once = True
group_tileset = False

initial_point = None
current_selection = None

selection_list = []
surface_clips = []

def clip_surface(surface,rect):
	surface_copy = surface.copy()
	rect_copy = rect.copy()       
	surface_copy.set_clip(rect_copy)
	new_surface = surface.subsurface(surface_copy.get_clip())

	return new_surface.copy()

def calc_new_dimension(surface_clips):
	clips_width = [clips.get_width() for clips in surface_clips]
	clips_height = [clips.get_height() for clips in surface_clips]
	
	new_width = max(clips_width)
	max_height = 0
	for height in clips_height:
		max_height += height
	
	return [new_width,max_height]

while 1:
	# mouse fucntions
	if group_tileset == False:
		image.fill((0,0,0))
		image.blit(session_image,(0,0))

	mx, my = pygame.mouse.get_pos()
	mx = mx//SCALE
	my = my//SCALE

	mouse_clicked = pygame.mouse.get_pressed()
	keys = pygame.key.get_pressed()

	#rectangular selector
	if mouse_clicked[2] and pygame.MOUSEMOTION:
		if click_once:
			click_once = False
			initial_point = [mx,my]

		scale_width = mx-initial_point[0]
		scale_height = my-initial_point[1]
		current_selection = pygame.Rect(initial_point[0],initial_point[1],scale_width,scale_height)
		pygame.draw.rect(image, (255,0,0), current_selection, 1)

	if selection_list and group_tileset == False:
		for selection in selection_list:
			pygame.draw.rect(image, (0,255,0), selection, 1)

	if keys[K_z] and click_once:
		click_once = False
		selection_list = selection_list[:-1]

	if keys[K_g] and click_once:
		click_once = False
		group_tileset = True
		surface_clips = [clip_surface(image,selection) for selection in selection_list]
		new_dimension = calc_new_dimension(surface_clips)
		SCREEN = pygame.display.set_mode((new_dimension[0]*SCALE,new_dimension[1]*SCALE),0,32)
		group_surface = pygame.Surface(new_dimension)
		image.fill((0,0,0))
		current_y_position = 0
		for clips in surface_clips:
			clips.set_colorkey((0,255,0))
			current_surface = group_surface.blit(clips,(0,current_y_position))
			current_y_position = current_surface.bottom
		image.blit(group_surface,(0,0))

	if keys[K_s] and click_once:
		click_once = False
		new_filename = input("[ENTER FILENAME] : ")
		pygame.image.save(group_surface, f"./tileset/{new_filename}.png")
		print("[TILESET SAVED!]")



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


