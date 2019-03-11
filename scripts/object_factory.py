import pygame

from pygame.sprite import Sprite
from sprite_image import SpriteImage
from game_object import GameObject
from text_box import TextBox

"""The object factory for creating game objects of different types."""
class ObjectFactory():
	def __init__(self, game_objects, pygame_sprites, fonts):
		"""Initializes the object factory."""
		
		# The current dynamic game object id. Incremented after every game object is 
		# created.
		self.cur_game_obj_id = 0
		
		# The game objects being created.
		self.game_objects = game_objects
		
		# The pygame sprites being used for creating the game objects.
		self.pygame_sprites = pygame_sprites
		
		# The fonts for the text boxes.
		self.fonts = fonts
		
	def create_test_obj(self, position_x, position_y, obj_type):
		"""Creates the test object."""
		debug_sprites = {}
		
		sprite_name = ""
		
		if obj_type == 0:
			sprite_name = "debug_1.png"
		else:
			sprite_name = "debug_2.png"
		
		sprite_debug_1 = SpriteImage(0, self.pygame_sprites[sprite_name])
		debug_sprites[sprite_name] = sprite_debug_1
			
		debug_1_object = GameObject(self.cur_game_obj_id, position_x, position_y, 
				None, debug_sprites)
				
		debug_1_object.cur_sprite_image = sprite_debug_1
		
		self.game_objects[self.cur_game_obj_id] = debug_1_object
		
		self.cur_game_obj_id += 1
		
	def create_gui_wall(self, position_x, position_y, sprite_name):
		"""Creates the gui wall object."""
		cur_sprites = {}
		
		sprite_1 = SpriteImage(0, self.pygame_sprites[sprite_name])
		cur_sprites[sprite_name] = sprite_1
			
		cur_object = GameObject(self.cur_game_obj_id, position_x, position_y, 
				None, cur_sprites)
				
		cur_object.cur_sprite_image = sprite_1
		
		self.game_objects[self.cur_game_obj_id] = cur_object
		
		self.cur_game_obj_id += 1
		
	def create_text_box(self,position_x, position_y, text, font_name, color, align_bottom_left):
		"""Creates the text box object."""
			
		# The current font being used.
		cur_font = self.fonts[font_name]
		
		# The text box being created.
		cur_object = TextBox(self.cur_game_obj_id, position_x, position_y, text, \
				cur_font, color, align_bottom_left, None, None)
		
		self.game_objects[self.cur_game_obj_id] = cur_object
		
		self.cur_game_obj_id += 1
