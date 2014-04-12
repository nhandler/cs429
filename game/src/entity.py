import pygame

class EntitySprite(pygame.sprite.Sprite):
    def __init__(self, image, position, size, direction):
        pygame.sprite.Sprite.__init__(self)
        self.coords = position
        self.width, self.height = size
        self.direction = direction
        self.image = image
        self._reset_rect()
        self.health = 1

    def to_json(self):
        (x, y) = self.coords
        json = {
            'x': x,
            'y': y,
            'width': self.width,
            'height': self.height,
            'direction': self.direction,
            'health': self.health
        }
        
        return json

    def from_json(self, json):
        x = json['x']
        y = json['y']
        self.coords = (x, y)
        self.width = json['width']
        self.height = json['height']
        self.direction = json['direction']
        self.health = json['health']

    def convertCoords(self):
        (x, y) = self.coords
        new_x = x*self.width + self.width/2
        new_y = y*self.height + self.height/2
        return (new_x, new_y)

    def _reset_rect(self):
        self.position = self.convertCoords()
        self.rect = self.image.get_rect()
        self.rect.center = self.convertCoords()

    def update(self):
        self._reset_rect()

    def takeHit(self):
        if self.health > 0:
            self.health -= 1
        if self.health == 0:
            self.dies()

    def dies(self):
        pass
