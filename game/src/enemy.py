import random
from creature import CreatureSprite
from locals import Direction, ENEMY_IMAGE

class EnemySprite (CreatureSprite):
    def __init__(self, position=(0, 0), size=(0, 0), direction=Direction.down, json=None):
        CreatureSprite.__init__(self, ENEMY_IMAGE, position, size, direction)
        if json:
            self.from_json(json)
        else:
            self.health = 3

    def to_json(self):
        '''
        Serialize the important members of this class as a json object
        '''
        json = CreatureSprite.to_json(self)
        json['health'] = self.health
        return json

    def from_json(self, json):
        '''
        Restore this object from the passed in json object

        @param json - the json object
        '''
        CreatureSprite.from_json(self, json)
        self.health = json['health']

    def act(self, tile):
        '''
        Does the action of this particular EnemySprite

        @param tile - The tile the sprite is on
        '''
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
        '''
        Handles the case where the sprite would go out of bounds

        @param px - x coordinate
        @param py - y coordinate
        @param left - coordinate of left side of game world
        @param right - coordinate of right side of game world
        @param down - coordinate of bottom of game world
        @param up - coordinate of bootom of game world
        '''
        if px == left:
            self.direction = Direction.right
        if px == right:
            self.direction = Direction.left
        if py == up:
            self.direction = Direction.down
        if py == down:
            self.direction = Direction.up
