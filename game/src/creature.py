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

    def isOutOfBounds(self):
        (x, y) = self.coords
        if x < 0: 
            return (TILE_LEFT, y)
        if x > TileMap.width - 1: 
            return (TILE_RIGHT, y)
        if y < 0: 
            return (x, TILE_UP)
        if y > TileMap.height - 1: 
            return (x, TILE_DOWN)
        return (x, y)

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

        # TODO remove this
        (x, y) = self.coords
        if x < 0: 
            x = 0
        if x > TileMap.width - 1: 
            x = TileMap.width - 1
        if y < 0: 
            y = 0
        if y > TileMap.height - 1: 
            y = TileMap.height - 1
        self.coords = (x, y)

        self.rect = self.image.get_rect()
        self.currentStrip = self.strips[self.direction]
        self.rect.center = self.convertCoords()
