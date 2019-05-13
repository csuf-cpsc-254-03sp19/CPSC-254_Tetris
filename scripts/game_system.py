import pygame

from game_object import GameObject
from input_manager import InputManager
from sprite_image import SpriteImage
from object_factory import ObjectFactory
from settings import Settings
from button import Button

""" ----------------------------------------------------------------
    GameSystem class
    
    The primary game system that is the skeleton of the entire game.
    It contains the setup functions as well as the main game loop
    and collision detection functions.
---------------------------------------------------------------- """
class GameSystem:
	def __init__(self):
		self.is_active = True
		self.delta_time = 0.0
		self.pygame_clock = None
		self.backbuffer = None
		
		self.color_red = (255, 0, 0)
		self.color_red2 = (255, 100, 100)
		self.color_green = (0, 190, 0)
		self.color_green2 = (150, 255, 150)
		self.color_blue = (100, 100, 200)
		self.color_blue2 = (200, 200, 255)
		self.color_Black = (0, 0, 0)
		self.color_White = (255, 255, 255)
		self.color_Gray = (151, 151, 151)
		self.color_pink = (209, 96, 171)
		self.color_Orange = (232, 125, 35)
		self.color_cosmic_blue = (9, 130, 187)
		
		self.button_game_title = None
		self.button_play_tetris = None
		self.button_quit = None
		self.button_high_score = None
		self.button_q = None
		self.button_arrow = None
		self.button_z = None
		self.button_x = None
		self.button_c = None	
		
		self.input_manager = InputManager(self)
		self.object_factory = None
		self.settings = None
		
		self.game_objects = {}
		self.test_objects = {}
		self.gui_tile_objects = {}
		self.gui_text_objects = {}
		self.tetronimos_falling = {}
		self.tetronimo_blocks = {}
		self.tetronimo_displays = {}
		self.pygame_sprites = {}
		self.fonts = {}
		self.settings = Settings()
		
		self.object_factory = ObjectFactory(self.game_objects, self.pygame_sprites, self.fonts)
				
		self.settings.object_factory = self.object_factory
		self.settings.tetronimos_falling = self.tetronimos_falling
		self.settings.tetronimo_blocks = self.tetronimo_blocks
		self.settings.input_manager = self.input_manager
		self.settings.game_system = self
		self.object_factory.settings = self.settings
		self.object_factory.input_manager = self.input_manager
		
	def start_program(self):
		self.setup_pygame()
		self.load_sprites()
		self.load_fonts()
		self.setup_title_screen()
		self.main_loop()
		
	def load_sprites(self):
		image_folder_url = "../images/"
		
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
		self.load_sprite(image_folder_url, "wall_out_hor.png")
		self.load_sprite(image_folder_url, "wall_out_vertical_left.png")
		self.load_sprite(image_folder_url, "wall_out_vertical_right.png")
		self.load_sprite(image_folder_url, "wall_out_vertical_left_fade.png")
		self.load_sprite(image_folder_url, "wall_out_vertical_right_fade.png")
		self.load_sprite(image_folder_url, "block_yellow.png")
		self.load_sprite(image_folder_url, "block_skyblue.png")
		self.load_sprite(image_folder_url, "block_orange.png")
		self.load_sprite(image_folder_url, "block_blue.png")
		self.load_sprite(image_folder_url, "block_green.png")
		self.load_sprite(image_folder_url, "block_red.png")
		self.load_sprite(image_folder_url, "block_purple.png")
		self.load_sprite(image_folder_url, "block_grey.png")
		self.load_sprite(image_folder_url, "display_none.png")
		self.load_sprite(image_folder_url, "display_O.png")
		self.load_sprite(image_folder_url, "display_I.png")
		self.load_sprite(image_folder_url, "display_J.png")
		self.load_sprite(image_folder_url, "display_L.png")
		self.load_sprite(image_folder_url, "display_S.png")
		self.load_sprite(image_folder_url, "display_Z.png")
		self.load_sprite(image_folder_url, "display_T.png")
		
	def load_sprite(self, image_folder_url, cur_sprite_image_name):
		self.pygame_sprites[cur_sprite_image_name] = pygame.image.load( \
			image_folder_url + cur_sprite_image_name)
	
	def load_fonts(self):
		font_url = "../fonts/"
		
		self.load_font(font_url, "PressStart2P.ttf", "PressStart2P-small", 12)
		self.load_font(font_url, "PressStart2P.ttf", "PressStart2P-medium", 32)
	
	def load_font(self, fonts_url, font_file_name, font_key_name, size):
		font1 = pygame.font.Font(fonts_url + font_file_name, size)
		
		self.fonts[font_key_name] = font1
	
	def setup_pygame(self):
		pygame.init()
		self.settings.init_audio()
		self.pygame_clock = pygame.time.Clock()
		self.backbuffer = pygame.display.set_mode((640, 800))
		pygame.display.set_caption("Tired of Tetris' Team - Tetris Game")
		
	def setup_title_screen(self):
		highscore = open("../data/high_score.txt", "a+")
		highscore = open("../data/high_score.txt", "r+")
		highscore = highscore.read()

		if not highscore: 
			whighscore = open("../data/high_score.txt", "w+")
			whighscore.write(str(0))
			whighscore.close()

		self.button_game_title = Button(self.fonts["PressStart2P-medium"], \
			self.color_cosmic_blue, 120, 0, 400, 100, "Let's Play Tetris")
		self.button_play_tetris = Button(self.fonts["PressStart2P-medium"], \
			self.color_green, 120, 100, 400, 100, 'Play Tetris')
		self.button_quit = Button(self.fonts["PressStart2P-medium"], \
			self.color_blue, 120, 225, 400, 100, 'Quit')
		self.button_high_score = Button(self.fonts["PressStart2P-medium"], \
			self.color_pink, 20, 350, 600, 100, "High Score: " + str(highscore))
		self.button_q = Button(self.fonts["PressStart2P-small"], \
			self.color_cosmic_blue, 20, 475, 600, 30, "Press q to quit.")
		self.button_arrow = Button(self.fonts["PressStart2P-small"], \
			self.color_cosmic_blue, 20, 500, 600, 30, "Press arrow keys to move tetrimino.")
		self.button_z = Button(self.fonts["PressStart2P-small"], \
			self.color_cosmic_blue, 20, 525, 600, 30, "Press z to rotate tetrimino.")
		self.button_x = Button(self.fonts["PressStart2P-small"], \
			self.color_cosmic_blue, 20, 550, 600, 30, "Press x to drop tetrimino.")
		self.button_c = Button(self.fonts["PressStart2P-small"], \
			self.color_cosmic_blue, 20, 575, 600, 30, "Press c to save tetrimino.")
			
		
	def title_screen_update(self):
		pos = self.input_manager.pos
		
		if self.input_manager.mouse_button_pressed:
			if self.button_play_tetris.isOver(pos):				
				self.setup_classic_game()
				self.settings.game_state = 0
				self.button_game_title = None
				self.button_high_score = None
				self.button_play_tetris = None
				self.button_quit = None	
			elif self.button_quit.isOver(pos):
				self.is_active = False
				
		if self.settings.game_state == 1:
			if self.button_play_tetris.isOver(pos):
				self.button_play_tetris.color = self.color_green2
			else:
				self.button_play_tetris.color = self.color_green

			if self.button_quit.isOver(pos):
				self.button_quit.color = self.color_blue2
			else:
				self.button_quit.color = self.color_blue
	
	def setup_classic_game(self):		
		self.load_map_gameplay()
		text = "NEXT:"
		color = (0, 0, 0)
		
		self.object_factory.create_text_box(80, 32, text, "PressStart2P-small", color, False)
		
		text = "SAVE:"
		self.object_factory.create_text_box(80, 640, text, "PressStart2P-small", color, False)
		
		text = "HIGH SCORE:"
		self.object_factory.create_text_box(565, 32, text, "PressStart2P-small", color, False)
		
		
		text = "SCORE:"
		self.object_factory.create_text_box(565, 110, text, "PressStart2P-small", color, False)

		color_white = (255, 255, 255)

		self.settings.text_box_score = self.object_factory.create_text_box(565, 145, str(self.settings.score), "PressStart2P-small", 
				color_white, False)
		
		highscore = open("../data/high_score.txt", "r+")
		highscore = highscore.read()

		if int(self.settings.score) <= int(highscore):
			self.settings.text_box_highscore = self.object_factory.create_text_box(565, 70, str(highscore), "PressStart2P-small", 
				color_white, False)
		if int(self.settings.score) > int(highscore):
			self.settings.text_box_highscore = self.object_factory.create_text_box(565, 70, str(self.settings.score), "PressStart2P-small", 
				color_white, False)
				
		self.settings.tetronimo_displays.append( \
				self.object_factory.create_tetronimo_display(80, 118))
		self.settings.tetronimo_displays.append( \
				self.object_factory.create_tetronimo_display(80, 262))
		self.settings.tetronimo_displays.append( \
				self.object_factory.create_tetronimo_display(80, 406))
		self.settings.tetronimo_displays.append( \
				self.object_factory.create_tetronimo_display(80, 550))
		self.settings.tetronimo_displays.append( \
				self.object_factory.create_tetronimo_display(80, 726))
		
		self.settings.game_state = 0
		self.settings.reset_tetronimo_assembly()
		
		pygame.mixer.music.load(self.settings.tetris_a_url)
		pygame.mixer.music.play(8, 0.0)
		
	def load_map_gameplay(self):
		self.clear_gameplay_objects()
		with open("../data/map_gameplay.txt", "r") as in_file:
			map_text = in_file.read()
			cur_position_x = 8
			cur_position_y = 8
			
			for char in map_text:
				if not char == '\n':				
					if char == 'C':
						self.object_factory.create_gui_wall(
								cur_position_x, cur_position_y, "wall_in_center.png")
					elif char == 'c' or char == ' ':
						self.object_factory.create_gui_wall(
								cur_position_x, cur_position_y, "wall_out_center.png")
					elif char == 'U':
						self.object_factory.create_gui_wall(
								cur_position_x, cur_position_y, "wall_in_up.png")
					elif char == 'D':
						self.object_factory.create_gui_wall(
								cur_position_x, cur_position_y, "wall_in_down.png")
					elif char == 'L':
						self.object_factory.create_gui_wall(
								cur_position_x, cur_position_y, "wall_in_left.png")
					elif char == 'R':
						self.object_factory.create_gui_wall(
								cur_position_x, cur_position_y, "wall_in_right.png")
					elif char == 'H':
						self.object_factory.create_gui_wall(
								cur_position_x, cur_position_y, "wall_in_hor.png")
					elif char == 'h':
						self.object_factory.create_gui_wall(
								cur_position_x, cur_position_y, "wall_out_hor.png")
					elif char == 'l':
						self.object_factory.create_gui_wall(
								cur_position_x, cur_position_y, "wall_out_vertical_left.png")
					elif char == 'r':
						self.object_factory.create_gui_wall(
								cur_position_x, cur_position_y, "wall_out_vertical_right.png")
					elif char == ',':
						self.object_factory.create_gui_wall(
								cur_position_x, cur_position_y, "wall_out_vertical_left_fade.png")
					elif char == '.':
						self.object_factory.create_gui_wall(
								cur_position_x, cur_position_y, "wall_out_vertical_right_fade.png")
					elif char == '/':
						self.object_factory.create_gui_wall(
								cur_position_x, cur_position_y, "wall_in_upleft.png")
					elif char == '\\':
						self.object_factory.create_gui_wall(
								cur_position_x, cur_position_y, "wall_in_upright.png")
					elif char == '[':
						self.object_factory.create_gui_wall(
								cur_position_x, cur_position_y, "wall_in_downleft.png")
					elif char == ']':
						self.object_factory.create_gui_wall(
								cur_position_x, cur_position_y, "wall_in_downright.png")
					elif char == 'T':
						self.object_factory.create_gui_wall(
								cur_position_x, cur_position_y, "wall_in_leftT.png")
					elif char == 't':
						self.object_factory.create_gui_wall(
								cur_position_x, cur_position_y, "wall_in_rightT.png")
						
					cur_position_x += 16

					if cur_position_x >= (40 * 16) + 8:
						cur_position_x = 8
						cur_position_y += 16
			
	
	def load_map_game_over(self):
		self.clear_gameplay_objects()
		
		self.setup_title_screen()
		
		self.settings.game_state = 1
		self.settings.score = 0
		self.settings.tetronimo_assembly_state = 0
		self.settings.tetronimo_timer_cur = 0
		self.settings.next_tetronimo_type = 0
		self.settings.rows_cleared = 0
		self.settings.tetronimo_timer_period = 1000.0
		self.settings.tetronimo_timer_min_period = 50.0
		self.settings.remove_row_timer_period = 1000.0
		self.settings.block_flash_period = 200.0
		self.settings.tetronimo_timer_period_cache = self.settings.tetronimo_timer_period
		self.settings.delta_time_accum = 0.0
		self.settings.delta_time_accum_remove_row = 0.0
		self.settings.delta_time_accum_block_flash = 0.0
		self.settings.block_fill_pos_y = self.settings.tetronimo_container_bounds[3]
		self.settings.tetronimo_inc = False
		self.settings.tetronimo_displays.clear()
		
	def clear_gameplay_objects(self):
		for key in self.game_objects:
			cur_game_obj = self.game_objects[key]
			cur_tag = cur_game_obj.tag
			
			if cur_tag == 0 or cur_tag == 1 or cur_tag == 2 or cur_tag == 3 or \
					cur_tag == 4 or cur_tag == 5:
				cur_game_obj.marked_for_deletion = True
			
	def main_loop(self):
		while self.is_active:
			self.pygame_clock.tick(60)
			self.delta_time = self.pygame_clock.get_time()
			self.input_manager.reset_tapped_keys()	
			self.input_manager.check_events()
			
			if self.input_manager.pressed_q:
				self.is_active = False
			else:
				if self.settings.game_state == 1:
					self.title_screen_update()
				else:
					self.gather_objects()
					self.settings.update(self.delta_time)
					
					for key in self.tetronimos_falling:
						cur_object = self.tetronimos_falling[key]
						if cur_object.is_active:
							cur_object.update(self.delta_time)		
					for key in self.tetronimo_displays:
						cur_object = self.tetronimo_displays[key]
						if cur_object.is_active:
							cur_object.update(self.delta_time)
						
					self.destroy_objects_marked_for_deletion()
					self.destroy_objects_marked_for_deletion()
					self.gather_objects()
				
				self.render_objects()
				
		self.clean_up()
		
	def destroy_objects_marked_for_deletion(self):
		empty_keys = []
		
		for key in self.game_objects:
			cur_object = self.game_objects[key]	
			if cur_object.marked_for_deletion:
				self.game_objects[key] = None
				empty_keys.append(key)
				
		for key in empty_keys:
			self.game_objects.pop(key, None)
		
	def render_objects(self):
		if self.settings.game_state == 1:
			self.backbuffer.fill(self.color_cosmic_blue)
			self.button_game_title.draw(self.backbuffer, self.color_cosmic_blue)
			self.button_play_tetris.draw(self.backbuffer, self.color_Black)
			self.button_quit.draw(self.backbuffer, self.color_Black)
			self.button_high_score.draw(self.backbuffer, self.color_Black)
			self.button_q.draw(self.backbuffer, self.color_Black)
			self.button_arrow.draw(self.backbuffer, self.color_Black)
			self.button_z.draw(self.backbuffer, self.color_Black)
			self.button_x.draw(self.backbuffer, self.color_Black)
			self.button_c.draw(self.backbuffer, self.color_Black)
		else:
			self.backbuffer.fill((0, 0, 0))
	
			for x in range (0, 3):
				for key in self.game_objects:
					cur_game_obj = self.game_objects[key]
					
					if cur_game_obj.is_active:
						cur_sprite_image = cur_game_obj.cur_sprite_image
						
						if cur_sprite_image is not None and \
							cur_sprite_image.image_layer == x and \
							cur_sprite_image.image is not None and \
							cur_sprite_image.image_rect is not None:	
							cur_sprite_image.update_image_rect(cur_game_obj.position_x, cur_game_obj.position_y)
							cur_image = cur_sprite_image.image
							cur_rect = cur_sprite_image.image_rect
							self.backbuffer.blit(cur_image, cur_rect)
		pygame.display.flip()
		
	def gather_objects(self):
		self.test_objects.clear()
		self.gui_tile_objects.clear()
		self.gui_text_objects.clear()
		self.tetronimos_falling.clear()
		self.tetronimo_blocks.clear()
		self.tetronimo_displays.clear()
		for key in self.game_objects:
			cur_game_obj = self.game_objects[key]
			object_id = cur_game_obj.object_id
			
			if cur_game_obj.tag == 0:
				self.test_objects[object_id] = cur_game_obj
			elif cur_game_obj.tag == 1:
				self.gui_tile_objects[object_id] = cur_game_obj
			elif cur_game_obj.tag == 2:
				self.gui_text_objects[object_id] = cur_game_obj
			elif cur_game_obj.tag == 3:
				self.tetronimos_falling[object_id] = cur_game_obj
			elif cur_game_obj.tag == 4:
				self.tetronimo_blocks[object_id] = cur_game_obj
			elif cur_game_obj.tag == 5:
				self.tetronimo_displays[object_id] = cur_game_obj
	@staticmethod
	def clean_up():
		pygame.quit()
