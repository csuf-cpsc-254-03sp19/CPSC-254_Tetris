import pygame

from pygame.sprite import Sprite
from game_object import GameObject

"""The tetronimo block class. Created every time a new tetronimo falling is created."""
class TetronimoBlock(GameObject):
	def __init__(self, object_id, tag, position_x, position_y, tetronimo_type, owner, settings, collision_box, sprite_images):
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
		
		# A reference to the owner that owns this tetronimo block. When landed, the block
		# will no longer use an owner.
		self.owner = owner
		
		# A reference to the settings object.
		self.settings = settings
		
		# A reference to the tetronimo blocks.
		self.tetronimo_blocks = self.settings.tetronimo_blocks
		
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
			
	def update(self, delta_time):
		"""Updates the tetronimo block object."""
		
		# If in the block state of falling, check to see if the block is colliding with 
		# the bottom of the screen. If so, change the falling tetronimo to not falling.
		if self.block_state == 0:
			# Check to see if the tetronimo block is at the container bound bottom.
			
			# Prevent the other blocks that haven't reached the bottom from making the 
			# tetronimo continue to fall.
			if self.owner.is_falling:
			
				# If the block is at the bottom of the screen, make the owner stop 
				# falling.
				if self.position_y + 16 >= self.settings.tetronimo_container_bounds[3]:
					self.owner.is_falling = False
					
			# Check to see if the tetronimo bloc is on top of another tetronimo block.
			for key in self.tetronimo_blocks:
				# The current tetronimo block being tested against.
				cur_block = self.tetronimo_blocks[key]
				
				# Only check for blocks that are in the landed state.
				if cur_block.block_state == 1:
					if cur_block.position_y == self.position_y + 32 and \
							cur_block.position_x == self.position_x:
						self.owner.is_falling = False
					
			# Check if the tetronimo owner can move left.
			if self.owner.can_move_left:
			
				# If the block is at the left of the screen, make the owner stop 
				# moving left.
				if self.position_x - 16 <= self.settings.tetronimo_container_bounds[0]:
					self.owner.can_move_left = False
					
				# Also check if there are any other blocks to the left of this block.
				for key in self.tetronimo_blocks:
					# The other block being checked for.
					cur_block_other = self.tetronimo_blocks[key]
					
					# Only check for blocks that have the same y position value and are 
					# just to the left of the block.
					if cur_block_other.position_y == self.position_y and \
							cur_block_other.block_state == 1 and \
							cur_block_other.position_x + 32 == self.position_x:
						self.owner.can_move_left = False
					
			# Check if the tetronimo owner can move right.
			if self.owner.can_move_right:
			
				# If the block is at the right of the screen, make the owner stop 
				# moving right.
				if self.position_x + 16 >= self.settings.tetronimo_container_bounds[1]:
					self.owner.can_move_right = False
					
				# Also check if there are any other blocks to the right of this block.
				for key in self.tetronimo_blocks:
					# The other block being checked for.
					cur_block_other = self.tetronimo_blocks[key]
					
					# Only check for blocks that have the same y position value and are 
					# just to the right of the block.
					if cur_block_other.position_y == self.position_y and \
							cur_block_other.block_state == 1 and \
							cur_block_other.position_x - 32 == self.position_x:
						self.owner.can_move_right = False
			
	def change_block_to_landed(self):
		self.block_state = 1
		self.cur_sprite_image = self.sprite_images["block_grey.png"]
