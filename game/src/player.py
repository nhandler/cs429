import pygame, math, sys
from pygame.locals import *
import spritesheet
from SpriteSheetAnim import SpriteStripAnim

height = 10
width = 10
BLOCK_SIZE = 60

class PlayerSprite (pygame.sprite.Sprite):
    def __init__ (self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.coords = position
        self.position = (((self.coords[0] * BLOCK_SIZE) + (BLOCK_SIZE/2)), ((self.coords[1] * BLOCK_SIZE) + (BLOCK_SIZE/2)))
        self.up = self.down = self.right = self.left = False
        self.direction = "down"
        self.strips = self.imageStrips(self.src_image)
        self.currentStrip = self.strips[self.direction]
        self.image = self.currentStrip.next()
        self.rect_center = self.position

    def imageStrips(image, dummy):
        strips = dict()
        strips["up"] = SpriteStripAnim('Hero.png', (0,0,16,16), 4, 1, True, 4)
        strips["down"] = SpriteStripAnim('Hero.png', (16*4+1,0,16,16), 4, 1, True, 4)
        strips["right"] =  SpriteStripAnim('Hero.png', (16*4+1, 17, 16, 16), 4, 1, True, 4)
        strips["left"] = SpriteStripAnim('Hero.png', (0,17,16,16), 4, 1, True, 4)
        return strips

    def update (self, deltat):
        x, y = self.coords

        if self.up:
            y -= 1
            self.direction = "up"
            if self.currentStrip is self.strips[self.direction]:
                self.image = self.currentStrip.next()
            else:
                self.currentStrip = self.strips[self.direction]
                self.image = self.currentStrip.next()
            #self.up = False
        if self.down:
            y += 1
            self.direction  = "down"
            if self.currentStrip is self.strips[self.direction]:
                self.image = self.currentStrip.next()
            else:
                self.currentStrip = self.strips[self.direction]
                self.image = self.currentStrip.next()
            #self.down = False
        if self.left:
            x -= 1
            self.direction = "left"
            if self.currentStrip is self.strips[self.direction]:
                self.image = self.currentStrip.next()
            else:
                self.currentStrip = self.strips[self.direction]
                self.image = self.currentStrip.next()
            #self.left = False
        if self.right:
            x += 1
            self.direction = "right"
            if self.currentStrip is self.strips[self.direction]:
                self.image = self.currentStrip.next()
            else:
                self.currentStrip = self.strips[self.direction]
                self.image = self.currentStrip.next()
            #self.right = False

        if x < 0: x = 0
        if x > width - 1: x = width - 1
        if y < 0: y = 0
        if y > height - 1: y = height - 1

        self.coords = (x, y)
        self.position = (((x * BLOCK_SIZE) + (BLOCK_SIZE/2)), ((y * BLOCK_SIZE) + (BLOCK_SIZE/2)))
        self.rect = self.image.get_rect()
        self.currentStrip = self.strips[self.direction]
        self.rect.center = self.position