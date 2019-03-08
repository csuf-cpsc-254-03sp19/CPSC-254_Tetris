import pygame

from pygame.sprite import Sprite

"""The object factory for creating game objects of different types."""
class ObjectFactory():
	def __init__(self, game_objects, pygame_sprites):
		"""Initializes the object factory."""
		
		# The current dynamic game object id. Incremented after every game object is 
		# created.
		self.cur_game_obj_id = 0
		
		# The game objects being created.
		self.game_objects = game_objects
		
		# The pygame sprites being used for creating the game objects.
		self.pygame_sprites = pygame_sprites
		
	def create_test_obj(self, position_x, position_y):
		"""Creates the test object."""
		debug_sprites = {}
		sprite_debug_1 = SpriteImage(0, self.pygame_sprites["debug_1.png"])
		debug_sprites["debug_1.png"] = sprite_debug_1
		
		debug_1_object = GameObject(cur_game_obj_id, 16, 16, None, debug_sprites)
		debug_1_object.cur_sprite_image = sprite_debug_1
		self.game_objects[cur_game_obj_id] = debug_1_object
