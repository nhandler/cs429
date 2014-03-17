import pygame
from enemy import EnemySprite
from bullet import BulletSprite
from locals import Direction
from pygame.locals import *
import random

class ShooterSprite (EnemySprite):
    def __init__(self, image, position, size):
        EnemySprite.__init__(self, image, position, size)

    def shouldShoot(self):
    	i = random.randint(1, 10)
        n = random.randint(1, 10)
        if i == n: return True
        else: return False

    def shoot(self, sprite, group):
    	bullet = BulletSprite('enemy_bullet.png', sprite.coords, (60, 60), sprite.direction)
        group.add(bullet)
        