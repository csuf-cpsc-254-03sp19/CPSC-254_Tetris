import pygame
import random

"""The settings object for the game. It contains all the scoring and high score information, as well as the game state and the tetronimo assembly."""
class Settings():
	def __init__(self):
		"""Initialized the settings."""
		
		# Checks which game state the game is in.
		# 0 - Classic Mode.
		# 1 - Title Screen.
		# 2 - Game Over Screen.
		self.game_state = 0
		
		# The tetronimo assembly state for managing how tetronimos are being created.
		# 0 - Tetronimo is falling.
		# 1 - Tetronimo has fallen.
		# 2 - Line of tetronimos found.
		# 3 - Move tetronimos down from line of tetronimos.
		# 4 - Filled up screen.
		# 5 - Creating tetronimo.
		self.tetronimo_assembly_state = 5
		
		# This timer accumulates once
		self.tetronimo_timer_cur = 0
		
		# The type of the next tetronimo being created.
		self.next_tetronimo_type = 0
		
		# The total number of rows cleared.
		self.rows_cleared = 0
		
		# The period at which the tetronimo timer accumulates frames. In milliseconds.
		self.tetronimo_timer_period = 1000.0
		
		# The minimum period for the tetronimo to fall.
		self.tetronimo_timer_min_period = 50.0
		
		# The period at which the row of tetronimos is removed.
		self.remove_row_timer_period = 1000.0
		
		# The period at which the blocks flash.
		self.block_flash_period = 200.0
		
		# The cache for the tetronimo time period.
		self.tetronimo_timer_period_cache = self.tetronimo_timer_period
		
		# The time accumulated, in milliseconds. When filled up larger than or equal to 
		# tetronimo_timer_period, the tetronimo_timer_cur will increment and this will be 
		# reset to 0.0.
		self.delta_time_accum = 0.0
		
		# The delta time accumulated for removing a single row.
		self.delta_time_accum_remove_row = 0.0
		
		# The delta time accumulated for the block flash.
		self.delta_time_accum_block_flash = 0.0
		
		# The bounds of the tetronimo container. left, right, top, bottom.
		self.tetronimo_container_bounds = (160, 480, 16, 784)
		
		# The spawn position of the O tetronimo.
		self.tetronimo_spawn_pos_O = (320, 48)
		
		# The spawn position of the I tetronimo.
		self.tetronimo_spawn_pos_I = (320, 32)
		
		# The spawn position of the rest of the tetronimos.
		self.tetronimo_spawn_pos_D = (304, 64)
		
		# The position to fill a row of grey blocks once the player loses.
		self.block_fill_pos_y = self.tetronimo_container_bounds[3]
		
		# Checks if the tetronimo_timer_cur has been incremented. Used to drive the 
		# vertical movement of the tetronimos and the tetronimo game state.
		self.tetronimo_inc = False
		
		# The rows of tetronimos that are found.
		self.tetronimo_rows = {}
		
		# The queue of randomly generated tetronimo types used for tetronimo assembly. A 
		# new tetronimo type is added to it at the 5th assembly state and the oldest one 
		# is removed.
		self.tetronimo_type_queue = []
		
		# A list of references to the tetronimo displays.
		self.tetronimo_displays = []
		
		# The saved tetronimo that the player saved.
		self.cached_tetronimo_falling = None
		
		# The current tetronimo that is falling.
		self.cur_tetronimo_falling = None
		
		# A reference to the tetronimos falling.
		self.tetronimos_falling = None
		
		# A reference to the tetronimo blocks.
		self.tetronimo_blocks = None
		
		# A reference to the game objects.
		self.game_objects = None
		
		# A reference to the object factory.
		self.object_factory = None
		
		# The input manager for checking the user input.
		self.input_manager = None
		
		# A reference to the game system.
		self.game_system = None
		
		#text box score
		self.text_box_score = None
		
		#text box highscore
		self.text_box_highscore = None

		# Set up the random seed.
		random.seed()

		# The score for each line clear 
		self.score = 0
		
		
		#Highscore 
		highscore = 0
		
		#open high_score txt file and read in file 
		highscore = open("high_score.txt", "r+")
		highscore = highscore.read(1)
		#if file is emppty where there no highscore 

		if not highscore:
			# Then write 0 in high_score.txt file 
			whighscore= open("high_score.txt", "w+")
			whighscore.write(str(0))
			whighscore.close()

		#read high_score.txt 
		highscore = open("high_score.txt", "r+")
		highscore = highscore.read()

		# if score is greater than highscore then output the score to the txt file 
		if int(self.score) > int(highscore):
			writehighscore= open("high_score.txt", "w+")
			writehighscore.write(str(self.score))
	
		
	def reset_tetronimo_assembly(self):
		"""Resets the tetronimo assembly. Must be called after every game start."""
		self.tetronimo_timer_period = 1000.0
		self.tetronimo_timer_period_cache = self.tetronimo_timer_period
		self.tetronimo_timer_cur = 0.0
		self.delta_time_accum = 0.0
		self.delta_time_accum_remove_row = 0.0
		self.delta_time_accum_block_flash = 0.0
		self.tetronimo_inc = False
		self.tetronimo_assembly_state = 5
		self.block_fill_pos_y = self.tetronimo_container_bounds[3]
		self.tetronimo_rows.clear()
		
		# Add 3 random tetronimos.
		self.tetronimo_type_queue.append(self.rand_tetronimo_type())
		self.tetronimo_type_queue.append(self.rand_tetronimo_type())
		self.tetronimo_type_queue.append(self.rand_tetronimo_type())
		self.tetronimo_type_queue.append(self.rand_tetronimo_type())
		
		# Set the image type of the last tetronimo display to none.
		self.tetronimo_displays[len(self.tetronimo_displays) - 1].image_type = 7
		
	def rand_tetronimo_type(self):
		"""Generates a random number for the tetronimo type."""
		# The random number being generated.
		random_number = random.randint(0, 6)
		return random_number
		
	def update_tetronimo_type_queue(self):
		"""Updates the tetronimo type queue by adding a new tetronimo type and deleting the old one."""
		self.tetronimo_type_queue.append(self.rand_tetronimo_type())
		self.tetronimo_type_queue.pop(0)
		
		# Update the tetronimo displays with the new tetronimos in the tetronimo queue.
		for x in range(0, 4):
			# The index for the tetronimo display.
			index = 4 - (x + 1)
			
			# The current tetronimo type.
			cur_tetronimo_type = self.tetronimo_type_queue[x]
			
			# The current tetronimo display.
			cur_tetronimo_display = self.tetronimo_displays[x]
			
			cur_tetronimo_display.image_type = cur_tetronimo_type
	
	
		
	def update(self, delta_time):
		"""Updates the settings and the primary game mechanics."""
		
		if self.text_box_score is not None:
			self.text_box_score.set_text(str(self.score))

		if self.text_box_highscore is not None:
			
			#read in highscore from high_score.txt file
			highscore = open("high_score.txt", "r+")
			highscore = highscore.read()
			if int(self.score) > int(highscore):
				self.text_box_highscore.set_text(str(self.score))
				writehighscore= open("high_score.txt", "w+")
				writehighscore.write(str(self.score))
			if int(self.score) <= int(highscore):
				self.text_box_highscore.set_text(str(highscore))

		# Game state for when the game is playing classic mode.
		if self.game_state == 0:
		
			# Key input processing.
			if self.tetronimo_assembly_state == 0:
				# Check if the down key is pressed while a piece is falling. If so, speed it 
				# up.
				if not self.tetronimo_timer_period == self.tetronimo_timer_min_period:
					# Check if the down key is pressed.
					if self.input_manager.pressed_down:
						# If auto landing, do not allow the piece to speed up.
						if not self.input_manager.pressed_x:
							self.tetronimo_timer_period_cache = \
								self.tetronimo_timer_period
							self.tetronimo_timer_period = \
								self.tetronimo_timer_min_period
							self.tetronimo_timer_cur = 0.0
							self.delta_time_accum = 0.0
						else:
							self.tetronimo_timer_period = \
								self.tetronimo_timer_period_cache
				else:
					if not self.input_manager.pressed_down:
						self.tetronimo_timer_period = self.tetronimo_timer_period_cache
						
				# Check if the c key is tapped so that the player can save or swap a falling 
				# tetronimo.
				if self.input_manager.tapped_c:
					
					# If there is no cached tetronimo, then cache one.
					if self.cached_tetronimo_falling is None:
						# Deactivate the current tetronimo falling.
						self.cur_tetronimo_falling.is_active = False
						
						# Also deactivate the blocks of the tetronimo falling.
						for block in self.cur_tetronimo_falling.tetronimo_blocks:
							block.is_active = False
						
						self.cached_tetronimo_falling = self.cur_tetronimo_falling
						self.tetronimo_assembly_state = 5
						
						# Update the tetronimo display for the saved tetronimo.
						self.tetronimo_displays[len(self.tetronimo_displays) - 1]. \
							image_type = self.cur_tetronimo_falling.tetronimo_type
					else:		
						# Tetronimos may differ in their central coordinate depending 
						# on their tetronimo type, so choose the correct offsets for 
						# assigning the position of the cached tetronimo.
						
						# The type of the cached tetronimo.
						type_cache = self.cached_tetronimo_falling.tetronimo_type
						
						# The type of the current tetronimo.
						type_cur = self.cur_tetronimo_falling.tetronimo_type
						
						# The type cache type. Types are 'D' for L, J, S, Z, and T,
						# 'O' for O, and 'I' for I. They all have a different 
						# coordinate.
						type_cache_type = 'D'
						type_cur_type = 'D'
						
						if type_cache == 0:
							type_cache_type = 'O'
						elif type_cache == 1:
							type_cache_type = 'I'
							
						if type_cur == 0:
							type_cur_type = 'O'
						elif type_cur == 1:
							type_cur_type = 'I'
							
						# The extra offset for the x coordinate when switching between 
						# tetronimo type types.
						extra_offset_x = 0
						
						# The extra offset for the y coordinate when switching between 
						# tetronimo type types.
						extra_offset_y = 0
							
						# Choose the correct offset types based on the tetronimo type 
						# types.
						if type_cache_type == 'O' and type_cur_type == 'D':
							extra_offset_x = -16
							extra_offset_y = -16
						elif type_cache_type == 'D' and type_cur_type == 'O':
							extra_offset_x = 16
							extra_offset_y = 16
						elif type_cache_type == 'I' and type_cur_type == 'D':
							extra_offset_x = -16
							extra_offset_y = -32
						elif type_cache_type == 'D' and type_cur_type == 'I':
							extra_offset_x = 16
							extra_offset_y = 32
						elif type_cache_type == 'O' and type_cur_type == 'I':
							extra_offset_y = 16
						elif type_cache_type == 'I' and type_cur_type == 'O':
							extra_offset_y = -16
							
						# Update the position of the tetronimo blocks of the cached 
						# tetronimo falling.
						for cur_block in self.cached_tetronimo_falling.tetronimo_blocks:
								
							cur_block.position_x += \
									self.cur_tetronimo_falling.position_x - \
									self.cached_tetronimo_falling.position_x + \
									extra_offset_x
							cur_block.position_y += \
									self.cur_tetronimo_falling.position_y - \
									self.cached_tetronimo_falling.position_y + \
									extra_offset_y
							
						# Also update the position of the cached tetronimo.
						self.cached_tetronimo_falling.position_x = \
								self.cur_tetronimo_falling.position_x + extra_offset_x
								
						self.cached_tetronimo_falling.position_y = \
								self.cur_tetronimo_falling.position_y + extra_offset_y
								
						# Check if the tetronimo is colliding with any other tetronimos 
						# before swapping.
						
						# Checks if a collision with a block occured.
						collision_occured = False
						
						for cur_block in self.cached_tetronimo_falling.tetronimo_blocks:
							for key in self.tetronimo_blocks:
							
								# The current tetronimo block being tested for collision.
								cur_block_other = self.tetronimo_blocks[key]
								
								if cur_block_other.block_state == 1:
									if cur_block.position_x == \
											cur_block_other.position_x and \
										cur_block.position_y == \
											cur_block_other.position_y:
										collision_occured = True
										break
										
							if collision_occured:
								break
								
							# Also check if the new piece is colliding with the walls
							if cur_block.position_x <= \
									self.tetronimo_container_bounds[0] or \
									cur_block.position_x >= \
									self.tetronimo_container_bounds[1] or \
									cur_block.position_y >= \
									self.tetronimo_container_bounds[3]:
								collision_occured = True
								break
								
						if not collision_occured:
							# Deactivate the current tetronimo falling.
							self.cur_tetronimo_falling.is_active = False
							for block in self.cur_tetronimo_falling.tetronimo_blocks:
								block.is_active = False
						
							# Activate the cached tetronimo falling.
							self.cached_tetronimo_falling.is_active = True
							for block in self.cached_tetronimo_falling.tetronimo_blocks:
								block.is_active = True
								
							# Swap the cached tetronimo and the current tetronimo falling.
							temp = self.cached_tetronimo_falling
							self.cached_tetronimo_falling = self.cur_tetronimo_falling
							self.cur_tetronimo_falling = temp
							
							# Update the tetronimo display for the saved tetronimo.
							self.tetronimo_displays[len(self.tetronimo_displays) - 1]. \
								image_type = self.cached_tetronimo_falling.tetronimo_type
						
			self.delta_time_accum += delta_time
			
			self.tetronimo_inc = False
			
			# Update the tetronimo after the general time period has elapsed.
			while self.delta_time_accum >= self.tetronimo_timer_period:
				self.delta_time_accum -= self.tetronimo_timer_period
				self.tetronimo_inc = True
						
				# If in assembly state has fallen, create a new tetronimo.
				if self.tetronimo_assembly_state == 1 or \
						self.tetronimo_assembly_state == 3:
					self.tetronimo_assembly_state = 5
				
			# Or check if there is a line of tetronimos. Also check if there are 
			# tetronimos on top of the screen.
			if self.tetronimo_assembly_state == 1:
				# Check if there are any blocks at the top of the screen.
				for key in self.tetronimo_blocks:
					cur_block = self.tetronimo_blocks[key]
					
					if cur_block.is_active and cur_block.block_state == 1 and \
							cur_block.position_y == 64:
						self.tetronimo_assembly_state = 4
						self.change_all_blocks_to_grey()
						break
						
				# The row count values.
				row_counts = {}
				
				# The row tetronimo objects.
				row_objs = {}
				
				# Check for a line of tetronimos.
				for key in self.tetronimo_blocks:
					# The current tetronimo block being checked for being in a row.
					cur_block = self.tetronimo_blocks[key]
					
					# Only check the block if it is active and is in the block state 1.
					if cur_block.is_active and cur_block.block_state == 1:
					
						# The y position of the current block.
						pos_y = cur_block.position_y
						
						# Create the row array and count if it isn't created already for 
						# this row.
						if not pos_y in row_counts:
							row_counts[pos_y] = 0
							row_objs[pos_y] = []
							
						# Increment the number of blocks in the row and add the block to 
						# the row block list that it belongs to.
						row_counts[pos_y] += 1
						row_objs[pos_y].append(cur_block)
			
				# Find the rows that have 10 blocks in them.
				for key in row_counts:
					# The current row cound that was found.
					cur_row_count = row_counts[key]
			
					# If the row count is 10, then we found a row with 10 blocks.
					if cur_row_count == 10:
						#self.score += 40
						#print(self.score)
						# Add the rows with row count 10 to the list of rows found.
						for key2 in row_counts:	
												
							# The current row count for the secondary row count.
							cur_row_count2 = row_counts[key2]
	
							# If the row has 10 blocks, then add the row object to the 
							# tetronimo rows list.
							if cur_row_count2 == 10:
								self.tetronimo_rows[key2] = row_objs[key2]

								self.score += 40
								
						self.tetronimo_assembly_state = 2
				
						
						
						
						break
						
						
			# The state for destroying the rows of tetronimo blocks.
			if self.tetronimo_assembly_state == 2:
				# Once the timer is finished, destroy the row of blocks.
				if self.delta_time_accum_remove_row >= self.remove_row_timer_period:
					self.tetronimo_assembly_state = 3
					self.delta_time_accum = 0.0
					self.delta_time_accum_remove_row = 0.0
					self.delta_time_accum_block_flash = 0.0
					
					# The sorted list of keys in ascending order.
					key_list_sorted = []
					
					# First, sort all the row y value keys in ascending order.
					for key in self.tetronimo_rows:
						key_list_sorted.append(key)
						
					key_list_sorted.sort()
					
					# Destroy all the blocks in each row. Also move down blocks that are 
					# above the row.
					for key in key_list_sorted:
					
						# The current tetronimo row.
						cur_tetronimo_row = self.tetronimo_rows[key]
						
						# Go through every block and mark it for deletion.
						for block in cur_tetronimo_row:
							block.marked_for_deletion = True
					
							
						# Also increment the y value of the blocks above the row of blocks 
						# being deleted.
						for key2 in self.tetronimo_blocks:
							# The current block being incremented.
							cur_block = self.tetronimo_blocks[key2]
							
							# Only increment the block if it is active and has a block 
							# state of 1.
							if cur_block.is_active and cur_block.block_state == 1:
								# If the block has a y value that is less than or equal to the 
								# row y value, then increment the y value of the current 
								# block.
								if cur_block.position_y <= key:
									cur_block.position_y += 32
									
						self.rows_cleared += 1
						self.clear_row = self.rows_cleared 
						
						self.clear_row += 0
						print(self.clear_row)
						
						self.clear_row = 0
						# For every 4 rows cleared, decrease the tetronimo timer period by 
						# 10 to increase the difficulty.
						if self.tetronimo_timer_period > 50.0 and \
								self.rows_cleared % 4 == 0:
							self.tetronimo_timer_period -= 50.0
								
					self.tetronimo_rows.clear()
					
				else:
					self.delta_time_accum_remove_row += delta_time
					self.delta_time_accum_block_flash += delta_time
					
					# Change the colors of the tetronimo blocks.
					if self.delta_time_accum_block_flash < self.block_flash_period / 2:
						for key in self.tetronimo_rows:
							
							# The current tetronimo row having its colors updated.
							cur_tetronimo_row = self.tetronimo_rows[key]
							
							for block in cur_tetronimo_row:
								block.change_to_grey_block_sprite()
					elif self.delta_time_accum_block_flash >= self.block_flash_period / 2 and \
							self.delta_time_accum_block_flash < self.block_flash_period:
						for key in self.tetronimo_rows:
						
							# The current tetronimo row having its colors updated.
							cur_tetronimo_row = self.tetronimo_rows[key]
							
							for block in cur_tetronimo_row:
								block.change_to_primary_block_sprite()
								
					else:
						self.delta_time_accum_block_flash = 0.0
				
			# Check if filling the screen with blocks after the player loses.
			if self.tetronimo_assembly_state == 4:
				# If the screen isn't already filled with blocks, fill it with blocks.
				if self.block_fill_pos_y >= 32:
					# Add 10 blocks to a single row two times.
					self.create_row_of_grey_blocks()
					self.create_row_of_grey_blocks()
					
				# After a certain amount of time, switch to the game over game state and 
				# load the game over map.
				elif self.block_fill_pos_y < -1024:
					self.game_state = 2
					self.game_system.load_map_game_over()
				else:
					self.block_fill_pos_y -= 32
				
			# Game state for when the tetronimo is first being created.
			if self.tetronimo_assembly_state == 5:
			
				self.next_tetronimo_type = self.tetronimo_type_queue[0]
						
				# Choose the next tetronimo type randomly.
				self.update_tetronimo_type_queue()
				
				# The tetronimo spawn position.
				spawn_pos_x = self.tetronimo_spawn_pos_D[0]
				spawn_pos_y = self.tetronimo_spawn_pos_D[1]
				
				if self.next_tetronimo_type == 0:
					spawn_pos_x = self.tetronimo_spawn_pos_O[0]
					spawn_pos_y = self.tetronimo_spawn_pos_O[1]
				elif self.next_tetronimo_type == 1:
					spawn_pos_x = self.tetronimo_spawn_pos_I[0]
					spawn_pos_y = self.tetronimo_spawn_pos_I[1]
				
				# Create the initial tetronimo.
				self.cur_tetronimo_falling = \
						self.object_factory.create_tetronimo_falling( \
						spawn_pos_x, spawn_pos_y, self.next_tetronimo_type)
						
				self.tetronimo_assembly_state = 0
				
		# The game over screen processing.
		elif self.game_state == 2:
			print("Game over!")

		
	
	def change_all_blocks_to_grey(self):
		"""Changes all the blocks to grey. Also removes any blocks past the tetronimo container bounds."""
		for key in self.tetronimo_blocks:
		
			# The current block being turned grey.
			cur_block = self.tetronimo_blocks[key]
			
			# Also mark the block for deletion if it is below the threshold of the 
			# tetronimo container bounds.
			if cur_block.position_y < self.tetronimo_container_bounds[2]:
				cur_block.marked_for_deletion = True
			else:
				cur_block.change_to_grey_block_sprite()
			
	def create_row_of_grey_blocks(self):
		"""Creates a row of grey blocks."""
		for x in range(0, 10):
			# Create a single tetronimo block that starts off grey.
			self.object_factory.create_tetronimo_block(
				x * 32 + 16 + self.tetronimo_container_bounds[0], \
				self.block_fill_pos_y - self.tetronimo_container_bounds[2], \
				7, None)
		self.block_fill_pos_y -= 32
