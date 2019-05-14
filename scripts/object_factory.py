import pygame

from pygame.sprite import Sprite
from sprite_image import SpriteImage
from game_object import GameObject
from text_box import TextBox
from tetronimo_falling import TetronimoFalling
from tetronimo_block import TetronimoBlock
from tetronimo_display import TetronimoDisplay

""" ---------------------------------------------------------------
    ObjectFactory Class
    
    The object factory for creating game objects of different types.
--------------------------------------------------------------- """
class ObjectFactory():
	def __init__(self, game_objects, pygame_sprites, fonts):
		#initialize with the necessary objects and sprites
		self.cur_game_obj_id = 0		
		self.game_objects = game_objects		
		self.pygame_sprites = pygame_sprites		
		self.fonts = fonts
		self.settings = None	
		self.input_manager = None
		
	def create_test_obj(self, position_x, position_y, obj_type):
		#this function creates the test object
		debug_sprites = {}
		sprite_name = ""
		
		if obj_type == 0:
			sprite_name = "debug_1.png"
		else:
			sprite_name = "debug_2.png"
		
		sprite_debug_1 = SpriteImage(0, self.pygame_sprites[sprite_name])
		debug_sprites[sprite_name] = sprite_debug_1
		debug_1_object = GameObject(self.cur_game_obj_id, 0, position_x, position_y, 
				None, debug_sprites)
		debug_1_object.cur_sprite_image = sprite_debug_1
		
		self.game_objects[self.cur_game_obj_id] = debug_1_object
		self.cur_game_obj_id += 1
		
		return cur_object
		
	def create_gui_wall(self, position_x, position_y, sprite_name):
		#this function creates the gui wall object
		cur_sprites = {}
		
		sprite_1 = SpriteImage(0, self.pygame_sprites[sprite_name])
		cur_sprites[sprite_name] = sprite_1
			
		cur_object = GameObject(self.cur_game_obj_id, 1, position_x, position_y, 
				None, cur_sprites)		
		cur_object.cur_sprite_image = sprite_1
		
		self.game_objects[self.cur_game_obj_id] = cur_object
		self.cur_game_obj_id += 1
		
		return cur_object
		
	def create_text_box(self, position_x, position_y, text, font_name, color, \
			align_bottom_left):
		#this function creates the text box object
		#assign the current font being used
		#assign the text box being created
		cur_font = self.fonts[font_name]
		cur_object = TextBox(self.cur_game_obj_id, 2, position_x, position_y, text, \
				cur_font, color, align_bottom_left, None, None)
		
		self.game_objects[self.cur_game_obj_id] = cur_object
		self.cur_game_obj_id += 1
		
		return cur_object
		
	def create_tetronimo_falling(self, position_x, position_y, tetronimo_type):
		#This function will create the teteronimo falling
		#Assign the teteronimo falling to be created
		cur_object = TetronimoFalling(self.cur_game_obj_id, 3, position_x, position_y, \
				tetronimo_type, self, self.settings, self.input_manager, None, None)

		self.game_objects[self.cur_game_obj_id] = cur_object
		self.cur_game_obj_id += 1
		
		return cur_object
		
	def create_tetronimo_block(self, position_x, position_y, tetronimo_type, owner):
		"""
		This function creates the teteronimo falling.
		Assign the sprites for the teteronimo block.
		Assign the name of the current sprite being gathered.
		Assign the current sprites to be gathered.
		Assign the teteronimo falling to be created.
		"""
		sprites = {}
		sprite_name = "block_yellow.png"
		
		cur_sprite = SpriteImage(0, self.pygame_sprites[sprite_name])
		sprites[sprite_name] = cur_sprite
		
		sprite_name = "block_skyblue.png"
		cur_sprite = SpriteImage(0, self.pygame_sprites[sprite_name])
		sprites[sprite_name] = cur_sprite
		
		sprite_name = "block_orange.png"
		cur_sprite = SpriteImage(0, self.pygame_sprites[sprite_name])
		sprites[sprite_name] = cur_sprite
		
		sprite_name = "block_blue.png"
		cur_sprite = SpriteImage(0, self.pygame_sprites[sprite_name])
		sprites[sprite_name] = cur_sprite
		
		sprite_name = "block_green.png"
		cur_sprite = SpriteImage(0, self.pygame_sprites[sprite_name])
		sprites[sprite_name] = cur_sprite
		
		sprite_name = "block_red.png"
		cur_sprite = SpriteImage(0, self.pygame_sprites[sprite_name])
		sprites[sprite_name] = cur_sprite
		
		sprite_name = "block_purple.png"
		cur_sprite = SpriteImage(0, self.pygame_sprites[sprite_name])
		sprites[sprite_name] = cur_sprite
		
		sprite_name = "block_grey.png"
		cur_sprite = SpriteImage(0, self.pygame_sprites[sprite_name])
		sprites[sprite_name] = cur_sprite
		
		cur_object = TetronimoBlock(self.cur_game_obj_id, 4, position_x, position_y, \
				tetronimo_type, owner, self.settings, None, sprites)
		self.game_objects[self.cur_game_obj_id] = cur_object		
		self.cur_game_obj_id += 1
		
		return cur_object

	def create_tetronimo_display(self, position_x, position_y):
		"""
		This functions creates the teteronimo display.
		Assign the sprites for the teteronimo block.
		Assign the name of the current sprite being gathered.
		Assign the current sprites being gathered
		Assign the teteroimo displaybeing created.
		"""
		sprites = {}
		sprite_name = "display_none.png"
		
		cur_sprite = SpriteImage(0, self.pygame_sprites[sprite_name])
		sprites[sprite_name] = cur_sprite
		
		sprite_name = "display_O.png"
		cur_sprite = SpriteImage(0, self.pygame_sprites[sprite_name])
		sprites[sprite_name] = cur_sprite
		
		sprite_name = "display_I.png"
		cur_sprite = SpriteImage(0, self.pygame_sprites[sprite_name])
		sprites[sprite_name] = cur_sprite
		
		sprite_name = "display_J.png"
		cur_sprite = SpriteImage(0, self.pygame_sprites[sprite_name])
		sprites[sprite_name] = cur_sprite
		
		sprite_name = "display_L.png"
		cur_sprite = SpriteImage(0, self.pygame_sprites[sprite_name])
		sprites[sprite_name] = cur_sprite
		
		sprite_name = "display_S.png"
		cur_sprite = SpriteImage(0, self.pygame_sprites[sprite_name])
		sprites[sprite_name] = cur_sprite
		
		sprite_name = "display_Z.png"
		cur_sprite = SpriteImage(0, self.pygame_sprites[sprite_name])
		sprites[sprite_name] = cur_sprite
		
		sprite_name = "display_T.png"
		cur_sprite = SpriteImage(0, self.pygame_sprites[sprite_name])
		sprites[sprite_name] = cur_sprite
		
		cur_object = TetronimoDisplay(self.cur_game_obj_id, 5, position_x, position_y, \
				None, sprites)
		self.game_objects[self.cur_game_obj_id] = cur_object
		self.cur_game_obj_id += 1
		
		return cur_object
	
