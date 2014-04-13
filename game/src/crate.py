import pygame
from entity import EntitySprite
from locals import Direction, CRATE_IMAGE, BURNING_CRATE_IMAGE

class ObjectSprite (EntitySprite):
    normal = pygame.image.load(CRATE_IMAGE)
    hit = pygame.image.load(BURNING_CRATE_IMAGE)

    def __init__ (self, position, size, item):
        EntitySprite.__init__(self, position, size, Direction.down)
        self.image = self._scale(self.normal)
        self.health = 3
        self.item = item

    def _scale(self, image):
        return pygame.transform.scale(image, (self.width, self.height))

    def dies(self):
        self.image = self._scale(self.hit)
        self._reset_rect()
