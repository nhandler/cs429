import pygame
import math
import sys
from pygame.locals import *
import spritesheet
from SpriteSheetAnim import SpriteStripAnim
from tileMap import *

class Direction:
    up = 0
    down = 1
    left = 2
    right = 3

class BulletSprite (pygame.sprite.Sprite):
    def __init__ (self, image, position, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.coords = position
        self.position = (((self.coords[0] * TileMap.BLOCK_SIZE) + (TileMap.BLOCK_SIZE/2)), ((self.coords[1] * TileMap.BLOCK_SIZE) + (TileMap.BLOCK_SIZE/2)))
        self.direction = direction
        self.rect_center = self.position

    def move(self):
        (x, y) = self.coords
        if self.direction == Direction.up: y -= 1
        elif self.direction == Direction.down: y += 1
        elif self.direction == Direction.left: x -= 1
        elif self.direction == Direction.right: x += 1
        self.coords = (x, y)

    def update (self, deltat):
        self.move()
        (x, y) = self.coords
        self.position = (((x * TileMap.BLOCK_SIZE) + (TileMap.BLOCK_SIZE/2)), ((y * TileMap.BLOCK_SIZE) + (TileMap.BLOCK_SIZE/2)))
        self.rect = self.image.get_rect()
        self.rect.center = self.position