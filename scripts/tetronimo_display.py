import pygame

from pygame.sprite import Sprite
from game_object import GameObject

"""The tetronimo display class. Displays a tetronimo as an image. Only used for the GUI."""
class TetronimoDisplay(GameObject):
	def __init__(self, object_id, tag, position_x, position_y, collision_box, sprite_images):
		"""Initialized the tetronimo image game object."""
	
		# Call the inherited class constructor.
		super(TetronimoDisplay, self).__init__(object_id, tag, position_x, position_y, collision_box, sprite_images)
		
		# The image type.
		# 0 - O tetronimo.
		# 1 - I tetronimo.
		# 2 - L tetronimo.
		# 3 - J tetronimo.
		# 4 - S tetronimo.
		# 5 - Z tetronimo.
		# 6 - T tetronimo.
		# 7 - n/a
		self.image_type = 0
			
		self.cur_sprite_image = self.sprite_images["display_none.png"]
			
	def update(self, delta_time):
		"""Updates the tetronimo display object."""
		
		if self.image_type == 0 and \
				not self.cur_sprite_image == self.sprite_images["display_O.png"]:
			self.cur_sprite_image = self.sprite_images["display_O.png"]
		elif self.image_type == 1 and \
				not self.cur_sprite_image == self.sprite_images["display_I.png"]:
			self.cur_sprite_image = self.sprite_images["display_I.png"]
		elif self.image_type == 2 and \
				not self.cur_sprite_image == self.sprite_images["display_L.png"]:
			self.cur_sprite_image = self.sprite_images["display_L.png"]
		elif self.image_type == 3 and \
				not self.cur_sprite_image == self.sprite_images["display_J.png"]:
			self.cur_sprite_image = self.sprite_images["display_J.png"]
		elif self.image_type == 4 and \
				not self.cur_sprite_image == self.sprite_images["display_S.png"]:
			self.cur_sprite_image = self.sprite_images["display_S.png"]
		elif self.image_type == 5 and \
				not self.cur_sprite_image == self.sprite_images["display_Z.png"]:
			self.cur_sprite_image = self.sprite_images["display_Z.png"]
		elif self.image_type == 6 and \
				not self.cur_sprite_image == self.sprite_images["display_T.png"]:
			self.cur_sprite_image = self.sprite_images["display_T.png"]
		elif self.image_type == 7 and \
				not self.cur_sprite_image == self.sprite_images["display_none.png"]:
			self.cur_sprite_image = self.sprite_images["display_none.png"]
