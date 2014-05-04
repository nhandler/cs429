import pygame
from entity import EntitySprite
from locals import Direction

class BulletSprite (EntitySprite):
    def __init__(self, image_filename, position, size, direction):
        '''
        Intitializes a BulletSprite

        @param image_filename - The file name of the sprite's image
        @param position - The position of the sprite
        @param size - The size of teh sprite
        @param direction - The direction of the sprite
        '''

        EntitySprite.__init__(self, position, size)
        self.direction = direction
        self.image = pygame.image.load(image_filename)
        self._reset_rect()

    def move(self):
        '''
        Function to be called during update to move the position of the sprite
        '''

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
        '''
        Updates the position of sprite
        '''

        self.move()
        EntitySprite.update(self)
