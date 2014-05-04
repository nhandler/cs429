import random
from bullet import BulletSprite
from shooter import ShooterSprite
from locals import Direction, SHOOTER_BULLET_IMAGE, BOSS_IMAGE

class BossSprite (ShooterSprite):

    def __init__(self, position=(0, 0), size=(0, 0), direction=Direction.down, json=None):
        '''
        Constructor for BossSprite

        @param position - optional argument to specify position
        @param size - optional argument to specify size of sprite
        @param direction - optional argument to specify direction facing when initialized
        @param json - optional argument to be used when loading from a json file
        '''

        ShooterSprite.__init__(self, position, size, direction)
        if json:
            self.from_json(json)
        else:
            self.health = 50
        self._create_spritesheet(BOSS_IMAGE)

    def to_json(self):
        '''
        Serialize the important members of this class as a json object
        '''
        json = ShooterSprite.to_json(self)
        json['health'] = 50

        return json

    def from_json(self, json):
        '''
        Restore this object from the passed in json object

        @param json - the json object
        '''
        ShooterSprite.from_json(self, json)
        self.health = json['health']

    def act(self, tile):
        '''
        Function to be called when the action is supposed to be taken
        Uses a random number to decide whether or not to move

        @param tile - The tile the boss is currently on
        '''

        i = random.randint(1, 2)

        if self.can_take_action():
            if i == 1: self.direction = Direction.up
            else: self.direction = Direction.down
            self.move(self.direction, tile)
            z = random.randint(1, 2)
            if z == 1:
                self.move(self.direction, tile)

            self.direction = Direction.left

            self.action_taken()
        self.iters_until_action -= 1

    def shouldShoot(self, px, py):
        '''
        Function to decide whether or not to shoot
        This is based on the player's (x,y) and a random number

        @param px - The player's current x
        @param py - The player's current y 

        '''

        (x, y) = self.coords
        i = random.randint(1, 10)

        if x == px and y == py:
            return False
        elif i > 9:
            return True
        else:
            return False

    def shoot(self, sprite, group):
        '''
        Function to shoot the bullet 

        @param sprite - The sprite that is shooting
        @param group - The group for the bullet to added to
        '''
        bullet = BulletSprite(SHOOTER_BULLET_IMAGE, sprite.coords, (self.width, self.height), Direction.left)
        group.add(bullet)
        bullet = BulletSprite(SHOOTER_BULLET_IMAGE, sprite.coords, (self.width, self.height), Direction.up)
        group.add(bullet)
        bullet = BulletSprite(SHOOTER_BULLET_IMAGE, sprite.coords, (self.width, self.height), Direction.down)
        group.add(bullet)

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
        
        self.direction = Direction.left
        
