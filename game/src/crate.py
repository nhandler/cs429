import pygame
from entity import EntitySprite
from item import get_items
from locals import CRATE_IMAGE, BURNING_CRATE_IMAGE

class ObjectSprite (EntitySprite):
    normal = pygame.image.load(CRATE_IMAGE)
    hit = pygame.image.load(BURNING_CRATE_IMAGE)

    def __init__ (self, position=(0, 0), size=(0, 0), item=None, json=None):
        '''
        Initializes the ObjectSprite

        @param position - optional argument to specify position
        @param size - optional argument to specify size of sprite
        @param direction - optional argument to specify direction facing when initialized
        @param json - optional argument to be used when loading from a json file
        '''

        EntitySprite.__init__(self, position, size)
        if json:
            self.from_json(json)
        else:
            self.health = 3
            self.item = item

        if self.health <= 0:
            self.dies()
        else:
            self.image = self._scale(self.normal)
            self._reset_rect()

    def to_json(self):
        '''
        Serialize the important members of this class as a json object.
        '''
        json = EntitySprite.to_json(self)
        json['health'] = self.health
        if self.item:
            json['item'] = self.item.name
        else:
            json['item'] = 'None'

        return json

    def from_json(self, json):
        '''
        Restore this object from the passed in json object

        @param json - the json object
        '''
        EntitySprite.from_json(self, json)
        self.health = json['health']
        self.item = get_items()[json['item']]

    def _scale(self, image):
        return pygame.transform.scale(image, (self.width, self.height))

    def dies(self):
        '''
        Function to be called when the object has no more health left
        '''
        self.image = self._scale(self.hit)
        self._reset_rect()
