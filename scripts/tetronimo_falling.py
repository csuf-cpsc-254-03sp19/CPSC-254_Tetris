import pygame

from pygame.sprite import Sprite
from game_object import GameObject

"""The falling tetronimo class. Created every time a new tetronimo must fall from the top of the screen."""
class TetronimoFalling(GameObject):
	def __init__(self, object_id, tag, position_x, position_y, tetronimo_type, \
			object_factory, settings, collision_box, sprite_images):
			
		super(TetronimoFalling, self).__init__(object_id, tag, position_x, position_y, \
				collision_box, sprite_images)
				
		"""Initialized the tetronimo falling game object."""
		
		# The tetronimo type. Use the number, not the character in parenthesis.
		# Rotation states are also shown. This follows the SRS Tetris format.
		#------------------------------
		# Type    R1    R2    R3    R4
		#------------------------------
		# 0(O) - .OO.  .OO.  .OO.  .OO.
		#	     .OO.  .OO.  .OO.  .OO.
		#        ....  ....  ....  ....
		#
		# 1(I) - ....  ..O.  ....  .O..
		#        OOOO  ..O.  ....  .O..
		#        ....  ..O.  OOOO  .O..
		#        ....  ..O.  ....  .O..
		#
		# 2(L) - O..   .OO   ...   .O.
		#        OOO   .O.   OOO   .O.
		#        ...   .O.   ..O   OO.
		#
		# 3(J) - ..O   .O.   ...   OO.
		#        OOO   .O.   OOO   .O.
		#        ...   .OO   O..   .O.
		#
		# 4(S) - .OO   O..   .OO   O..
		#        OO.   OO.   OO.   OO.
		#        ...   .O.   ...   .O.
		#
		# 5(Z) - OO.   ..O   OO.   .O.
		#        .OO   .OO   .OO   OO.
		#        ...   .O.   ...   O..
		#
		# 6(T) - .O.   .O.   ...   .O.
		#        OOO   .OO   OOO   OO.
		#        ...   .O.   .O.   .O.
		self.tetronimo_type = tetronimo_type
		
		# The rotation state of the tetronimo. See the graph above for the 4 rotation 
		# states.
		self.rotation_state = 0
		
		# A list of all the tetronimo blocks that belong to this game object.
		self.tetronimo_blocks = []
		
		# A reference to the game object factory. It is used to create the tetronimo 
		# blocks.
		self.object_factory = object_factory
		
		# A reference to the game settings.
		self.settings = settings
		
		# Create the tetronimo blocks that belong to this game object.
		self.create_tetronimo_blocks()
		
	def create_tetronimo_blocks(self):
		if self.tetronimo_type == 0:
			# The current tetronimo block being created.
			cur_tetronimo_block = self.object_factory.create_tetronimo_block(
					self.position_x - 16, self.position_y - 16, self.tetronimo_type)
			self.tetronimo_blocks.append(cur_tetronimo_block)
			
			cur_tetronimo_block = self.object_factory.create_tetronimo_block(
					self.position_x + 16, self.position_y - 16, self.tetronimo_type)
			self.tetronimo_blocks.append(cur_tetronimo_block)
			
			cur_tetronimo_block = self.object_factory.create_tetronimo_block(
					self.position_x - 16, self.position_y + 16, self.tetronimo_type)
			self.tetronimo_blocks.append(cur_tetronimo_block)
			
			cur_tetronimo_block = self.object_factory.create_tetronimo_block(
					self.position_x + 16, self.position_y + 16, self.tetronimo_type)
			self.tetronimo_blocks.append(cur_tetronimo_block)
