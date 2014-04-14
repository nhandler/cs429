import pygame
from entity import EntitySprite
from locals import Direction, MEDAL_IMAGE

class ButtonSprite (EntitySprite):
    normal = pygame.image.load(MEDAL_IMAGE)

    def __init__ (self, position, size):
        EntitySprite.__init__(self, position, size, Direction.down)
        self.image = self._scale(self.normal)
        self._reset_rect()

    def _scale(self, image):
        return pygame.transform.scale(image, (self.width, self.height))
        
