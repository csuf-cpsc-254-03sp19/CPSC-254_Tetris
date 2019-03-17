import pygame

from pygame.sprite import Sprite
from game_object import GameObject

"""The tetronimo block class. Created every time a new tetronimo falling is created."""
class TetronimoBlock(GameObject):
	def __init__(self, object_id, tag, position_x, position_y, tetronimo_type, collision_box, sprite_images):
		super(TetronimoBlock, self).__init__(object_id, tag, position_x, position_y, collision_box, sprite_images)
		"""Initialized the tetronimo block game object."""
		
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
		self.tetronimo_type = tetronimo_type
		
		# The block state of the tetronimo block.
		# 0 - Falling.
		# 1 - Landed.
		# 2 - Frozen.
		self.block_state = 0
		
		# Set the correct image sprite based on the tetronimo type.
		if self.tetronimo_type == 0:
			self.cur_sprite_image = self.sprite_images["block_yellow.png"]
