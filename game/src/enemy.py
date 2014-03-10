import pygame
from creature import CreatureSprite
from locals import Direction
from pygame.locals import *

class EnemySprite (CreatureSprite):
    def __init__(self, image, position):
        CreatureSprite.__init__(self, image, position)
        self.direction = Direction.up
        self.health = 3

    def act(self):
        if self.can_take_action():
            self.move(self.direction)

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

    def takeHit(self):
        self.rect = self.image.get_rect()
        self.rect.center = self.convertCoords()
        self.health -= 1
