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
		
		# Checks if the tetronimo can rotate.
		self.can_rotate = True
		
		# Checks if the left key was pressed.
		self.pressed_left = False
		
		# Checks if the right key was pressed.
		self.pressed_right = False
		
		# Checks if the rotate key was pressed.
		self.pressed_rotate = False
		
		# Checks if the auto land key was pressed.
		self.pressed_autoland = False
		
		# The tetronimo type. Use the number, not the character in parenthesis.
		# Rotation states are also shown. This follows the SRS Tetris format (except the s 
		# and z tetronimos).
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
		# 2(L) - ..O   .O.   ...   OO.
		#        OOO   .O.   OOO   .O.
		#        ...   .OO   O..   .O.
		#
		# 3(J) - O..   .OO   ...   .O.
		#        OOO   .O.   OOO   .O.
		#        ...   .O.   ..O   OO.
		#
		# 4(S) - .OO   O..   .OO   O..
		#        OO.   OO.   OO.   OO.
		#        ...   .O.   ...   .O.
		#
		# 5(Z) - OO.   ..O   OO.   ..O
		#        .OO   .OO   .OO   .OO
		#        ...   .O.   ...   .O.
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
		
		# The four rotations of the tetronimo. Contains a list of tuples for the x and y 
		# positions of each block.
		self.rotations = []
		
		# The kick positions for the tetronimo for all 4 rotations. Contains tuples with 4 
		# values:
		# 0 - position_x,
		# 1 - position_y,
		# 2 - direction - 0 - left, 1 - right, 2 - up, 3 - down,
		# 3 - kick_offset,
		self.kick_positions = []
		
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
		
		# The cached x and y position of the tetronimo.
		pos_x = self.position_x
		pos_y = self.position_y
			
		# The rotation position lists of the tetronimo.
		rotation1 = []
		rotation2 = []
		rotation3 = []
		rotation4 = []
		
		# The kick position arrays of the tetronimos for different rotations.
		kick1 = []
		kick2 = []
		kick3 = []
		kick4 = []
		
		# Different types of tetronimo blocks will have different block positions and 
		# colors.
		if self.tetronimo_type == 0:
			
			# .OO.
			# .OO.
			# ....
			rotation1.append((-16, -16))
			rotation1.append((16, -16))
			rotation1.append((-16, 16))
			rotation1.append((16, 16))
			
			rotation2 = rotation1
			rotation3 = rotation1
			rotation4 = rotation1
			
		elif self.tetronimo_type == 1:
			
			# 1(I) - ....  ..O.  ....  .O..
			#        OOOO  ..O.  ....  .O..
			#        ....  ..O.  OOOO  .O..
			#        ....  ..O.  ....  .O..
			rotation1.append((-48, 32))
			rotation1.append((-16, 32))
			rotation1.append((16, 32))
			rotation1.append((48, 32))
			
			rotation2.append((16, 96))
			rotation2.append((16, 64))
			rotation2.append((16, 32))
			rotation2.append((16, 0))
			
			rotation3.append((-48, 64))
			rotation3.append((-16, 64))
			rotation3.append((16, 64))
			rotation3.append((48, 64))
			
			rotation4.append((-16, 96))
			rotation4.append((-16, 64))
			rotation4.append((-16, 32))
			rotation4.append((-16, 0))
			
			kick1.append((-16, 32, 0, 64))
			kick1.append((-48, 32, 0, 32))
			kick1.append((48, 32, 1, -32))
			kick1.append((16, 32, 1, -64))
			
			kick2.append((16, 0, 2, 32))
			kick2.append((16, 64, 3, -64))
			kick2.append((16, 96, 3, -32))
			
			kick3.append((-16, 64, 0, 64))
			kick3.append((-48, 64, 0, 32))
			kick3.append((48, 64, 1, -32))
			kick3.append((16, 64, 1, -64))
			
			kick4.append((-16, 0, 2, 32))
			kick4.append((-16, 32, 2, 64))
			kick4.append((-16, 96, 3, -32))
			
		elif self.tetronimo_type == 2:
			
			# 2(L) - ..O   .O.   ...   OO.
			#        OOO   .O.   OOO   .O.
			#        ...   .OO   O..   .O.
			rotation1.append((0, 0))
			rotation1.append((-32, 0))
			rotation1.append((32, 0))
			rotation1.append((32, -32))
			
			rotation2.append((0, 0))
			rotation2.append((0, -32))
			rotation2.append((0, 32))
			rotation2.append((32, 32))
			
			rotation3.append((0, 0))
			rotation3.append((-32, 0))
			rotation3.append((32, 0))
			rotation3.append((-32, 32))
			
			rotation4.append((0, 0))
			rotation4.append((0, -32))
			rotation4.append((0, 32))
			rotation4.append((-32, -32))
			
			kick1.append((-32, 0, 0, 32))
			kick1.append((32, 0, 2, 32))
			kick1.append((32, -32, 1, -32))
			kick1.append((32, -32, 2, 32))
			
			kick2.append((0, -32, 2, 32))
			kick2.append((0, 32, 3, -32))
			kick2.append((32, 32, 3, -32))
			kick2.append((32, 32, 1, -32))
			
			kick3.append((-32, 0, 0, 32))
			kick3.append((32, 0, 1, -32))
			kick3.append((-32, 32, 3, -32))
			kick3.append((-32, 32, 0, 32))
			
			kick4.append((0, -32, 2, 32))
			kick4.append((0, 32, 3, -32))
			kick4.append((-32, -32, 2, 32))
			kick4.append((-32, -32, 0, 32))
		
		elif self.tetronimo_type == 3:
			
			# 3(J) - O..   .OO   ...   .O.
			#        OOO   .O.   OOO   .O.
			#        ...   .O.   ..O   OO.
			rotation1.append((0, 0))
			rotation1.append((-32, 0))
			rotation1.append((32, 0))
			rotation1.append((-32, -32))
			
			rotation2.append((0, 0))
			rotation2.append((0, -32))
			rotation2.append((0, 32))
			rotation2.append((32, -32))
			
			rotation3.append((0, 0))
			rotation3.append((-32, 0))
			rotation3.append((32, 0))
			rotation3.append((32, 32))
			
			rotation4.append((0, 0))
			rotation4.append((0, 32))
			rotation4.append((0, -32))
			rotation4.append((-32, 32))
			
			kick1.append((-32, 0, 0, 32))
			kick1.append((32, 0, 1, -32))
			kick1.append((-32, -32, 0, 32))
			kick1.append((-32, -32, 2, 32))
			
			kick2.append((0, -32, 3, -32))
			kick2.append((0, 32, 2, 32))
			kick2.append((32, -32, 3, -32))
			kick2.append((32, -32, 1, -32))
			
			kick3.append((-32, 0, 0, 32))
			kick3.append((32, 0, 1, -32))
			kick3.append((32, 32, 3, -32))
			kick3.append((32, 32, 1, -32))
			
			kick4.append((0, -32, 2, 32))
			kick4.append((0, 32, 3, -32))
			kick4.append((-32, 32, 3, -32))
			kick4.append((-32, 32, 1, -32))
			
		elif self.tetronimo_type == 4:
			
			# 4(S) - .OO   O..   .OO   O..
			#        OO.   OO.   OO.   OO.
			#        ...   .O.   ...   .O.
			rotation1.append((0, 0))
			rotation1.append((0, -32))
			rotation1.append((32, -32))
			rotation1.append((-32, 0))
			
			rotation2.append((0, 0))
			rotation2.append((-32, 0))
			rotation2.append((-32, -32))
			rotation2.append((0, 32))
			
			rotation3.append((0, 0))
			rotation3.append((0, -32))
			rotation3.append((32, -32))
			rotation3.append((-32, 0))
			
			rotation4.append((0, 0))
			rotation4.append((-32, 0))
			rotation4.append((-32, -32))
			rotation4.append((0, 32))
			
			kick1.append((-32, 0, 0, 32))
			kick1.append((0, -32, 2, 32))
			kick1.append((32, -32, 1, -32))
			kick1.append((32, -32, 2, 32))
			
			kick2.append((-32, 0, 0, 32))
			kick2.append((0, 32, 3, -32))
			kick2.append((-32, -32, 0, 32))
			kick2.append((-32, -32, 2, 32))
			
			kick3.append((-32, 0, 0, 32))
			kick3.append((0, -32, 2, 32))
			kick3.append((32, -32, 1, -32))
			kick3.append((32, -32, 2, 32))
			
			kick4.append((-32, 0, 0, 32))
			kick4.append((0, 32, 3, -32))
			kick4.append((-32, -32, 0, 32))
			kick4.append((-32, -32, 2, 32))
			
		elif self.tetronimo_type == 5:
			
			# 5(Z) - OO.   ..O   OO.   ..O
			#        .OO   .OO   .OO   .OO
			#        ...   .O.   ...   .O.
			rotation1.append((0, 0))
			rotation1.append((0, -32))
			rotation1.append((-32, -32))
			rotation1.append((32, 0))
			
			rotation2.append((0, 0))
			rotation2.append((0, 32))
			rotation2.append((32, 0))
			rotation2.append((32, -32))
			
			rotation3.append((0, 0))
			rotation3.append((0, -32))
			rotation3.append((-32, -32))
			rotation3.append((32, 0))
			
			rotation4.append((0, 0))
			rotation4.append((0, 32))
			rotation4.append((32, 0))
			rotation4.append((32, -32))
			
			kick1.append((32, 0, 1, -32))
			kick1.append((0, -32, 2, 32))
			kick1.append((-32, -32, 0, 32))
			kick1.append((-32, -32, 2, 32))
			
			kick2.append((32, 0, 1, -32))
			kick2.append((0, 32, 3, -32))
			kick2.append((32, -32, 0, 32))
			kick2.append((32, -32, 2, 32))
			
			kick3.append((32, 0, 1, -32))
			kick3.append((0, -32, 2, 32))
			kick3.append((-32, -32, 0, 32))
			kick3.append((-32, -32, 2, 32))
			
			kick4.append((32, 0, 1, -32))
			kick4.append((0, 32, 3, -32))
			kick4.append((32, -32, 0, 32))
			kick4.append((32, -32, 2, 32))
			
		elif self.tetronimo_type == 6:
			
			# 6(T) - .O.   .O.   ...   .O.
			#        OOO   .OO   OOO   OO.
			#        ...   .O.   .O.   .O.
			rotation1.append((0, 0))
			rotation1.append((-32, 0))
			rotation1.append((32, 0))
			rotation1.append((0, -32))
			
			rotation2.append((0, 0))
			rotation2.append((0, -32))
			rotation2.append((0, 32))
			rotation2.append((32, 0))
			
			rotation3.append((0, 0))
			rotation3.append((-32, 0))
			rotation3.append((32, 0))
			rotation3.append((0, 32))
			
			rotation4.append((0, 0))
			rotation4.append((0, -32))
			rotation4.append((0, 32))
			rotation4.append((-32, 0))
			
			kick1.append((32, 0, 1, -32))
			
			kick2.append((0, 32, 3, -32))
			
			kick3.append((-32, 0, 0, 32))
			
			kick4.append((0, -32, 1, 32))
			
		self.rotations.append(rotation1)
		self.rotations.append(rotation2)
		self.rotations.append(rotation3)
		self.rotations.append(rotation4)
			
		self.kick_positions.append(kick1)
		self.kick_positions.append(kick2)
		self.kick_positions.append(kick3)
		self.kick_positions.append(kick4)
		
		self.create_4_tetronimo_blocks(pos_x, pos_y, rotation1)
			
	def create_4_tetronimo_blocks(self, pos_x, pos_y, rotation):
		"""Creates the 4 tetronimo blocks for the tetronimo using the first rotation."""
		self.create_tetronimo_block(pos_x + rotation[0][0], pos_y + rotation[0][1])
		self.create_tetronimo_block(pos_x + rotation[1][0], pos_y + rotation[1][1])
		self.create_tetronimo_block(pos_x + rotation[2][0], pos_y + rotation[2][1])
		self.create_tetronimo_block(pos_x + rotation[3][0], pos_y + rotation[3][1])
			
	def create_tetronimo_block(self, position_x, position_y):
		"""Create a single tetronimo block."""
		
		# The current tetronimo block being created.
		cur_tetronimo_block = self.object_factory.create_tetronimo_block(
				position_x, position_y, self.tetronimo_type, self)
		self.tetronimo_blocks.append(cur_tetronimo_block)
		
	def update(self, delta_time):
		"""Updates the falling tetronimo object."""
		
		self.is_falling = True
		self.can_move_left = True
		self.can_move_right = True
		self.can_rotate = True
			
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
				
			# Check if pressing the rotate key.
			if self.input_manager.pressed_z:
				# If haven't rotated previously, rotate the tetronimo.
				if not self.pressed_rotate:
					# Increment the rotation index. If equal to 3, set it to zero.
					if self.rotation_state < 3:
						self.rotation_state += 1
					else:
						self.rotation_state = 0
					
					# Checks if the tetronimo can rotate.
					can_rotate = True
					
					# Checks if the tetronimo was kicked.
					kicked = False
					
					self.rotate_blocks()
						
					print("kick attempts.")
					
					# Before keeping a rotation, check to see if the tetronimo can 
					# actually rotate, or if it needs to kick a wall. If not, change back 
					# to the previous rotation.
					for kick in self.kick_positions[self.rotation_state]:
						# The kick direction.
						kick_direction = kick[2]
						
						# The kick position in the x coordinate.
						kick_pos_x = kick[0]
						
						# The kick position in the y coordinate.
						kick_pos_y = kick[1]
						
						# The kick offset, in either the x or y coordinate.
						kick_offset = kick[3]
						
						return_values = None
						
						if kick_direction == 0:
							return_values = self.kick_tetronimo_attempt(
								kick_pos_x, kick_pos_y, kick_offset, True, False)
						elif kick_direction == 1:
							return_values = self.kick_tetronimo_attempt(
								kick_pos_x, kick_pos_y, kick_offset, True, True)
						elif kick_direction == 2:
							return_values = self.kick_tetronimo_attempt(
								kick_pos_x, kick_pos_y, kick_offset, False, False)
						elif kick_direction == 3:
							return_values = self.kick_tetronimo_attempt(
								kick_pos_x, kick_pos_y, kick_offset, False, True)
								
						can_rotate = return_values[0]
						kicked = return_values[1]
								
						# If the tetronimo was kicked, exit the kicking loop.
						if kicked or not can_rotate:
							break
							
					# If the rotation failed, rotate the piece back to its original 
					# position.
					if not can_rotate:
						self.rotation_state
						# Decrement the rotation index. If equal to 0, set it to 3.
						if self.rotation_state > 0:
							self.rotation_state -= 1
						else:
							self.rotation_state = 3
							
						self.rotate_blocks()
					
				self.pressed_rotate = True
			else:
				self.pressed_rotate = False
				
			# Check if pressig the auto land key.
			if self.input_manager.pressed_x:
				# Get the largest block value and use that as the offset for the landing 
				# position.
				largest_y = 0 
				
				# First, check if the tetronimo can land on another tetronimo.
				
				# Checks if the tetronimo landed on another tetronimo.
				land_on_tetronimo = False
				
				# The amount by which to offset the tetronimo falling so that it reaches 
				# the bottom of the screen or on top of another tetronimo.
				offset_amount_y = 0
				
				# The shortest y distance found. It will be used as the offset amount for
				# the tetronimo.
				shortest_y_distance = 999.0
				
				# First, check for the shortest distance between the owner's tetronimo 
				# blocks and the other tetronimo blocks.
				for cur_block in self.tetronimo_blocks:
					for key in self.settings.tetronimo_blocks:
						# The current tetronimo block other.
						cur_block_other = self.settings.tetronimo_blocks[key]
						
						# Check if the other block has the same x coordinate as the 
						# current block and is in the landed block state.
						if cur_block_other.block_state == 1 and \
								cur_block.position_x == cur_block_other.position_x and \
								cur_block.position_y < cur_block_other.position_y:
								
							cur_y_distance = cur_block_other.position_y - \
									cur_block.position_y - 32
									
							# If the distance is shorter than the previous distance, 
							# update the shortest y distance.
							if cur_y_distance < shortest_y_distance:
								shortest_y_distance = cur_y_distance
				
				# Next, check if the tetronimo can also reach the bottom of the screen.
				
				# Get the largest y position of the tetronimo.
				for block in self.tetronimo_blocks:
					if block.position_y > largest_y:
						largest_y = block.position_y
				
				# The amount by which to offset the tetronimo falling so that it reaches 
				# the bottom of the screen.
				cur_y_distance = self.settings.tetronimo_container_bounds[3] - \
						largest_y - 16
						
				# If the distance is shorter than the previous distance, 
				# update the shortest y distance.
				if cur_y_distance < shortest_y_distance:
					shortest_y_distance = cur_y_distance
				
				offset_amount_y = shortest_y_distance
				
				self.position_y += offset_amount_y
				
				# Also update the positions of the tetronimo blocks to reach the bottom of 
				# the game screen.
				for block in self.tetronimo_blocks:
					block.position_y += offset_amount_y
					
				self.settings.delta_time_accum = 0
				
				# Force the tetronimo assembly to increment.
				self.settings.tetronimo_inc = True
				self.is_falling = False
				
			# Update all the tetronimo blocks that belong to this falling tetronimo object.
			for block in self.tetronimo_blocks:
				block.update(delta_time)
				
			# The drive for moving the tetronimo or setting it into the landed state.
			if self.settings.tetronimo_inc:
				# If no longer falling, destroy the tetronimo.
				if not self.is_falling:
					# Destroy the falling tetronimo. This will not destroy the blocks that make 
					# the tetronimo, and the blocks will be landed.
					self.marked_for_deletion = True
					
					self.settings.tetronimo_assembly_state = 1
					
					# If moving downwards, switch over to the default speed to prevent too 
					# many pieces from falling all at once.
					if self.input_manager.pressed_down:
						self.settings.tetronimo_timer_period = \
							self.settings.tetronimo_timer_period_cache
					
					# Set the blocks to the landed state.
					for block in self.tetronimo_blocks:
						block.change_block_to_landed()
				else:
					self.move_blocks(0, 32)
				
			if not self.marked_for_deletion:
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
		
	def move_blocks(self, delta_x, delta_y):
		"""Change the x or y position by a certain amount."""
		self.position_x += delta_x
		self.position_y += delta_y
		
		# Update the x and y position for the tetronimo blocks that belong to this 
		# tetronimo.
		for block in self.tetronimo_blocks:
			block.position_x += delta_x
			block.position_y += delta_y
			
	def rotate_blocks(self):
		# The current rotations for the tetronimo blocks being rotated.
		rotations = self.rotations[self.rotation_state]
		
		# The block index of the tetronimo block being rotated.
		block_index = 0
		
		# Change the tetronimo block positions.
		for block in self.tetronimo_blocks:
			block.position_x = self.position_x + rotations[block_index][0]
			block.position_y = self.position_y + rotations[block_index][1]
			block_index += 1
			
	def check_tetronimo_block_collisions(self):
		# Checks if a collision has been found.
		found_collision = False
		
		# Check if the tetronimo is intersecting any other 
		# tetronimos.
		for cur_block in self.tetronimo_blocks:
			for key in self.settings.tetronimo_blocks:
				# The other tetronimo block being collided with.
				cur_block_other = self.settings.tetronimo_blocks[key]
				
				if cur_block_other.block_state == 1 and \
					cur_block.position_x >= cur_block_other.position_x - 16 and \
					cur_block.position_x < cur_block_other.position_x + 16 and \
					cur_block.position_y >= cur_block_other.position_y - 16 and \
					cur_block.position_y < cur_block_other.position_y + 16:
					found_collision = True
					break;
			if found_collision:
				break
		return found_collision
		
	def kick_tetronimo_attempt(self, kick_pos_x, kick_pos_y, kick_offset, kick_x, kick_positive):
		"""Checks for tetronimo kicking."""
	
		# Check if the tetronimo can rotate.
		can_rotate = True
		
		# Checks if the tetronimo was kicked.
		kicked = False
		
		# The global kick position x.
		kick_position_global_x = kick_pos_x + self.position_x
		
		# The global kick position y.
		kick_position_global_y = kick_pos_y + self.position_y
		
		# Check if kicking on the x axis or the y axis.
		if kick_x:
			# The position value for the wall boundary.
			wall_value = self.settings.tetronimo_container_bounds[1]
			
			if not kick_positive:
				wall_value = self.settings.tetronimo_container_bounds[0]
			
			# Check if kicking the screen bounds.
			if (not kick_positive and kick_position_global_x < wall_value) or \
				(kick_positive and kick_position_global_x > wall_value):
					
				print("kicked wall!")
				kicked = True
				can_rotate = self.apply_kick(kick_offset, kick_x, kick_positive)
		else:
			# The position value for the wall boundary.
			wall_value = self.settings.tetronimo_container_bounds[3]
			
			if not kick_positive:
				wall_value = self.settings.tetronimo_container_bounds[2]
			
			# Check if kicking the screen bounds.
			if (not kick_positive and kick_position_global_y < wall_value) or \
				(kick_positive and kick_position_global_y > wall_value):
					
				print("kicked wall!")
				kicked = True
				can_rotate = self.apply_kick(kick_offset, kick_x, kick_positive)
					
		# Check if kicking the other blocks.
		if not kicked:
			print("look for blocks..")
			# Iterate through every other tetronimo block and check for collisions with 
			# this tetronimo's blocks.
			for key in self.settings.tetronimo_blocks:
			
				# The other block being collided with.
				cur_block_other = self.settings.tetronimo_blocks[key]
				
				# Only collide with blocks that are in the block_state landed.
				if cur_block_other.block_state == 1:
				
					# Check if the x and y coordinates are the same.
					if kick_position_global_x >= cur_block_other.position_x - 8 and \
						kick_position_global_x < cur_block_other.position_x + 8 and \
						kick_position_global_y >= cur_block_other.position_y - 8 and \
						kick_position_global_y < cur_block_other.position_y + 8:
						
						print("kicked block!")
						kicked = True
						can_rotate = self.apply_kick(kick_offset, kick_x, kick_positive)
						
						if not can_rotate:
							print("rotation failed.")
						
		# If it cannot rotate, then it cannot be kicked either.
		if can_rotate == False:
			kicked = False
					
		return (can_rotate, kicked)

	def apply_kick(self, offset, kick_x, kick_positive):
	
		# Checks if the tetronimo can rotate.
		can_rotate = True
		
		# Kick the blocks.
		if kick_x:
			for block in self.tetronimo_blocks:
				block.position_x += offset
			self.position_x += offset
		else:
			for block in self.tetronimo_blocks:
				block.position_y += offset
			self.position_y += offset
		
		# Check if the tetronimo is intersecting any other 
		# tetronimos after kicking right.
		found_collision = self.check_tetronimo_block_collisions()
			
		# Check if blocks are now outside of the screen bounds.
		if found_collision == False:
				
			if kick_x:
				# Swap the wall values.
				if kick_positive:
					wall_value = self.settings.tetronimo_container_bounds[0]
					
					for block in self.tetronimo_blocks:
						if block.position_x <= wall_value:
							found_collision = True
				else:
					wall_value = self.settings.tetronimo_container_bounds[1]
					
					for block in self.tetronimo_blocks:
						if block.position_x >= wall_value:
							found_collision = True
			else:	
				if kick_positive:
					wall_value = self.settings.tetronimo_container_bounds[2]
					
					for block in self.tetronimo_blocks:
						if block.position_y <= wall_value:
							found_collision = True
				else:
					wall_value = self.settings.tetronimo_container_bounds[3]
					
					for block in self.tetronimo_blocks:
						if block.position_y >= wall_value:
							found_collision = True
			
		# If a collision has been found, then the wall kick has failed. return to
		# The previous block positions.
		if found_collision:
			print("cannot rotate!")
			
			# Kick the blocks back to their previous position.
			if kick_x:
				# Kick every single block that this tetronimo owns.
				for block in self.tetronimo_blocks:
					block.position_x -= offset
				self.position_x -= offset
			else:
				# Kick every single block that this tetronimo owns.
				for block in self.tetronimo_blocks:
					block.position_y -= offset
				self.position_y -= offset
				
			can_rotate = False
				
		return can_rotate
