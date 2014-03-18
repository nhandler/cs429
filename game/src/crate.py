import pygame
import math
import sys
from pygame.locals import *

class ObjectSprite (pygame.sprite.Sprite):
    normal = pygame.image.load('crate.png')
    hit = pygame.image.load('burning_crate.png')

    def __init__ (self, position, size, item):
        pygame.sprite.Sprite.__init__(self)
        self.coords = position
        (width, height) = size
        self.width = width
        self.height = height
        self.image = self._scale(self.normal)
        self.rect = self.image.get_rect()
        self.rect.center = self.convertCoords()
        self.health = 3
        self.item = item

    def _scale(self, image):
        return pygame.transform.scale(image, (self.width, self.height))

    def update (self, hit_list):
        if self in hit_list:
            self.image = self._scale(self.hit)

        self.rect = self.image.get_rect()
        self.rect.center = self.convertCoords()

    def convertCoords(self):
        (x, y) = self.coords
        new_x = x*self.width + self.width/2
        new_y = y*self.height + self.height/2
        return (new_x, new_y)

    def takeHit(self):
        if self.health > 0:
            self.health -= 1
        if self.health == 0:
            self.image = self._scale(self.hit)
            self.rect = self.image.get_rect()
            self.rect.center = self.convertCoords()
