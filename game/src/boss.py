import random
from bullet import BulletSprite
from shooter import ShooterSprite
from locals import Direction, SHOOTER_BULLET_IMAGE, BOSS_IMAGE

class BossSprite (ShooterSprite):

    def __init__(self, position, size, direction):
        ShooterSprite.__init__(self, position, size, direction)
        self._create_spritesheet(BOSS_IMAGE)
        self.health = 50

    def act(self, tile):
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
        (x, y) = self.coords
        i = random.randint(1, 10)

        if x == px and y == py:
            return False
        elif i > 9:
            return True
        else:
            return False

    def shoot(self, sprite, group):
        bullet = BulletSprite(SHOOTER_BULLET_IMAGE, sprite.coords, (self.width, self.height), Direction.left)
        group.add(bullet)
        bullet = BulletSprite(SHOOTER_BULLET_IMAGE, sprite.coords, (self.width, self.height), Direction.up)
        group.add(bullet)
        bullet = BulletSprite(SHOOTER_BULLET_IMAGE, sprite.coords, (self.width, self.height), Direction.down)
        group.add(bullet)

    def handleOutOfBounds(self, px, py, left, right, up, down):
        self.direction = Direction.left
        