""" --------------------------------------------------
    Initialize each ObjectFactory object with:
        - The current dynamic game object id. Incremented after every game object is created.
	- The game objects being created.
	- The pygame sprites being used for creating the game objects.
	- The fonts for the text boxes.		
	- A reference to the settings.
	- A reference to the input manager. 
-----------------------------------------------------
    ObjectFactory()::create_test_obj()
    
    This function creates the test object.
-----------------------------------------------------
    ObjectFactory()::create_gui_wall()
    
    This function creates the gui wall object.
-----------------------------------------------------
    ObjectFactory()::create_text_box()
    
    This function creates the text box object.
    Assign the current font being used.
    Assign the text box being created.
-----------------------------------------------------
    ObjectFactory()::create_teteronimo_falling()
    
    This function will create the teteronimo falling.
    Assign the teteronimo falling to be created.
-----------------------------------------------------
    ObjectFactory()::create_teteronimo_block()
    
    This function creates the teteronimo falling.
    Assign the sprites for the teteronimo block.
    Assign the name of the current sprite being gathered.
    Assign the current sprites to be gathered.
    Assign the teteronimo falling to be created.
-----------------------------------------------------
    ObjectFactory()::create_teteronimo_display()
    
    This functions creates the teteronimo display.
    Assign the sprites for the teteronimo block.
    Assign the name of the current sprite being gathered.
    Assign the current sprites being gathered
    Assign the teteroimo displaybeing created.
-------------------------------------------------- """
