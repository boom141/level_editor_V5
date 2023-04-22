from scripts import*

def main():

	pygame.draw.rect(SCREEN, (255,255,255), (0,0,2,2))
	print(SCREEN.get_at((0,0)))

	while 1:
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