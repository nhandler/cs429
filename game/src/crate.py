import pygame, math, sys
from pygame.locals import *

BLOCK_SIZE = 60

class ObjectSprite (pygame.sprite.Sprite):
    normal = pygame.image.load('crate.png')
    hit = pygame.image.load('burning_crate.png')

    def __init__ (self, position):
        pygame.sprite.Sprite.__init__(self)
        self.coords = position
        self.position = (((self.coords[0] * BLOCK_SIZE) + (BLOCK_SIZE/2)), ((self.coords[1] * BLOCK_SIZE) + (BLOCK_SIZE/2)))
        self.image = self.normal
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.health = 3

    def update (self, hit_list):
        if self in hit_list:
            self.image = self.hit

        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def takeHit(self):
        if self.health > 0:
            self.health -= 1
        if self.health == 0:
            self.image = self.hit
            self.rect = self.image.get_rect()
            self.rect.center = self.position
