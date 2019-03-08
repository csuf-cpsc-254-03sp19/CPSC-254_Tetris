import pygame

from game_object import GameObject

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
