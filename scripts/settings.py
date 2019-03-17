import pygame

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
		
		# The period at which the tetronimo timer accumulates frames. In milliseconds.
		self.tetronimo_timer_period = 1000.0
		
		# The time accumulated, in milliseconds. When filled up larger than or equal to 
		# tetronimo_timer_period, the tetronimo_timer_cur will increment and this will be 
		# reset to 0.0.
		self.delta_time_accum = 0.0
		
		# The bounds of the tetronimo container. x, y, width, height.
		self.tetronimo_container_bounds = (160, 480, 16, 720)
		
		# The spawn position of the O tetronimo.
		self.tetronimo_spawn_pos_O = (320, 48)
		
		# The spawn position of the I tetronimo.
		self.tetronimo_spawn_pos_I = (320, 32)
		
		# The spawn position of the rest of the tetronimos.
		self.tetronimo_spawn_pos_D = (304, 64)
		
		# Checks if the tetronimo_timer_cur has been incremented. Used to drive the 
		# vertical movement of the tetronimos and the tetronimo game state.
		self.tetronimo_inc = False
		
		# A reference to the tetronimos falling.
		self.tetronimos_falling = None
		
		# A reference to the game objects.
		self.game_objects = None
		
		# A reference to the object factory.
		self.object_factory = None
		
	def reset_tetronimo_assembly(self):
		self.tetronimo_timer_period = 1000.0
		self.tetronimo_timer_cur = 0.0
		self.delta_time_accum = 0.0
		self.tetronimo_inc = False
		self.tetronimo_assembly_state = 5
		
	def update(self, delta_time):
		"""Updates the settings and the primary game mechanics."""
		
		if self.game_state == 0:
			self.delta_time_accum += delta_time
			
			self.tetronimo_inc = False
			
			while self.delta_time_accum >= self.tetronimo_timer_period:
				self.delta_time_accum -= self.tetronimo_timer_period
				self.tetronimo_inc = True
				
				if self.tetronimo_assembly_state == 0:
					for key in self.tetronimos_falling:
						cur_tetronimos_falling = self.tetronimos_falling[key]
						cur_tetronimos_falling.drive()
				
			if self.tetronimo_assembly_state == 5:
				spawn_pos_x = self.tetronimo_spawn_pos_O[0]
				spawn_pos_y = self.tetronimo_spawn_pos_O[1]
				
				self.object_factory.create_tetronimo_falling(spawn_pos_x, spawn_pos_y, 0)
				self.tetronimo_assembly_state = 0
