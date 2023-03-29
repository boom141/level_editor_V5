from scripts import*

def main():
	last_time = time.time()
	init_canvas.create_grid(CANVAS)

	while 1:
		SCREEN.fill((25,25,25))
		UTILITIES.fill((45,45,45))

		keys = pygame.key.get_pressed()
		ctx_features.canvas_displacement({"UP":keys[K_w], "DOWN":keys[K_s], "LEFT":keys[K_a], "RIGHT":keys[K_d]})
		
		mouse = pygame.mouse.get_pos()
		tile_row = int(mouse[0] - ctx_features.displacement[0]) // init_canvas.pixel_size
		tile_column = int(mouse[1] - ctx_features.displacement[1]) // init_canvas.pixel_size
		
		utils.render_folders(UTILITIES)
		utils.render_tileset(UTILITIES)

		pygame.draw.line(UTILITIES, (255,255,255), (0,150), (200,150), 3)
		SCREEN.blit(CANVAS,(int(ctx_features.displacement[0]),int(ctx_features.displacement[1])))
		SCREEN.blit(UTILITIES,(0,0))

		draw_text(SCREEN,(210,10),"Minecraft.ttf",20,text=utils.current_folder)
		draw_text(SCREEN,(210,460),"Minecraft.ttf",15,text=f"TILE: {tile_column},{tile_row}")
		
		init_canvas.render_tiles(CANVAS)

		#events
		if mouse[0] > UTILITIES.get_width() and pygame.MOUSEMOTION:
			if pygame.mouse.get_pressed()[0]:
				ctx_features.place_tile([tile_row,tile_column])

		for btn in utils.folders_button:
			if pygame.mouse.get_pressed()[0] and btn[0].collidepoint(pygame.mouse.get_pos()):
				utils.current_folder = btn[1]

		for btn in utils.tiles_button:
			if  pygame.mouse.get_pressed()[0] and btn[0].collidepoint(pygame.mouse.get_pos()):
				utils.current_index = btn[1]
				
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

		FPS.tick(60)
		pygame.display.update()

if __name__ == "__main__":
	main()