import pygame
import math 
import sys
from pygame.locals import *
sys.path.append('../src')
import unittest
from enemy import EnemySprite, Direction, HorizontalMovement, VerticalMovement

class TestEnemy(unittest.TestCase):
    enemy = None
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    BLACK = (0,0,0)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    def setUp(self):
        self.enemy = EnemySprite('enemy.png', (5, 5))

    def test_changeDirectionDown(self):
        self.enemy.verticalMovement = VerticalMovement.up

        self.enemy.changeVerticalMovementOpposite()

        self.assertEqual(self.enemy.verticalMovement, VerticalMovement.down)

    def test_change_direction_up(self):
        self.enemy.verticalMovement = VerticalMovement.down

        self.enemy.changeVerticalMovementOpposite()

        self.assertEqual(self.enemy.verticalMovement, VerticalMovement.up)


if __name__ == '__main__':
    unittest.main()
