import pygame
import sys
import unittest
sys.path.insert(0, '../src')
from bullet import BulletSprite
from locals import Direction

class TestBulletMovement(unittest.TestCase):

    bullet = None
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    BLACK = (0,0,0)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    def test_move_up(self):
        self.bullet = BulletSprite('bullet.png', (5, 5), (60, 60), Direction.up)
        self.bullet.update()
        self.assertEqual((5, 4), self.bullet.coords)

    def test_move_down(self):
        self.bullet = BulletSprite('bullet.png', (5, 5), (60, 60), Direction.down)
        self.bullet.update()
        self.assertEqual((5, 6), self.bullet.coords)

    def test_move_left(self):
        self.bullet = BulletSprite('bullet.png', (5, 5), (60, 60), Direction.left)
        self.bullet.update()
        self.assertEqual((4, 5), self.bullet.coords)

    def test_move_right(self):
        self.bullet = BulletSprite('bullet.png', (5, 5), (60, 60), Direction.right)
        self.bullet.update()
        self.assertEqual((6, 5), self.bullet.coords)

if __name__ == '__main__':
    unittest.main()
