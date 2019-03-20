import pygame

from pygame.sprite import Sprite
from game_object import GameObject

"""The falling tetronimo class. Created every time a new tetronimo must fall from the top of the screen."""
class TetronimoFalling(GameObject):
	def __init__(self, object_id, tag, position_x, position_y, tetronimo_type, \
			object_factory, settings, collision_box, sprite_images):
		"""Initialized the tetronimo falling game object."""
			
		# Call the inherited class constructor.
		super(TetronimoFalling, self).__init__(object_id, tag, position_x, position_y, \
				collision_box, sprite_images)
		
		# Checks if the tetronimo is falling.
		self.is_falling = True
		
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
		# 2(J) - ..O   .O.   ...   OO.
		#        OOO   .O.   OOO   .O.
		#        ...   .OO   O..   .O.
		#
		# 3(L) - O..   .OO   ...   .O.
		#        OOO   .O.   OOO   .O.
		#        ...   .O.   ..O   OO.
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
		"""Create the tetronimo blocks for the falling tetronimo."""
		
		# Different types of tetronimo blocks will have different block positions and 
		# colors.
		if self.tetronimo_type == 0:
			self.create_tetronimo_block(self.position_x - 16, self.position_y - 16)
			self.create_tetronimo_block(self.position_x + 16, self.position_y - 16)
			self.create_tetronimo_block(self.position_x - 16, self.position_y + 16)
			self.create_tetronimo_block(self.position_x + 16, self.position_y + 16)
			
		elif self.tetronimo_type == 1:
			self.create_tetronimo_block(self.position_x - 48, self.position_y + 32)
			self.create_tetronimo_block(self.position_x - 16, self.position_y + 32)
			self.create_tetronimo_block(self.position_x + 16, self.position_y + 32)
			self.create_tetronimo_block(self.position_x + 48, self.position_y + 32)
			
		elif self.tetronimo_type == 2:
			self.create_tetronimo_block(self.position_x, self.position_y)
			self.create_tetronimo_block(self.position_x - 32, self.position_y)
			self.create_tetronimo_block(self.position_x + 32, self.position_y)
			self.create_tetronimo_block(self.position_x - 32, self.position_y - 32)
		
		elif self.tetronimo_type == 3:
			self.create_tetronimo_block(self.position_x, self.position_y)
			self.create_tetronimo_block(self.position_x - 32, self.position_y)
			self.create_tetronimo_block(self.position_x + 32, self.position_y)
			self.create_tetronimo_block(self.position_x + 32, self.position_y - 32)
			
		elif self.tetronimo_type == 4:
			self.create_tetronimo_block(self.position_x, self.position_y)
			self.create_tetronimo_block(self.position_x, self.position_y - 32)
			self.create_tetronimo_block(self.position_x + 32, self.position_y - 32)
			self.create_tetronimo_block(self.position_x - 32, self.position_y)
			
		elif self.tetronimo_type == 5:
			self.create_tetronimo_block(self.position_x, self.position_y)
			self.create_tetronimo_block(self.position_x, self.position_y - 32)
			self.create_tetronimo_block(self.position_x - 32, self.position_y - 32)
			self.create_tetronimo_block(self.position_x + 32, self.position_y)
			
		elif self.tetronimo_type == 6:
			self.create_tetronimo_block(self.position_x, self.position_y)
			self.create_tetronimo_block(self.position_x - 32, self.position_y)
			self.create_tetronimo_block(self.position_x + 32, self.position_y)
			self.create_tetronimo_block(self.position_x, self.position_y - 32)
			
	def create_tetronimo_block(self, position_x, position_y):
		"""Create a single tetronimo block."""
		
		# The current tetronimo block being created.
		cur_tetronimo_block = self.object_factory.create_tetronimo_block(
				position_x, position_y, self.tetronimo_type, self)
		self.tetronimo_blocks.append(cur_tetronimo_block)
		
	def update(self, delta_time):
		"""Updates the falling tetronimo object."""
		
		# Update all the tetronimo blocks that belong to this falling tetronimo object.
		for block in self.tetronimo_blocks:
			block.update(delta_time)
			
	def drive(self):
		"""Move the blocks that belong to this tetronimo if not at the bottom of the screen."""
		if not self.is_falling:
			# Destroy the falling tetronimo. This will not destroy the blocks that make 
			# the tetronimo, and the blocks will be landed.
			self.marked_for_deletion = True
			
			self.settings.tetronimo_assembly_state = 1
			
			# Set the blocks to the landed state.
			for block in self.tetronimo_blocks:
				block.block_state = 1
		else:
			self.move_blocks(0, 32)
		
	def move_blocks(self, delta_x, delta_y):
		"""Change the x or y position by a certain amount."""
		self.position_x += delta_x
		self.position_y += delta_y
		
		# Update the x and y position for the tetronimo blocks that belong to this 
		# tetronimo.
		for block in self.tetronimo_blocks:
			block.position_x += delta_x
			block.position_y += delta_y
