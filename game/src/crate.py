import pygame
from entity import EntitySprite
from locals import Direction

class ObjectSprite (EntitySprite):
    normal = pygame.image.load('../res/crate.png')
    hit = pygame.image.load('../res/burning_crate.png')

    def __init__ (self, position, size, item):
        self.width, self.height = size
        image = self._scale(self.normal)
        EntitySprite.__init__(self, image, position, size, Direction.down)
        self.health = 3
        self.item = item

    def to_json(self):
        json = EntitySprite.to_json(self)
        json['health'] = self.health
        #TODO: add proper item support
        json['item'] = 'None'

        return json

    def from_json(self, json):
        EntitySprite.from_json(self, json)
        self.health = json['health']
        #TODO: add proper item support
#        self.item = json['item']

    def _scale(self, image):
        return pygame.transform.scale(image, (self.width, self.height))

    def dies(self):
        self.image = self._scale(self.hit)
        self._reset_rect()
