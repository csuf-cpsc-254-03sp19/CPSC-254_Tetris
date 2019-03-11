import pygame

from game_object import GameObject
from input_manager import InputManager
from sprite_image import SpriteImage
from object_factory import ObjectFactory

"""The primary game system that is the skeleton of the entire game. It contains the setup functions as well as the main game loop and collision detection functions."""
class GameSystem:
	def __init__(self):
		"""Initialized the game system."""
		print("Hello world!")
		
		# Checks if the game is currently active.
		self.is_active = True
		
		# The pygame clock for limiting the framerate.
		self.pygame_clock = None
		
		# The backbuffer being rendered to.
		self.backbuffer = None
		
		# The input manager for managing keyboard and mouse input.
		self.input_manager = InputManager(self)
		
		# The game object factory for creating the game objects.
		self.object_factory = None
		
		# The game objects for the game. Keys are the game object ids.
		self.game_objects = {}
		
		# The pygame sprite images.
		self.pygame_sprites = {}
		
		# Create the game object factory.
		self.object_factory = ObjectFactory(self.game_objects, self.pygame_sprites)
		
	def start_program(self):
		"""Starts off the program, initializing pygame and loading all the
		sprites, sounds and fonts."""
		print("The game has just begun.")
		
		self.setup_pygame()
		self.load_sprites()
		self.setup_classic_game()
		self.main_loop()
		
	def load_sprites(self):
		# The image folder url.
		image_folder_url = "../images/"
		
		# The current sprite image being loaded. Not to be confused with the sprite 
		# image class.
		self.load_sprite(image_folder_url, "debug_1.png")
		self.load_sprite(image_folder_url, "debug_2.png")
		self.load_sprite(image_folder_url, "wall_in_up.png")
		self.load_sprite(image_folder_url, "wall_in_down.png")
		self.load_sprite(image_folder_url, "wall_in_left.png")
		self.load_sprite(image_folder_url, "wall_in_right.png")
		self.load_sprite(image_folder_url, "wall_in_upright.png")
		self.load_sprite(image_folder_url, "wall_in_downright.png")
		self.load_sprite(image_folder_url, "wall_in_downleft.png")
		self.load_sprite(image_folder_url, "wall_in_upleft.png")
		self.load_sprite(image_folder_url, "wall_in_center.png")
		self.load_sprite(image_folder_url, "wall_in_hor.png")
		self.load_sprite(image_folder_url, "wall_in_leftT.png")
		self.load_sprite(image_folder_url, "wall_in_rightT.png")
		self.load_sprite(image_folder_url, "wall_out_center.png")
		
	def load_sprite(self, image_folder_url, cur_sprite_image_name):
		self.pygame_sprites[cur_sprite_image_name] = pygame.image.load( \
			image_folder_url + cur_sprite_image_name)
		print(image_folder_url)
	
	def setup_pygame(self):
		"""Sets up the pygame module."""
		
		# Create the pygame module.
		pygame.init()

		# Get the pygame clock.
		self.pygame_clock = pygame.time.Clock()

		# The backbuffer of the game.
		self.backbuffer = pygame.display.set_mode((640, 800))

		# Set the caption for the game window.
		pygame.display.set_caption("Tetris")
		
	def setup_classic_game(self):
		self.load_map_gameplay()
		
	def load_map_gameplay(self):
		with open("map_gameplay.txt", "r") as in_file:
			# The text containing all the characters for the map objects.
			map_text = in_file.read()
				
			# The current x position of the current map object being read from or the a star node.
			cur_position_x = 8

			# The current y position of the current map object being read from or the a star node.
			cur_position_y = 8
			
			 # Go through every character and create the correct map object from it.
			for char in map_text:
				if not char == '\n':

					# The current background tile being produced.
					background_tile1 = None

					# Choose a different sprite based on the character.
					if char == 'C':
						self.object_factory.create_gui_wall(cur_position_x, cur_position_y, "wall_in_center.png")
					elif char == 'c' or char == ' ':
						self.object_factory.create_gui_wall(cur_position_x, cur_position_y, "wall_out_center.png")
					elif char == 'U':
						self.object_factory.create_gui_wall(cur_position_x, cur_position_y, "wall_in_up.png")
					elif char == 'D':
						self.object_factory.create_gui_wall(cur_position_x, cur_position_y, "wall_in_down.png")
					elif char == 'L':
						self.object_factory.create_gui_wall(cur_position_x, cur_position_y, "wall_in_left.png")
					elif char == 'R':
						self.object_factory.create_gui_wall(cur_position_x, cur_position_y, "wall_in_right.png")
					elif char == 'H':
						self.object_factory.create_gui_wall(cur_position_x, cur_position_y, "wall_in_hor.png")
					elif char == '/':
						self.object_factory.create_gui_wall(cur_position_x, cur_position_y, "wall_in_upleft.png")
					elif char == '\\':
						self.object_factory.create_gui_wall(cur_position_x, cur_position_y, "wall_in_upright.png")
					elif char == '[':
						self.object_factory.create_gui_wall(cur_position_x, cur_position_y, "wall_in_downleft.png")
					elif char == ']':
						self.object_factory.create_gui_wall(cur_position_x, cur_position_y, "wall_in_downright.png")
					elif char == 'T':
						self.object_factory.create_gui_wall(cur_position_x, cur_position_y, "wall_in_leftT.png")
					elif char == 't':
						self.object_factory.create_gui_wall(cur_position_x, cur_position_y, "wall_in_rightT.png")
						
					cur_position_x += 16

					if cur_position_x >= (40 * 16) + 8:
						cur_position_x = 8
						cur_position_y += 16
			
		
	def main_loop(self):
		# The entrance to the main loop. The game will continue to loop until 
		# is_active is set to false.
		while self.is_active:
			# Manage the frame rate to 60 fps.
			self.pygame_clock.tick(60)

			# Check the keyboard input events.
			self.input_manager.check_events()
			
			# If the q key is pressed, exit the game.
			if self.input_manager.pressed_q:
				self.is_active = False
			else:
				self.collision_detection()
				self.render_objects()
				
		self.clean_up()
			
	def collision_detection(self):
		print("Collision detection.")
		
	def render_objects(self):
		"""Render all the game objects to the screen."""
		# Fill the background with the color black.
		self.backbuffer.fill((0, 0, 0))
		
		# Render every object in the group. Render every object by layer from 0 to 3.
		for x in range (0, 3):
			for key in self.game_objects:
				# The current game object being rendered.
				cur_game_obj = self.game_objects[key]
				
				# The current sprite of the game object being rendered.
				cur_sprite_image = cur_game_obj.cur_sprite_image
				
				# If there is no image, don't render it.
				if cur_sprite_image is not None and \
					cur_sprite_image.image_layer == x and \
					cur_sprite_image.image is not None and \
					cur_sprite_image.image_rect is not None:
					
					# Update the object rect for the rendering process.
					cur_sprite_image.update_image_rect(cur_game_obj.position_x, 
							cur_game_obj.position_y)

					# The current image being rendered.
					cur_image = cur_sprite_image.image

					# The rect of the current image being rendered.
					cur_rect = cur_sprite_image.image_rect

					# Blit the sprite to the backbuffer.
					self.backbuffer.blit(cur_image, cur_rect)
				
		# Swap the backbuffer.
		pygame.display.flip()
	
	@staticmethod
	def clean_up():
		# Exit pygame.
		pygame.quit()

