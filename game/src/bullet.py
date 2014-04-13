import pygame
from entity import EntitySprite
from locals import Direction

class BulletSprite (EntitySprite):
    def __init__(self, image_filename, position, size, direction):
        EntitySprite.__init__(self, position, size, direction)
        self.image = pygame.image.load(image_filename)
        self._reset_rect()

    def move(self):
        (x, y) = self.coords
        if self.direction == Direction.up:
            y -= 1
        elif self.direction == Direction.down:
            y += 1
        elif self.direction == Direction.left:
            x -= 1
        elif self.direction == Direction.right:
            x += 1
        self.coords = (x, y)

    def update(self):
        self.move()
        EntitySprite.update(self)
