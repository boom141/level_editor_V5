from scripts import*

def main():
	last_time = time.time()
	click_once = False
	canvas.create_layers()

	while 1:
		delta_time = time.time() - last_time
		delta_time *= 60
		last_time = time.time()


		SCREEN.fill((0,0,0))
		UTILITIES.fill((45,45,45))
		if click_once:
			canvas.canvas_layering()

		keys = pygame.key.get_pressed()
		canvas.canvas_displacement({"UP":keys[K_w], "DOWN":keys[K_s], "LEFT":keys[K_a], "RIGHT":keys[K_d]},delta_time)
		
		mouse = pygame.mouse.get_pos()
		tile_row = int(mouse[0] - canvas.displacement[0]) // canvas.pixel_size
		tile_column = int(mouse[1] - canvas.displacement[1]) // canvas.pixel_size
		
		utils.render_folders(UTILITIES)
		utils.render_tileset(UTILITIES)
			
		pygame.draw.line(UTILITIES, (255,255,255), (0,150), (200,150), 3)
		for i in reversed(range(canvas.layers)):
			canvas.surface_layers[i].set_colorkey((25,25,25))
			SCREEN.blit(canvas.surface_layers[i],(int(canvas.displacement[0]),int(canvas.displacement[1])))
		SCREEN.blit(UTILITIES,(0,0))

		draw_text(SCREEN,(210,10),"Minecraft.ttf",20,text=utils.current_folder)
		draw_text(SCREEN,(210,35),"Minecraft.ttf",15,text=f"Layer: {canvas.current_layer}")
		draw_text(SCREEN,(210,455),"Minecraft.ttf",15,text=f"TILE: {tile_column},{tile_row}")
		draw_text(SCREEN,(210,480),"Minecraft.ttf",10,(0,255,0),text=f"FPS: {'{:.2f}'.format(FPS.get_fps())}")
		
		canvas.render_tiles()

		#events
		if mouse[0] > UTILITIES.get_width() and pygame.MOUSEMOTION:
			pygame.mouse.set_visible(False)
			if utils.current_folder not in canvas.exceptions:
				canvas.pixel_size = 32
				pygame.draw.rect(SCREEN, (255,255,255), (mouse[0] - 16,mouse[1] - 16,canvas.pixel_size,canvas.pixel_size), 1)
			else:
				img = loaded_images.image_database[utils.current_folder][utils.current_index]
				SCREEN.blit(img,(mouse[0],mouse[1]))
			
			if pygame.mouse.get_pressed()[0] and utils.current_folder != "None Selected" and canvas.current_layer != 0:
				pygame.draw.rect(SCREEN, (0,255,0), (mouse[0] - 16,mouse[1] - 16,32,32), 1)
				canvas.place_tile([tile_row,tile_column,utils.current_folder,utils.current_index,canvas.current_layer])
					
			elif pygame.mouse.get_pressed()[2] and utils.current_folder != "None Selected" and canvas.current_layer != 0:
				pygame.draw.rect(SCREEN, (255,0,0), (mouse[0] - 16,mouse[1] - 16,32,32), 1)
				canvas.remove_tile([tile_row,tile_column,canvas.current_layer])
		else:
			pygame.mouse.set_visible(True)
		
		
		for btn in utils.folders_button:
			if pygame.mouse.get_pressed()[0] and btn[0].collidepoint(pygame.mouse.get_pos()):
				utils.current_folder = btn[1]

		for btn in utils.tiles_button:
			if  pygame.mouse.get_pressed()[0] and btn[0].collidepoint(pygame.mouse.get_pos()):
				utils.current_index = btn[1]

		if keys[K_q] and click_once == False:
			click_once = True
			canvas.current_layer += 1

			if canvas.current_layer > canvas.layers-1:
				canvas.current_layer = 0

		if keys[K_e] and click_once == False:
			click_once = True
			canvas.current_layer -= 1
				
			if canvas.current_layer < 0:
				canvas.current_layer = canvas.layers-1

		if keys[K_LSHIFT] and click_once == False:
			click_once = True
			canvas.current_layer = 0

		if keys[K_RETURN]:
			click_once = True
			canvas.save_level()

		if keys[K_l]:
			click_once = True
			canvas.load_level()

		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if event.type == pygame.KEYUP:
					click_once = False

		FPS.tick(60)
		pygame.display.update()

if __name__ == "__main__":
	main()