import pygame
from entity import EntitySprite
from locals import Direction
from SpriteSheetAnim import SpriteStripAnim

class CreatureSprite(EntitySprite):
    def __init__(self, image_filename, position, size, direction):
        self.strips = self.imageStrips(image_filename)
        self.currentStrip = self.strips[direction]
        self.width, self.height = size
        image = self._get_next_image()
        EntitySprite.__init__(self, image, position, size, direction)
        self.action_wait_val = 12
        self.iters_until_action = 0

    def to_json(self):
        json = EntitySprite.to_json(self)
        json['action_wait_val'] = self.action_wait_val
        json['iters_until_action'] = self.iters_until_action
        
        return json

    def from_json(self, json):
        EntitySprite.from_json(self, json)
        self.action_wait_val = json['action_wait_val']
        self.iters_until_action = json['iters_until_action']

    def _get_next_image(self):
        return pygame.Surface.convert_alpha(
            pygame.transform.scale(
                self.currentStrip.next(),
                (self.width, self.height)
            )
        )

    def imageStrips(self, image):
        strips = dict()
        strips[Direction.up] = SpriteStripAnim(image, (0,0,16,16), 4, (67,255,0), True, 4)
        strips[Direction.down] = SpriteStripAnim(image, (64,0,16,16), 4, (67,255,0), True, 4)
        strips[Direction.right] = SpriteStripAnim(image, (64, 17, 16, 16), 4, (67,255,0), True, 4)
        strips[Direction.left] = SpriteStripAnim(image, (0,17,16,16), 4, (67, 255, 0), True, 4)
        return strips

    def can_take_action(self):
        return self.iters_until_action <= 0

    def action_taken(self):
        self.iters_until_action = self.action_wait_val

    def move(self, direction, tile):
        (x, y) = self.coords
        if direction == Direction.up and tile.is_walkable(x, y - 1):
            y -= 1
        elif direction == Direction.down and tile.is_walkable(x, y + 1):
            y += 1
        elif direction == Direction.left and tile.is_walkable(x - 1, y):
            x -= 1
        elif direction == Direction.right and tile.is_walkable(x + 1, y):
            x += 1
        self.coords = (x, y)

    def isOutOfBounds(self, width, height, left, right, up, down):
        (x, y) = self.coords
        (px, py) = (x, y)
        
        if x < 0:
            x = 0
            (px, py) = (left, y)
        elif x > width - 1: 
            x = width - 1
            (px, py) =  (right, y)
        elif y < 0: 
            y = 0
            (px, py) =  (x, up)
        elif y > height - 1: 
            y = height - 1
            (px, py) =  (x, down)

        self.coords = (x, y)
        if (px, py) != (x, y):
            self.handleOutOfBounds(px, py, left, right, up, down)
        return (px, py)

    # Callback function for being out of bounds
    def handleOutOfBounds(self, px, py, left, right, up, down):
        pass

    def update (self):
        if self.currentStrip is self.strips[self.direction]:
            self.image = self._get_next_image()
        else:
            self.currentStrip = self.strips[self.direction]
            self.image = self._get_next_image()
        self.currentStrip = self.strips[self.direction]
        EntitySprite.update(self)
        
