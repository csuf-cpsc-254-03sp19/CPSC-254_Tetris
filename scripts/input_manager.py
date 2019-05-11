import pygame

""" ---------------------------------------------------------------
    InputManager Class
    
    This class takes care of the keybindings and mouse presses.
    Keybindings are Up, Down, Left, Right, Q, Z, X, C.
    Button Presses are based on location on screen.
--------------------------------------------------------------- """

class InputManager:
	def __init__(self, game_system):
		self.pressed_up = False
		self.pressed_down = False
		self.pressed_left = False
		self.pressed_right = False
		self.pressed_q = False
		self.pressed_z = False
		self.pressed_x = False
		self.pressed_c = False
		self.tapped_c = False
		self.mouse_button_pressed = False
		self.mouse_x = 0
		self.mouse_y = 0
		self.pos = None
		self.game_system = game_system

	def reset_tapped_keys(self):
		self.tapped_c = False
		
	def check_events(self):
		self.mouse_button_pressed = False
		self.pos = pygame.mouse.get_pos()
		self.mouse_x, self.mouse_y = self.pos
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.game_system.is_active = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					self.pressed_right = True
				elif event.key == pygame.K_LEFT:
					self.pressed_left = True
				elif event.key == pygame.K_UP:
					self.pressed_up = True
				elif event.key == pygame.K_DOWN:
					self.pressed_down = True
				elif event.key == pygame.K_q:
					self.pressed_q = True
				elif event.key == pygame.K_z:
					self.pressed_z = True
				elif event.key == pygame.K_x:
					self.pressed_x = True
				elif event.key == pygame.K_c:
					self.tapped_c = True
					self.pressed_c = True
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					self.pressed_right = False
				elif event.key == pygame.K_LEFT:
					self.pressed_left = False
				elif event.key == pygame.K_UP:
					self.pressed_up = False
				elif event.key == pygame.K_DOWN:
					self.pressed_down = False
				elif event.key == pygame.K_q:
					self.pressed_q = False
				elif event.key == pygame.K_z:
					self.pressed_z = False
				elif event.key == pygame.K_x:
					self.pressed_x = False
				elif event.key == pygame.K_c:
					self.pressed_c = False
					self.tapped_c = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				self.mouse_button_pressed = True
				
""" --------------------------------------------------
    Initialize each InputManager object with:
        - a keybinding for Up
	- a keybinding for Down
	- a keybinding for Left
	- a keybinding for Right
	- a keybinding for Q
	- a keybinding for Z
	- a keybinding for X
	- a keybinding for C
	- a flag to check if tapped
	- a flag to check if button pressed
	- the x location of the mouse
	- the y location of the mouse
	- the pos
	- the assigned game system	
-----------------------------------------------------
    InputManager()::reset_tapped_keys()
    
    This function will reset the tapped keys
-----------------------------------------------------
    InputManager()::check_events()
    
    This function will be used to respond to keypress
    and keyrelease events.
    Get the mouse location.
    For each event,
        Do the Quit functions.
	Do the Keydown functions.
	Do the Keyup events.
-------------------------------------------------- """
