import pygame
from enemy import EnemySprite
from bullet import BulletSprite
from locals import Direction
from pygame.locals import *
import random

class ShooterSprite (EnemySprite):
    def __init__(self, image, position, size):
        EnemySprite.__init__(self, image, position, size)

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
    	bullet = BulletSprite('enemy_bullet.png', sprite.coords, (self.width, self.height), sprite.direction)
        group.add(bullet)
        
