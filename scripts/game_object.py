import pygame

from pygame.sprite import Sprite


class GameObject(Sprite):
	def __init__(self, objectID, positionX, positionY):
		"""Initialized the game object."""
		print("Game object created.")
		
		# The game object ID.
		self.objectID = objectID
		
		# The x position of the game object in 2D world space.
		self.positionX = positionX
		
		# The y position of the game object in 2D world space.
		self.positionY = positionY
