import pygame

from pygame.sprite import Sprite
from game_object import GameObject

"""The falling tetronimo class. Created every time a new tetronimo must fall from the top of the screen."""
class TetronimoFalling(GameObject):
	def __init__(self, object_id, tag, position_x, position_y, tetronimo_type, \
			object_factory, settings, input_manager, collision_box, sprite_images):
		"""Initialized the tetronimo falling game object."""
			
		# Call the inherited class constructor.
		super(TetronimoFalling, self).__init__(object_id, tag, position_x, position_y, \
				collision_box, sprite_images)
		
		# Checks if the tetronimo is falling.
		self.is_falling = True
		
		# Checks if the tetronimo can move left.
		self.can_move_left = True
		
		# Checks if the tetronimo can move right.
		self.can_move_right = True
		
		# Checks if the left key was pressed.
		self.pressed_left = False
		
		# Checks if the right key was pressed.
		self.pressed_right = False
		
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
		
		# The current horizontal frame for horizontal movement.
		self.cur_horizontal_frame = 0
		
		# The maximum horizontal frame for horizontal movement.
		self.max_horizontal_frame = 8
		
		# A list of all the tetronimo blocks that belong to this game object.
		self.tetronimo_blocks = []
		
		# A reference to the game object factory. It is used to create the tetronimo 
		# blocks.
		self.object_factory = object_factory
		
		# A reference to the game settings.
		self.settings = settings
		
		# A reference to the input manager.
		self.input_manager = input_manager
		
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
		
		self.can_move_left = True
		self.can_move_right = True
			
		# Update all the tetronimo blocks that belong to this falling tetronimo object.
		for block in self.tetronimo_blocks:
			block.update(delta_time)
			
		# Check if the left or right key is pressed while a piece is falling. If so, 
		# move the piece left or right.
		if self.settings.tetronimo_assembly_state == 0:
			
			# Check if pressing the left key.
			if self.input_manager.pressed_left:
				# Reset the movement frame if haven't pressed left previously.
				if not self.pressed_left:
					self.cur_horizontal_frame = self.max_horizontal_frame
				self.pressed_left = True
			else:
				self.pressed_left = False
				
				
			# Check if pressing the right key.
			if self.input_manager.pressed_right:
				# Reset the movement frame if haven't pressed left previously.
				if not self.pressed_right:
					self.cur_horizontal_frame = self.max_horizontal_frame
				self.pressed_right = True
			else:
				self.pressed_right = False
				
			# Drive the tetronimo to move left if able.
			if self.can_move_left and self.pressed_left:
				if self.cur_horizontal_frame == self.max_horizontal_frame:
					self.cur_horizontal_frame = 0
					self.position_x -= 32
					for block in self.tetronimo_blocks:
						block.position_x -= 32
				else:
					self.cur_horizontal_frame += 1
					
			# Drive the tetronimo to move right if able.
			if self.can_move_right and self.pressed_right:
				if self.cur_horizontal_frame == self.max_horizontal_frame:
					self.cur_horizontal_frame = 0
					self.position_x += 32
					for block in self.tetronimo_blocks:
						block.position_x += 32
				else:
					self.cur_horizontal_frame += 1
			
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
