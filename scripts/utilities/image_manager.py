import pygame, os


class image_loader:
	def __init__(self,root_folder):
		self.root_folder = root_folder
		self.image_database = {}

	def load(self):
		for folder in os.listdir(self.root_folder):
			image_con = []
			for file in os.listdir(f'{self.root_folder}/{folder}'):
				image = pygame.image.load(f'{self.root_folder}/{folder}/{file}').convert()
				image.set_colorkey((0,0,0))	
				if folder not in ["foliage","decoration"]:
					image = pygame.transform.scale(image, (32,32))
				image_con.append(image)
			self.image_database[f'{folder}'] = image_con