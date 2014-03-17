import pygame
import math
import sys
from pygame.locals import *
import spritesheet
from SpriteSheetAnim import SpriteStripAnim

class Direction:
    up = 0
    down = 1
    left = 2
    right = 3

class BulletSprite (pygame.sprite.Sprite):
    def __init__ (self, image, position, size, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.coords = position
        (width, height) = size
        self.width = width
        self.height = height
        self.position = self.convertCoords()
        self.direction = direction
        self.rect = self.image.get_rect()
        self.rect_center = self.position

    def convertCoords(self):
        (x, y) = self.coords
        new_x = x*self.width + self.width/2
        new_y = y*self.height + self.height/2

    def move(self):
        (x, y) = self.coords
        if self.direction == Direction.up: y -= 1
        elif self.direction == Direction.down: y += 1
        elif self.direction == Direction.left: x -= 1
        elif self.direction == Direction.right: x += 1
        self.coords = (x, y)

    def update (self):
        self.move()
        (x, y) = self.coords
        self.position = self.convertCoords()
        self.rect = self.image.get_rect()
        self.rect.center = self.position
