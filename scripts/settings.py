import pygame
import random

"""The settings object for the game. It contains all the scoring and high score information, as well as the game state and the tetronimo assembly."""
class Settings():
	def __init__(self):
		"""Initialized the settings."""
		
		# Checks which game state the game is in.
		# 0 - Classic Mode.
		# 1 - Title Screen.
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
		
		# Checks if the tetronimo_timer_cur has been incremented. Used to drive the 
		# vertical movement of the tetronimos and the tetronimo game state.
		self.tetronimo_inc = False
		
		# The rows of tetronimos that are found.
		self.tetronimo_rows = {}
		
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
		
		# Set up the random seed.
		random.seed()
		
	def reset_tetronimo_assembly(self):
		self.tetronimo_timer_period = 1000.0
		self.tetronimo_timer_period_cache = self.tetronimo_timer_period
		self.tetronimo_timer_cur = 0.0
		self.delta_time_accum = 0.0
		self.tetronimo_inc = False
		self.tetronimo_assembly_state = 5
		
	def update(self, delta_time):
		"""Updates the settings and the primary game mechanics."""
		
		# Game state for when the game is playing classic mode.
		if self.game_state == 0:
		
			# Check if the down key is pressed while a piece is falling. If so, speed it 
			# up.
			if self.tetronimo_assembly_state == 0:
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
				
			# Or check if there is a line of tetronimos.
			if self.tetronimo_assembly_state == 1:
				# The row count values.
				row_counts = {}
				row_objs = {}
				# Check for a line of tetronimos.
				for key in self.tetronimo_blocks:
					cur_block = self.tetronimo_blocks[key]
					
					pos_y = cur_block.position_y
					if not pos_y in row_counts:
						row_counts[pos_y] = 0
						row_objs[pos_y] = []
						
					row_counts[pos_y] += 1
					row_objs[pos_y].append(cur_block)
					
				for key in row_counts:
					cur_row_count = row_counts[key]
					if cur_row_count == 10:
						# Add the rows with row count 10 to the list of rows found.
						for key2 in row_counts:
							cur_row_count2 = row_counts[key2]
							if cur_row_count2 == 10:
								self.tetronimo_rows[key2] = row_objs[key2]
						
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
					
					# Destroy all the blocks in each row. Also move down blocks that are 
					# above the row.
					for key in self.tetronimo_rows:
						cur_tetronimo_row = self.tetronimo_rows[key]
						
						for block in cur_tetronimo_row:
							block.marked_for_deletion = True
							
						for key2 in self.tetronimo_blocks:
							cur_block = self.tetronimo_blocks[key2]
							
							if cur_block.position_y <= key:
								cur_block.position_y += 32
								
					self.tetronimo_rows.clear()
					
				else:
					self.delta_time_accum_remove_row += delta_time
					self.delta_time_accum_block_flash += delta_time
					
					# Change the colors of the tetronimo blocks.
					if self.delta_time_accum_block_flash < self.block_flash_period / 2:
						for key in self.tetronimo_rows:
							cur_tetronimo_row = self.tetronimo_rows[key]
							
							for block in cur_tetronimo_row:
								block.change_to_grey_block_sprite()
					elif self.delta_time_accum_block_flash >= self.block_flash_period / 2 and \
							self.delta_time_accum_block_flash < self.block_flash_period:
						for key in self.tetronimo_rows:
							cur_tetronimo_row = self.tetronimo_rows[key]
							
							for block in cur_tetronimo_row:
								block.change_to_primary_block_sprite()
								
					else:
						self.delta_time_accum_block_flash = 0.0
				
			# Game state for when the tetronimo is first being created.
			if self.tetronimo_assembly_state == 5:
			
				# Choose the next tetronimo type randomly.
				self.next_tetronimo_type = random.randint(0, 6)
				
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
				self.object_factory.create_tetronimo_falling(spawn_pos_x, spawn_pos_y, \
						self.next_tetronimo_type)
						
				self.tetronimo_assembly_state = 0
