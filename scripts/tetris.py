from game_system import GameSystem
from button import Button

import pygame
pygame.init()


"""This is the primary python script for running the game. You must run this script to run the game and the other scripts."""
primary_game_system = GameSystem()  # The primary game system.
primary_game_system.start_program() # Start the game system.