import pygame

from pygame.sprite import Sprite

""" -----------------------------------------------------
    GameObject class

    The primary game object abstract class.
    All game object types are inherited from this class.
    It contains a dictionary of sprite images,
    a position in 2D world space, and a collision box.
    The selection of the default sprite
    must be chosen by the inherited constuctor.
----------------------------------------------------- """
class GameObject():
	def __init__(self, object_id, tag, position_x, position_y, collision_box, sprite_images):		
		self.is_active = True
		self.marked_for_deletion = False
		self.object_id = object_id
		self.tag = tag
		self.position_x = position_x	
		self.position_y = position_y
		self.cur_sprite_image = None
		self.sprite_images = sprite_images
		self.collision_box = collision_box
""" --------------------------------------------------
    Initialize each Button object with:
        - a flag to check if the game object is active.
	      Used to allow updating or rendering.
	- a flag to check if the object is marked for deletion,
	      which will allow the object to be deleted
	      before the next frame is reached.
	- the game object ID.
	- a game object tag. Used to identify certain game objects.
	      0 - test object.
	      1 - GUI til object.
	      2 - GUI text object.
	      3 - Teteronimo falling.
	      4 - Teteronimo block.
	- an x position of the game object in 2D world space	
	- a  y-locaiton of the game object in 2D world space
	- the current sprite image object being used for rendering.
	- the sprites to use. It is a dictionary of sprite image objects,
	      where the key is the file name of the sprite.
	- the collision box used for collision detection. It is of type pygame.Rect
-------------------------------------------------- """
