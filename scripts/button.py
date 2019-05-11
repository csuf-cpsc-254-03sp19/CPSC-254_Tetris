import pygame

""" ---------------------------------------------------------------
    Button Class
    
    This class is for adding buttons to the menu.
    Each button will have a font, color, location, size, and text.
--------------------------------------------------------------- """

class Button():
	def __init__(self, font, color, x, y, width, height, text = ''):
		self.font = font
		self.color = color
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.text = text

	def draw(self, win, outline = None):
		# Call this method to draw the button on the screen
		if outline:
			pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)

		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

		if self.text != '':
			text = self.font.render(self.text, 1, (0, 0, 0))
			win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

	def isOver(self, pos):
		# Pos is the mouse position or a tuple of (x,y) coordinates
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				return True
		return False

""" --------------------------------------------------
    Initialize each Button object with:
        - an assigned font
	- an assigned color
	- an x-location
	- a  y-locaiton
	- the width of the button
	- the height of the button	
-----------------------------------------------------
    Button()::draw()
    
    This function will be used to draw button objects
    by utilizing the pygame.draw.rect function.
-----------------------------------------------------
    Button()::isOver()
    
    This function will be used to check whether
    the cursor is over a button or not.
-------------------------------------------------- """
