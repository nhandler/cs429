import pygame

class EntitySprite(pygame.sprite.Sprite):
    def __init__(self, position, size, direction):
        pygame.sprite.Sprite.__init__(self)
        self.coords = position
        self.width, self.height = size
        self.direction = direction
        self.image = pygame.Surface((0, 0))
        self._reset_rect()
        self.health = 1

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

    def takeHit(self):
        if self.health > 0:
            self.health -= 1
        if self.health == 0:
            self.dies()

    def dies(self):
        pass
