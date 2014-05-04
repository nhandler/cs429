import pygame

class EntitySprite(pygame.sprite.Sprite):
    shiftby = (0,0)
    
    def __init__(self, position, size):
        pygame.sprite.Sprite.__init__(self)
        self.coords = position
        self.width, self.height = size
        self.health = 1
        self.image = pygame.Surface((0, 0))
        self._reset_rect()
        self.shiftby = (0,0)

    def to_json(self):
        '''
        Serialize the important members of this class as a json object
        '''
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
        '''
        Restore this object from the passed in json object

        @param json - the json object
        '''
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
        self.rect = self.rect.move(self.shiftby)

    def update(self):
        self._reset_rect()
        (x,y) = self.shiftby
        if x > 0: x -= 20
        elif x < 0: x += 20
        if y > 0: y -= 20
        elif y < 0: y += 20
        self.shiftby = (x,y)
        

    def takeHit(self, amount):
        if self.health > 0:
            self.health -= amount
        if self.health <= 0:
            self.dies()

    def dies(self):
        pass
