import pygame
import math
import sys
from pygame.locals import *
import spritesheet
from SpriteSheetAnim import SpriteStripAnim
from tileMap import *


class HorizontalMovement:
    none = 0
    left = 1
    right = 2

class VerticalMovement:
    none = 0
    up = 1
    down = 2

class Direction:
    up = 0
    down = 1
    left = 2
    right = 3

class PlayerSprite (pygame.sprite.Sprite):
    def __init__ (self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.coords = position
        self.position = (((self.coords[0] * TileMap.BLOCK_SIZE) + (TileMap.BLOCK_SIZE/2)), ((self.coords[1] * TileMap.BLOCK_SIZE) + (TileMap.BLOCK_SIZE/2)))
        self.horizontalMovement = HorizontalMovement.none
        self.verticalMovement = VerticalMovement.none
        self.direction = Direction.down
        self.strips = self.imageStrips(self.src_image)
        self.currentStrip = self.strips[self.direction]
        self.image = self.currentStrip.next()
        self.rect_center = self.position

    def imageStrips(image, dummy):
        strips = dict()
        strips[Direction.up] = SpriteStripAnim('Hero.png', (0,0,16,16), 4, 1, True, 4)
        strips[Direction.down] = SpriteStripAnim('Hero.png', (16*4+1,0,16,16), 4, 1, True, 4)
        strips[Direction.right] =  SpriteStripAnim('Hero.png', (16*4+1, 17, 16, 16), 4, 1, True, 4)
        strips[Direction.left] = SpriteStripAnim('Hero.png', (0,17,16,16), 4, 1, True, 4)
        return strips

    def moveUp(self, deltat):
        (x, y) = self.coords
        y -= 1
        self.coords = (x, y)
        self.direction = Direction.up

    def moveDown(self, deltat):
        (x, y) = self.coords
        y += 1
        self.coords = (x, y)
        self.direction = Direction.down

    def moveLeft(self, deltat):
        (x, y) = self.coords
        x -= 1
        self.coords = (x, y)
        self.direction = Direction.left

    def moveRight(self, deltat):
        (x, y) = self.coords
        x += 1
        self.coords = (x, y)
        self.direction = Direction.right

    def changeHorizontalMovement(self, dir):
        self.horizontalMovement = dir

    def changeVerticalMovement(self, dir):
        self.verticalMovement = dir

    def isOutOfBounds(self, deltat):
        (x,y) = self.coords
        if self.horizontalMovement == HorizontalMovement.left:
            x -= 1
        elif self.horizontalMovement == HorizontalMovement.right:
            x +=1

        if self.verticalMovement == VerticalMovement.up:
            y -= 1
        elif self.verticalMovement == VerticalMovement.down:
            y += 1
        
        if x < 0: return (TILE_LEFT, y)
        if x > TileMap.width - 1: return (TILE_RIGHT, y)
        if y < 0: return (x, TILE_UP)
        if y > TileMap.height - 1: return (x, TILE_DOWN)
        return (x, y)

    def update (self, deltat):
        if self.horizontalMovement == HorizontalMovement.left:
            self.moveLeft(deltat)
        elif self.horizontalMovement == HorizontalMovement.right:
            self.moveRight(deltat)

        if self.verticalMovement == VerticalMovement.up:
            self.moveUp(deltat)
        elif self.verticalMovement == VerticalMovement.down:
            self.moveDown(deltat)

        if self.currentStrip is self.strips[self.direction]:
            self.image = self.currentStrip.next()
            self.image = pygame.Surface.convert(self.image)
        else:
            self.currentStrip = self.strips[self.direction]
            self.image = self.currentStrip.next()
            self.image = pygame.Surface.convert(self.image)

        (x, y) = self.coords
        
        if x < 0: x = 0
        if x > TileMap.width - 1: x = TileMap.width - 1
        if y < 0: y = 0
        if y > TileMap.height - 1: y = TileMap.height - 1

        self.coords = (x, y)

        self.position = (((x * TileMap.BLOCK_SIZE) + (TileMap.BLOCK_SIZE/2)), ((y * TileMap.BLOCK_SIZE) + (TileMap.BLOCK_SIZE/2)))
        self.rect = self.image.get_rect()
        self.currentStrip = self.strips[self.direction]
        self.rect.center = self.position
    
