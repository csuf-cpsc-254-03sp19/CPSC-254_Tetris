import pygame

from game_object import GameObject
from input_manager import InputManager
from sprite_image import SpriteImage
from object_factory import ObjectFactory
from settings import Settings
from button import Button


"""The primary game system that is the skeleton of the entire game. It contains the setup functions as well as the main game loop and collision detection functions."""
class GameSystem:
	def __init__(self):
		"""Initialized the game system."""
		
		# Checks if the game is currently active.
		self.is_active = True
		
		# The current time elapsed in milliseconds.
		self.delta_time = 0.0
		
		# The pygame clock for limiting the framerate.
		self.pygame_clock = None
		
		# The backbuffer being rendered to.
		self.backbuffer = None
		
		# Colors
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
		
		# The buttons for the title screen.
		self.button_game_title = None
		self.button_play_tetris = None
		self.button_quit = None
		self.button_high_score = None
		self.button_q = None
		self.button_arrow = None
		self.button_z = None
		self.button_x = None
		self.button_c = None
			
		# The input manager for managing keyboard and mouse input.
		self.input_manager = InputManager(self)
		
		# The game object factory for creating the game objects.
		self.object_factory = None
		
		# The settings object for managing the gameplay code.
		self.settings = None
		
		# The game objects for the game. Keys are the game object ids.
		self.game_objects = {}
		
		# The test object references.
		self.test_objects = {}
		
		# The GUI tile objects.
		self.gui_tile_objects = {}
		
		# The GUI text objects.
		self.gui_text_objects = {}
		
		# The tetronimos falling. This is updated every frame from objects gathered from 
		# the game_objects dictionary.
		self.tetronimos_falling = {}
		
		# The tetronimo blocks created by the tetronimos falling. Also includes blocks 
		# that have already landed.
		self.tetronimo_blocks = {}
		
		# The tetronimo displays.
		self.tetronimo_displays = {}
		
		# The pygame sprite images.
		self.pygame_sprites = {}
		
		# The fonts for the text boxes.
		self.fonts = {}
		
		# Create the settings object.
		self.settings = Settings()
		
		# Create the game object factory.
		self.object_factory = ObjectFactory(self.game_objects, self.pygame_sprites, 
				self.fonts)
				
		# Attach all the objects to each other.
		self.settings.object_factory = self.object_factory
		self.settings.tetronimos_falling = self.tetronimos_falling
		self.settings.tetronimo_blocks = self.tetronimo_blocks
		self.settings.input_manager = self.input_manager
		self.settings.game_system = self
		
		self.object_factory.settings = self.settings
		self.object_factory.input_manager = self.input_manager
		
	def start_program(self):
		"""Starts off the program, initializing pygame and loading all the
		sprites, sounds and fonts."""
		
		self.setup_pygame()
		self.load_sprites()
		self.load_fonts()
		self.setup_title_screen()
		self.main_loop()
		
	def load_sprites(self):
		"""Loads all of the sprites from the images folder."""
		
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
		"""Loads a single sprite from the images folder."""
		self.pygame_sprites[cur_sprite_image_name] = pygame.image.load( \
			image_folder_url + cur_sprite_image_name)
	
	def load_fonts(self):
		"""Loads all the fonts for the game engine."""
		
		# The fonts url.
		font_url = "../fonts/"
		
		# Load all of the fonts individually.
		self.load_font(font_url, "PressStart2P.ttf", "PressStart2P-small", 12)
		self.load_font(font_url, "PressStart2P.ttf", "PressStart2P-medium", 32)
	
	def load_font(self, fonts_url, font_file_name, font_key_name, size):
		"""Loads an individual font file."""
		
		# The current font being loaded.
		font1 = pygame.font.Font(fonts_url + font_file_name, size)
		
		self.fonts[font_key_name] = font1
	
	def setup_pygame(self):
		"""Sets up the pygame module."""
		
		# Create the pygame module.
		pygame.init()

		self.settings.init_audio()
		
		# Get the pygame clock.
		self.pygame_clock = pygame.time.Clock()

		# The backbuffer of the game.
		self.backbuffer = pygame.display.set_mode((640, 800))

		# Set the caption for the game window.
		pygame.display.set_caption("Tired of Tetris' Team - Tetris Game")
		
	def setup_title_screen(self):
		"""The code for setting up the title screen."""
		
		# The high score file.
		highscore = open("../data/high_score.txt", "a+")
		highscore = open("../data/high_score.txt", "r+")

		# The high score number.
		highscore = highscore.read()

		if not highscore: 
			whighscore = open("../data/high_score.txt", "w+")
			whighscore.write(str(0))
			whighscore.close()

		# button(font, color, x, y, width, height, text = '')
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
		"""The code for the title screen update."""
		
		# The mouse position.
		pos = self.input_manager.pos
		
		if self.input_manager.mouse_button_pressed:

			# Play Tetris Button
			if self.button_play_tetris.isOver(pos):
				
				# Start the game system.
				self.setup_classic_game()
				self.settings.game_state = 0
				self.button_game_title = None
				self.button_high_score = None
				self.button_play_tetris = None
				self.button_quit = None

			# Quit Button
			elif self.button_quit.isOver(pos):
				self.is_active = False
				
		if self.settings.game_state == 1:
			# If Mouse is over a button, then change to red, otherwise; stay same color
			# ...for play tetris button
			if self.button_play_tetris.isOver(pos):
				self.button_play_tetris.color = self.color_green2
			else:
				self.button_play_tetris.color = self.color_green

			# ... for quit button
			if self.button_quit.isOver(pos):
				self.button_quit.color = self.color_blue2
			else:
				self.button_quit.color = self.color_blue
	
	def setup_classic_game(self):
		"""Sets up a classic game of tetris."""
		
		# Load the gameplay game map.
		self.load_map_gameplay()
		
		# The text for the text boxes.
		text = "NEXT:"
		
		# The color of the text for the text boxes.
		color = (0, 0, 0)
		
		# Create all the text boxes for the game gui.
		self.object_factory.create_text_box(80, 32, text, "PressStart2P-small", 
				color, False)
		
		text = "SAVE:"
		self.object_factory.create_text_box(80, 640, text, "PressStart2P-small", 
				color, False)
		
		text = "HIGH SCORE:"
		self.object_factory.create_text_box(565, 32, text, "PressStart2P-small", 
				color, False)
		
		
		text = "SCORE:"
		self.object_factory.create_text_box(565, 110, text, "PressStart2P-small", 
				color, False)

		color_white = (255, 255, 255)

		self.settings.text_box_score = self.object_factory.create_text_box(565, 145, str(self.settings.score), "PressStart2P-small", 
				color_white, False)
		
		#read in highscore from high_score.txt file
		highscore = open("../data/high_score.txt", "r+")
		highscore = highscore.read()


		# if the score is less than or equal to highscore, then print highscore 
		if int(self.settings.score) <= int(highscore):
			self.settings.text_box_highscore = self.object_factory.create_text_box(565, 70, str(highscore), "PressStart2P-small", 
				color_white, False)
		# if the score is greater than highscore then print highscore will turn to score number. 
		if int(self.settings.score) > int(highscore):
			self.settings.text_box_highscore = self.object_factory.create_text_box(565, 70, str(self.settings.score), "PressStart2P-small", 
				color_white, False)
				
		# Create the tetronimo display objects.
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
		pygame.mixer.music.play(-1, 0.0)
		
	def load_map_gameplay(self):
		"""Loads the game map for the classic tetris game."""
		
		# First clear the previous game objects.
		self.clear_gameplay_objects()
		
		# Use with to ensure that the file is read entirely.
		with open("../data/map_gameplay.txt", "r") as in_file:
			# The text containing all the characters for the map objects.
			map_text = in_file.read()
				
			# The current x position of the current map object being read from.
			cur_position_x = 8

			# The current y position of the current map object being read from.
			cur_position_y = 8
			
			 # Go through every character and create the correct map object from it.
			for char in map_text:
				if not char == '\n':
				
					# Choose a different sprite based on the character.
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
		"""Loads the game over map after the player loses."""
		
		# First clear the previous game objects.
		self.clear_gameplay_objects()
		
		self.setup_title_screen()
		self.settings.game_state = 1
		
	def clear_gameplay_objects(self):
		for key in self.game_objects:
			# The current game object being deleted.
			cur_game_obj = self.game_objects[key]
			
			# The tag of the current game object.
			cur_tag = cur_game_obj.tag
			if cur_tag == 0 or cur_tag == 1 or cur_tag == 2 or cur_tag == 3 or \
					cur_tag == 4 or cur_tag == 5:
				cur_game_obj.marked_for_deletion = True
			
	def main_loop(self):
		"""The main loop for updating the game objects and updating all of the engine components."""
		
		# The entrance to the main loop. The game will continue to loop until 
		# is_active is set to false.
		while self.is_active:
			# Manage the frame rate to 60 fps.
			self.pygame_clock.tick(60)
			self.delta_time = self.pygame_clock.get_time()

			# Reset the tapped keys in the input manager.
			self.input_manager.reset_tapped_keys()
			
			# Check the keyboard input events.
			self.input_manager.check_events()
			
			# If the q key is pressed, exit the game.
			if self.input_manager.pressed_q:
				self.is_active = False
			else:
				# Update the game state.
				
				if self.settings.game_state == 1:
					self.title_screen_update()
				else:
				
					# Gather the game object types.
					self.gather_objects()
					
					# Update the game objects.
					self.settings.update(self.delta_time)
					
					# Update the tetronimos falling.
					for key in self.tetronimos_falling:
						# The current game object being updated.
						cur_object = self.tetronimos_falling[key]
						
						# Only update game objects that are active.
						if cur_object.is_active:
							cur_object.update(self.delta_time)
						
					# Update the tetronimo displays.
					for key in self.tetronimo_displays:
						# The current game object being updated.
						cur_object = self.tetronimo_displays[key]
						
						#Only update game objects that are active.
						if cur_object.is_active:
							cur_object.update(self.delta_time)
						
					self.destroy_objects_marked_for_deletion()
				
					# Update the collision detection.
					self.destroy_objects_marked_for_deletion()
					self.gather_objects()
				
				# Render the game objects.
				self.render_objects()
				
		# Clean up the game engine when finished.
		self.clean_up()
		
	def destroy_objects_marked_for_deletion(self):
		"""Destroys the game objects that are marked for deletion."""
		
		# The empty keys of the dictionary.
		empty_keys = []
		
		for key in self.game_objects:
		    # The current game object being deleted.
			cur_object = self.game_objects[key]
			
			# If marked for deletion, remove the game object from the game object 
			# dictionary.
			if cur_object.marked_for_deletion:
				self.game_objects[key] = None
				empty_keys.append(key)
				
		# Remove the empty keys.
		for key in empty_keys:
			self.game_objects.pop(key, None)
		
	def render_objects(self):
		"""Render all the game objects to the screen."""
		
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
			
			# Fill the background with the color black.
			self.backbuffer.fill((0, 0, 0))
			
			# Render every object in the group. Render every object by layer from 0 to 3.
			for x in range (0, 3):
				for key in self.game_objects:
					# The current game object being rendered.
					cur_game_obj = self.game_objects[key]
					
					# Only render game objects that are active.
					if cur_game_obj.is_active:
					
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
		
	def gather_objects(self):
		"""Gathers all of the game objects by tag type for processing."""
		
		# Clear all the previous game object references.
		self.test_objects.clear()
		self.gui_tile_objects.clear()
		self.gui_text_objects.clear()
		self.tetronimos_falling.clear()
		self.tetronimo_blocks.clear()
		self.tetronimo_displays.clear()
		
		# Gather all the game objects and place them in their proper dictionaries.
		for key in self.game_objects:
			# The current game object being examined.
			cur_game_obj = self.game_objects[key]
			
			# The current game object's id.
			object_id = cur_game_obj.object_id
			
			# Check the tag to tell which dictionary to put the object reference in.
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
		"""Cleans up the game system after it is finished working."""
		# Exit pygame.
		pygame.quit()

