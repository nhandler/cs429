import pygame
import math
import sys
from pygame.locals import *
from entity import EntitySprite
from locals import Direction

class ObjectSprite (EntitySprite):
    normal = pygame.image.load('crate.png')
    hit = pygame.image.load('burning_crate.png')

    def __init__ (self, position, size, item):
        self.width, self.height = size
        image = self._scale(self.normal)
        EntitySprite.__init__(self, image, position, size, Direction.down)
        self.health = 3
        self.item = item

    def _scale(self, image):
        return pygame.transform.scale(image, (self.width, self.height))

    def dies(self):
        self.image = self._scale(self.hit)
        self._reset_rect()
