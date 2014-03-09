import pygame
from creature import CreatureSprite, HorizontalMovement, VerticalMovement, Direction
from pygame.locals import *

class EnemySprite (CreatureSprite):
    def __init__(self, image, position):
        CreatureSprite.__init__(self, image, position)
        self.verticalMovement = VerticalMovement.up

    def changeVerticalMovementOpposite(self):
        if self.verticalMovement == VerticalMovement.up:
            self.verticalMovement = VerticalMovement.down
        else:
            self.verticalMovement = VerticalMovement.up

    def takeHit(self):
        self.rect = self.image.get_rect()
        self.rect.center = self.position
