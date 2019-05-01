from game_system import GameSystem
from button import Button

import pygame
pygame.init()


"""This is the primary python script for running the game. You must run this script to run the game and the other scripts."""
# Set a window 'win' to a size of 500x500 pixels
win = pygame.display.set_mode((500, 500))

# Set a caption
pygame.display.set_caption("Tired of Tetris' Team - Tetris Game")

# Colors
Color_Red = (255, 0, 0)
Color_Green = (0, 255, 0)
Color_Blue = (0, 0, 255)
Color_Black = (0, 0, 0)
Color_White = (255, 255, 255)
Color_Gray = (151, 151, 151)
Color_Pink = (209, 96, 171)
Color_Orange = (232, 125, 35)
Color_CosmicBlue = (9, 130, 187)

def redrawWindow():
    win.fill(Color_CosmicBlue)
    Button_GameTitle.draw(win, Color_CosmicBlue)
    Button_PlayTetris.draw(win, Color_Black)
    Button_Quit.draw(win, Color_Black)
    Button_HighScore.draw(win, Color_Black)

# button(color, x, y, width, height, text = '')
run = True
Button_GameTitle = Button(Color_CosmicBlue, 150, 0, 250, 100, "Let's Play Tetris")
Button_PlayTetris = Button(Color_Green, 150, 100, 250, 100, 'Play Tetris')
Button_Quit = Button(Color_Blue, 150, 225, 250, 100, 'Quit')
Button_HighScore = Button(Color_Pink, 150, 350, 250, 100, 'High Score')

while run:
    redrawWindow()
    pygame.display.update()
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        # Click Quit (X) in top right
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        # Press Button, do This!
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Game Title Button
            if Button_GameTitle.isOver(pos):
                print('Game Title button pressed')

            # Play Tetris Button
            if Button_PlayTetris.isOver(pos):
                print('Play Tetris button pressed')
                primary_game_system = GameSystem()  # The primary game system.
                primary_game_system.start_program() # Start the game system.

            # Quit Button
            if Button_Quit.isOver(pos):
                print('Quit button pressed')
                pygame.quit()
                quit()

            # View Highscore List
            if Button_HighScore.isOver(pos):
                print('High Score button pressed')
                # insert code for High Score**********************************

        # If Mouse is over a button, then change to red, otherwise; stay same color
        if event.type == pygame.MOUSEMOTION:
            # ...for play tetris button
            if Button_PlayTetris.isOver(pos):
                Button_PlayTetris.color = Color_Red
            else:
                Button_PlayTetris.color = Color_Green

            # ... for quit button
            if Button_Quit.isOver(pos):
                Button_Quit.color = Color_Red
            else:
                Button_Quit.color = Color_Blue

            # ... for high score button
            if Button_HighScore.isOver(pos):
                Button_HighScore.color = Color_Red
            else:
                Button_HighScore.color = Color_Pink
