import pygame, math, sys
from pygame.locals import *
sys.path.append('../src')
import unittest
from bullet import BulletSprite, Direction

class TestBulletMovement(unittest.TestCase):

    bullet = None
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    BLACK = (0,0,0)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    def test_move_up(self):
        self.bullet = BulletSprite('bullet.png', (5, 5), Direction.up)
        self.bullet.update()
        self.assertEqual((5, 4), self.bullet.coords)

    def test_move_down(self):
        self.bullet = BulletSprite('bullet.png', (5, 5), Direction.down)
        self.bullet.update()
        self.assertEqual((5, 6), self.bullet.coords)

    def test_move_left(self):
        self.bullet = BulletSprite('bullet.png', (5, 5), Direction.left)
        self.bullet.update()
        self.assertEqual((4, 5), self.bullet.coords)

    def test_move_right(self):
        self.bullet = BulletSprite('bullet.png', (5, 5), Direction.right)
        self.bullet.update()
        self.assertEqual((6, 5), self.bullet.coords)

if __name__ == '__main__':
    unittest.main()