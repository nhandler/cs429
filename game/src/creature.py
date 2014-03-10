import pygame
from pygame.locals import *
from SpriteSheetAnim import SpriteStripAnim
from tileMap import *

class Direction:
    up = 0
    down = 1
    left = 2
    right = 3

class CreatureSprite(pygame.sprite.Sprite):
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.coords = position
        self.direction = Direction.down
        self.strips = self.imageStrips(image)
        self.currentStrip = self.strips[self.direction]
        self.image = self.currentStrip.next()
        self.rect_center = self.convertCoords()

    def convertCoords(self):
        x = self.coords[0]*TileMap.BLOCK_SIZE + TileMap.BLOCK_SIZE/2
        y = self.coords[1]*TileMap.BLOCK_SIZE + TileMap.BLOCK_SIZE/2
        return (x, y)

    def imageStrips(self, image):
        strips = dict()
        strips[Direction.up] = SpriteStripAnim(image, (0,0,16,16), 4, 1, True, 4)
        strips[Direction.down] = SpriteStripAnim(image, (16*4+1,0,16,16), 4, 1, True, 4)
        strips[Direction.right] = SpriteStripAnim(image, (16*4+1, 17, 16, 16), 4, 1, True, 4)
        strips[Direction.left] = SpriteStripAnim(image, (0,17,16,16), 4, 1, True, 4)
        return strips

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
        self.direction = direction

    def isOutOfBounds(self):
        (x, y) = self.coords
        if x < 0: return (TILE_LEFT, y)
        if x > TileMap.width - 1: return (TILE_RIGHT, y)
        if y < 0: return (x, TILE_UP)
        if y > TileMap.height - 1: return (x, TILE_DOWN)
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

        (x, y) = self.coords
        if x < 0: x = 0
        if x > TileMap.width - 1: x = TileMap.width - 1
        if y < 0: y = 0
        if y > TileMap.height - 1: y = TileMap.height - 1
        self.coords = (x, y)

        self.rect = self.image.get_rect()
        self.currentStrip = self.strips[self.direction]
        self.rect.center = self.convertCoords()
