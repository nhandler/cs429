import pygame

class EntitySprite(pygame.sprite.Sprite):
    def __init__(self, position, size):
        pygame.sprite.Sprite.__init__(self)
        self.coords = position
        self.width, self.height = size
        self.health = 1
        self.image = pygame.Surface((0, 0))
        self._reset_rect()

    def to_json(self):
        (x, y) = self.coords
        json = {
            'x': x,
            'y': y,
            'width': self.width,
            'height': self.height,
            'health': self.health
        }
        
        return json

    def from_json(self, json):
        x = json['x']
        y = json['y']
        self.coords = (x, y)
        self.width = json['width']
        self.height = json['height']
        self.health = json['health']

    def convertCoords(self):
        (x, y) = self.coords
        new_x = x*self.width + self.width/2
        new_y = y*self.height + self.height/2
        return (new_x, new_y)

    def _reset_rect(self):
        self.rect = self.image.get_rect()
        self.rect.center = self.convertCoords()

    def update(self):
        self._reset_rect()

    def takeHit(self, amount):
        if self.health > 0:
            self.health -= amount
        if self.health <= 0:
            self.dies()

    def dies(self):
        pass
