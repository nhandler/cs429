import pygame
from pygame.locals import *
from SpriteSheetAnim import SpriteStripAnim
from tileMap import *
from locals import Direction

class CreatureSprite(pygame.sprite.Sprite):
    ACTION_WAIT_VAL = 10

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.coords = position
        self.direction = Direction.down
        self.strips = self.imageStrips(image)
        self.currentStrip = self.strips[self.direction]
        self.image = self.currentStrip.next()
        self.rect_center = self.convertCoords()
        self.iters_until_action = 0

    def convertCoords(self):
        x = self.coords[0]*TileMap.BLOCK_SIZE + TileMap.BLOCK_SIZE/2
        y = self.coords[1]*TileMap.BLOCK_SIZE + TileMap.BLOCK_SIZE/2
        return (x, y)

    def imageStrips(self, image):
        strips = dict()
        strips[Direction.up] = SpriteStripAnim(image, (0,0,16,16), 4, 1, True, 4)
        strips[Direction.down] = SpriteStripAnim(image, (49,0,16,16), 4, 1, True, 4)
        strips[Direction.right] = SpriteStripAnim(image, (49, 17, 16, 16), 4, 1, True, 4)
        strips[Direction.left] = SpriteStripAnim(image, (0,17,16,16), 4, 1, True, 4)
        return strips

    def can_take_action(self):
        return self.iters_until_action <= 0

    def action_taken(self):
        self.iters_until_action = CreatureSprite.ACTION_WAIT_VAL

    def move(self, direction):
        (x, y) = self.coords
        if direction == Direction.up:
            y -= 1
        elif direction == Direction.down:
            y += 1
        elif direction == Direction.left:
            x -= 1
        elif direction == Direction.right:
            x += 1
        self.coords = (x, y)

    def isOutOfBounds(self, width, height, left, right, up, down):
        (x, y) = self.coords
        (px, py) = (x, y)
        
        if x < 0:
            x = 0
            (px, py) = (left, y)
        elif x > width - 1: 
            x = width - 1
            (px, py) =  (right, y)
        elif y < 0: 
            y = 0
            (px, py) =  (x, up)
        elif y > height - 1: 
            y = height - 1
            (px, py) =  (x, down)

        self.coords = (x, y)
        if (px, py) != (x, y):
            self.handleOutOfBounds(px, py, left, right, up, down)
        return (px, py)

    # Callback function for being out of bounds
    def handleOutOfBounds(self, px, py, left, right, up, down):
        pass

    def update (self):
        if self.currentStrip is self.strips[self.direction]:
            self.image = pygame.Surface.convert(
                self.currentStrip.next()
            )
        else:
            self.currentStrip = self.strips[self.direction]
            self.image = pygame.Surface.convert(
                self.currentStrip.next()
            )

        self.rect = self.image.get_rect()
        self.currentStrip = self.strips[self.direction]
        self.rect.center = self.convertCoords()
