import pygame

from pygame.sprite import Sprite
from game_object import GameObject

"""The tetronimo block class. Created every time a new tetronimo falling is created."""
class TetronimoBlock(GameObject):
	def __init__(self, object_id, tag, position_x, position_y, tetronimo_type, collision_box, sprite_images):
		"""Initialized the tetronimo block game object."""
	
		# Call the inherited class constructor.
		super(TetronimoBlock, self).__init__(object_id, tag, position_x, position_y, collision_box, sprite_images)
		
		# The tetronimo type. Use the number, not the character in parenthesis.
		# Different tetronimo types are different colors.
		#-----------------------
		# Type   shape color
		#-----------------------
		# 0(O) - .OO.  yellow
		#	     .OO.
		#        ....
		#
		# 1(I) - ....  sky blue
		#        OOOO
		#        ....
		#        ....
		#
		# 2(L) - O..   orange
		#        OOO
		#        ...
		#
		# 3(J) - ..O   blue
		#        OOO
		#        ...
		#
		# 4(S) - .OO   green
		#        OO.
		#        ...
		#
		# 5(Z) - OO.   red
		#        .OO
		#        ...
		#
		# 6(T) - .O.   purple
		#        OOO
		#        ...
		#
		# 7(F) - n/a   grey
		self.tetronimo_type = tetronimo_type
		
		# The block state of the tetronimo block.
		# 0 - Falling.
		# 1 - Landed.
		# 2 - Frozen.
		self.block_state = 0
		
		# Set the correct image sprite based on the tetronimo type.
		if self.tetronimo_type == 0:
			self.cur_sprite_image = self.sprite_images["block_yellow.png"]
		elif self.tetronimo_type == 1:
			self.cur_sprite_image = self.sprite_images["block_skyblue.png"]
		elif self.tetronimo_type == 2:
			self.cur_sprite_image = self.sprite_images["block_blue.png"]
		elif self.tetronimo_type == 3:
			self.cur_sprite_image = self.sprite_images["block_orange.png"]
		elif self.tetronimo_type == 4:
			self.cur_sprite_image = self.sprite_images["block_green.png"]
		elif self.tetronimo_type == 5:
			self.cur_sprite_image = self.sprite_images["block_red.png"]
		elif self.tetronimo_type == 6:
			self.cur_sprite_image = self.sprite_images["block_purple.png"]
		elif self.tetronimo_type == 7:
			self.cur_sprite_image = self.sprite_images["block_grey.png"]
