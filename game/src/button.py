import pygame
from entity import EntitySprite
from locals import BUTTON_IMAGE

class ButtonSprite (EntitySprite):
    normal = pygame.image.load(BUTTON_IMAGE)

    def __init__ (self, position=(0, 0), size=(0, 0), json=None):
    	'''
    	Initializes the button 

    	@param position - optional argument to specify position
        @param size - optional argument to specify size of sprite
        @param direction - optional argument to specify direction facing when initialized
        @param json - optional argument to be used when loading from a json file
    	'''

        EntitySprite.__init__(self, position, size)
        if json:
            self.from_json(json)
        self.image = self._scale(self.normal)
        self._reset_rect()

    def _scale(self, image):
        return pygame.transform.scale(image, (self.width, self.height))
        
