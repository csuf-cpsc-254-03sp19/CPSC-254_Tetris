import pygame

from pygame.sprite import Sprite
from game_object import GameObject
from sprite_image import SpriteImage

"""The primary game object abstract class. All game object types are inherited from  this class. It contains a dictionary of sprite images, a position in 2D world space, and a collision box. The selection of the default sprite must be chosen by the inherited constuctor."""
class TextBox(GameObject):
	def __init__(self, object_id, tag, position_x, position_y, text, font, color, \
			align_bottom_left, collision_box, sprite_images):
		super(TextBox, self).__init__(object_id, tag, position_x, position_y, collision_box, sprite_images)
		"""Initialized the game object."""
		
		# Checks if the text box needs to be aligned to the bottom left.
		self.align_bottom_left = align_bottom_left
		
		# The original x position.
		self.original_x = position_x
		
		# The original y position.
		self.original_y = position_y
		
		# The text of the text box.
		self.text = text
		
		# The color of the text in the text box.
		self.color = color
		
		# The font being used to render the text in the text box.
		self.font = font
		
		self.set_text(self.text)

	def set_text(self, text):
		self.text = text
		
		# The current sprite image object being used for rendering.
		self.cur_sprite_image = SpriteImage(1, self.font.render(self.text, True, self.color))

		if self.align_bottom_left:
			self.image_rect.centerx = self.original_x
			self.image_rect.centery = self.original_y
			self.position_x = self.image_rect.right
			self.position_y = self.image_rect.bottom
			self.image_rect.centerx = self.position_x
			self.image_rect.centery = self.position_y

	def get_text(self):
		return self.text
		