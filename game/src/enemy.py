import random
from creature import CreatureSprite
from locals import Direction

class EnemySprite (CreatureSprite):
    def __init__(self, image, position, size, direction):
        CreatureSprite.__init__(self, image, position, size, direction)
        self.health = 3

    def act(self, tile):
        i = random.randint(1, 4)

        if self.can_take_action():
            if i == 1: self.direction = Direction.up
            elif i == 2: self.direction = Direction.left
            elif i == 3: self.direction = Direction.right
            else: self.direction = Direction.down
            self.move(self.direction, tile)

            self.action_taken()
        self.iters_until_action -= 1

    def handleOutOfBounds(self, px, py, left, right, up, down):
        if px == left:
            self.direction = Direction.right
        if px == right:
            self.direction = Direction.left
        if py == up:
            self.direction = Direction.down
        if py == down:
            self.direction = Direction.up
