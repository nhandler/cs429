import random
from bullet import BulletSprite
from shooter import ShooterSprite
from locals import Direction

class BossSprite (ShooterSprite):

    def __init__(self, image, position, size, direction):
        ShooterSprite.__init__(self, image, position, size, direction)
        self.health = 50

    def act(self, tile):
        i = random.randint(1, 2)

        if self.can_take_action():
            if i == 1: self.direction = Direction.up
            else: self.direction = Direction.down
            self.move(self.direction, tile)

            self.direction = Direction.left

            self.action_taken()
        self.iters_until_action -= 1

    def shoot(self, sprite, group):
    	bullet = BulletSprite('../res/enemy_bullet.png', sprite.coords, (self.width, self.height), Direction.left)
        group.add(bullet)
        bullet = BulletSprite('../res/enemy_bullet.png', sprite.coords, (self.width, self.height), Direction.up)
        group.add(bullet)
        bullet = BulletSprite('../res/enemy_bullet.png', sprite.coords, (self.width, self.height), Direction.down)
        group.add(bullet)

    def handleOutOfBounds(self, px, py, left, right, up, down):
        self.direction = Direction.left
        
