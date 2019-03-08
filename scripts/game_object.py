import pygame

from pygame.sprite import Sprite

"""The primary game object abstract class. All game object types are inherited from  this class. It contains a dictionary of sprite images, a position in 2D world space, and a collision box. The selection of the default sprite must be chosen by the inherited constuctor."""
class GameObject(Sprite):
	def __init__(self, objectID, positionX, positionY, collision_box, sprite_images):
		"""Initialized the game object."""
		print("Game object created.")
		
		# Checks if the object is marked for deletion, which will allow the object to
		# be deleted before the next frame is reached.
		self.marked_for_deletion = False
		
		# The game object ID.
		self.objectID = objectID
		
		# The x position of the game object in 2D world space.
		self.positionX = positionX
		
		# The y position of the game object in 2D world space.
		self.positionY = positionY
		
		# The current sprite image object being used for rendering.
		self.cur_sprite_image = None
		
		# The sprites to use. It is a dictionary of sprite image objects, where the
		# key is the file name of the sprite.
		self.sprite_images = sprite_images
		
		# The collision box used for collision detection. It is of type pygame.Rect
		self.collision_box = collision_box
