import pygame

from game_object import GameObject

"""The primary game system that is the skeleton of the entire game. It contains the setup functions as well as the main game loop and collision detection functions."""
class GameSystem:
	def __init__(self):
		"""Initialized the game system."""
		print("Hello world!")
		
		# The game objects for the game. Keys are the game object ids.
		self.game_objects = {}
		
	def start_program(self):
		"""Starts off the program, initializing pygame and loading all the
		sprites, sounds and fonts."""
		print("The game has just begun.")
		
		self.setup_pygame()
		
	def setup_pygame(self):
		"""Sets up the pygame module."""
		
		# Create the pygame module.
		pygame.init()

		# Get the pygame clock.
		self.pygame_clock = pygame.time.Clock()

		# The backbuffer of the game.
		self.backbuffer = pygame.display.set_mode((512, 768))

		# Set the caption for the game window.
		pygame.display.set_caption("Tetris")