""" -------------------------------------------------------------------------
    Initialize each GameSystem object with:
        - a flag that checks if the game is currently active.
	- a time the current time elapsed in milliseconds.
	- the pygame clock for limiting the framerate.
	- a backbuffer being rendered to.
	- an assortment of RGB assigned colors
	- a collection of buttons for the title screen.
	- an input manager for managing keyboard and mouse input.
	- a game object factory for creating the game objects.
	- a settings object for managing the gameplay code.
	- game objects for the game. Keys are the game object ids.
	- test object references.
	- GUI tile objects.
	- GUI text objects.
	- the tetronimos falling. This is updated every frame
	      from objects gathered from the game_objects dictionary.
	- the tetronimo blocks created by the tetronimos falling.
	      Also includes blocks that have already landed.
	- the tetronimo displays.
	- the pygame sprite images.
	- the fonts for the text boxes.
	- an instance to create the settings object.
	- an instance to create the game object factory.
	- attach all the objects to the object_factory, tetronimos_falling,
	      teteronimo_blocks, input_manager, game_system, settings, and
	      the input manager	      
----------------------------------------------------------------------------
    GameSystem()::start_program()
    
    This function starts off the program, initializing pygame
    and loading all the sprites, sounds and fonts
----------------------------------------------------------------------------
    GameSystem()::load_sprites()
    
    Loads all of the sprites from the images folder.
    Assign the image folder url.
    The current sprite image being loaded.
    Not to be confused with the sprite image class.
----------------------------------------------------------------------------
    GameSystem()::load_sprite()
    
    Load a single sprite form the images folder.
----------------------------------------------------------------------------
    GameSystem()::load_fonts()
    
    Loads all the fonts for the game engine
    Assign the fonts url
    Load all the fonts individually
----------------------------------------------------------------------------
    GameSystem()::load_font()
    
    Load an individual font file.
    Assign the current font being loaded.
----------------------------------------------------------------------------
    GameSystem()::setup_pygame()
    
    Set up the pygame module.
    Create the pygame module.
    Get the pygame clock.
    The backbuffer of the game.
    Set the caption for the game window.
----------------------------------------------------------------------------
    GameSystem()::setup_title_screen()
    
    Assign the code for setting up the title screen
    Assign the high score file
    Assign the high score number
    Button(font, color, x, y, width, height, text = '')
----------------------------------------------------------------------------
    GameSystem()::title_screen_update()
    
    The code for the title screen update
    Assign the mouse position
        Play Tetris Button
	    Start the Game System
	Quit Button
    If Mouse is over a button, then change to red, otherwise; stay same color
        For play Tetris Button
	And for Quit Button
----------------------------------------------------------------------------
    GameSystem()::setup_classic_game()
    
    Sets up a classic game map
    Load the gameplay game map
    The text for the text boxes
    The color of the text for the text boxes
    Create all the text boxes for the same gui.
    Read in highscore from high_score.txt file
    If the score is less than or equal to highscore, then print highscore
    If the score is greater than the highscore then print highscore will turn to score number
    Create the teteronimo display objects
----------------------------------------------------------------------------
    GameSystem()::load_map_gameplay()
    
    Loads the game map for the classic tetris game.
    First clear the previous game objects.
    Use with to ensure that the file is read entirely.
        The text containing all the characters for the map objects.
	The current x position of the current map object being read from.
	The current y position of the current map object being read from.
	    Go through every character and create the correct map object from it.
		Choose a different sprite based on the character.
----------------------------------------------------------------------------
    GameSystem()::load_map_game_over()
    
    Loads the game over map after the player loses.
    First clear the previous game objects.
----------------------------------------------------------------------------
    GameSystem()::clear_gameplay_objects()
    
    Clear all these gameplay objects.
    Assign the current game object from being deleted.
    Assign the tag of the current game object to be deleted.
----------------------------------------------------------------------------
    GameSystem()::main_loop()
    
    The main loop for updating the game objects and updating all of the engine components.
    At the entrance to the main loop,
        The game will continue to loop until is_active is set to false.
	Manage the frame rate to 60 fps.
	Reset the tapped keys in the input manager.
	Check the keyboard input events.
	If the q key is pressed, then exit the game.
	Otherwise, update the game state.
	    Gather the game object types
	    Update the game objects
	    Update the teteronimos falling.
	        The current game object being updated
		Only update game objects that are active
	    Update the teteronimos displays.
	        The current game object being updated
		Only pupdate game objects that are active
            Update the collision detection
	Render the game objects
    Lastly, clean up the game engine when finished.
----------------------------------------------------------------------------    
    GameSystem()::destroy_objects_marked_for_deletion()
    
    Destroy the game objects that are marked for deletion
    Initialize the empty keys of the dictionary
    For each key,
        Assign the current game object to be deleted
	If marked for deletion,
	    remove the game object from the game object dictionary.
	For all these keys, pop/remove the keys.
----------------------------------------------------------------------------
    GameSystem()::render_objects()
    
    Render all the game objects to the screen.
    Default set buffer to render a black screen.
    Otherwise, fill the back ground with black first
    Then, Render every object in the group. Render every object by layer from 0 to 3.
    And for each object in the group, 
        Assign the current game object to be rendered.
	Only render game obects that are active
	If active,
	    Assign the current sprite of the game object being rendered
	    If no image, don't render it.
	    Update the object rect for the rendering process
	    Assign the current image being rendered.
	    Assign the rect of the current image being rendered.
	    Blit the sprite to the backbuffer.
    Lastly, swap the backbuffer.
----------------------------------------------------------------------------
    GameSystem()::gather_objects()
    
    Gathers all of the game objects by tag type for processing.
    By First, clear all the previous game object references.
    Then, gather all the game objects and place them in their proper dictionaries.
    And for each object,
        Assign the current game object to be examined.
	Assign the current game object id
	Check the tag to tell which dictionary to put the object reference in.
----------------------------------------------------------------------------
    GameSystem()::clean_up()
    
    Cleans up the game system after it is finished working. Exit pygame
------------------------------------------------------------------------- """
