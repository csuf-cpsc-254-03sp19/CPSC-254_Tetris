import pygame

from pygame.sprite import Sprite

"""The sprite image object for containing an image and an image rect."""
class SpriteImage():
	def __init__(self, image_layer, image):
		"""Initialized the sprite image."""
		print("Sprite image created.")
		
		# The image layer for the painter's algorithm.
		self.image_layer = image_layer
		
		# The sprite image that can be rendered.
		self.image = image
		
		# The current image rect of the original rect.
		cur_image_rect = image.get_rect()
		
		# The new copy of the original image rect.
		self.image_rect = pygame.Rect(0, 0, 
			cur_image_rect.width, cur_image_rect.height)
		
	def update_image_rect(self, position_x, position_y):
		"""Updates the image rect's position."""
		self.image_rect.centerx = position_x
		self.image_rect.centery = position_y
