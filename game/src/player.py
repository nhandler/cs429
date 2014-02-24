import pygame, math, sys
from pygame.locals import *
import spritesheet
from SpriteSheetAnim import SpriteStripAnim

height = 10
width = 10
BLOCK_SIZE = 60

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
        self.position = (((self.coords[0] * BLOCK_SIZE) + (BLOCK_SIZE/2)), ((self.coords[1] * BLOCK_SIZE) + (BLOCK_SIZE/2)))
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
        else:
            self.currentStrip = self.strips[self.direction]
            self.image = self.currentStrip.next()

        (x, y) = self.coords

        if x < 0: x = 0
        if x > width - 1: x = width - 1
        if y < 0: y = 0
        if y > height - 1: y = height - 1

        self.coords = (x, y)

        self.position = (((x * BLOCK_SIZE) + (BLOCK_SIZE/2)), ((y * BLOCK_SIZE) + (BLOCK_SIZE/2)))
        self.rect = self.image.get_rect()
        self.currentStrip = self.strips[self.direction]
        self.rect.center = self.position
