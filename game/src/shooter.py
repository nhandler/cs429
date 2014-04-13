import random
from bullet import BulletSprite
from enemy import EnemySprite
from locals import SHOOTER_BULLET_IMAGE, SHOOTER_IMAGE

class ShooterSprite (EnemySprite):
    def __init__(self, position, size, direction):
        EnemySprite.__init__(self, position, size, direction)
        self._create_spritesheet(SHOOTER_IMAGE)

    def shouldShoot(self, px, py):
        (x, y) = self.coords
        i = random.randint(1, 10)

        if x == px and y == py:
            return False
        elif i > 9 and (x == px or y == py):
            return True
        else:
            return False

    def shoot(self, sprite, group):
    	bullet = BulletSprite(SHOOTER_BULLET_IMAGE, sprite.coords, (self.width, self.height), sprite.direction)
        group.add(bullet)
        
