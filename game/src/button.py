import pygame
from entity import EntitySprite
from locals import Direction

class ButtonSprite (EntitySprite):
    normal = pygame.image.load('../res/medal.png')

    def __init__ (self, position, size):
        self.width, self.height = size
        image = self._scale(self.normal)
        EntitySprite.__init__(self, image, position, size, Direction.down)

    def _scale(self, image):
        return pygame.transform.scale(image, (self.width, self.height))
        
