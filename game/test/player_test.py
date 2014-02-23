import pygame, math, sys
from pygame.locals import *
sys.path.insert(0, '/home/ian/CS428/cs429/game/src')
import unittest
from player import PlayerSprite

class TestPlayerMovement(unittest.TestCase):

    player = None
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    BLACK = (0,0,0)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    def setUp(self):
        self.player = PlayerSprite('Hero.png', (5, 5))

    def test_move_up(self):
        self.player.up = True
        self.player.update(self.clock.tick(60))
        self.assertEqual((5, 4), self.player.coords)

    def test_move_down(self):
        self.player.down = True
        self.player.update(self.clock.tick(60))
        self.assertEqual((5, 6), self.player.coords)

    def test_move_left(self):
        self.player.left = True
        self.player.update(self.clock.tick(60))
        self.assertEqual((4, 5), self.player.coords)

    def test_move_right(self):
        self.player.right = True
        self.player.update(self.clock.tick(60))
        self.assertEqual((6, 5), self.player.coords)

    def test_top_edge_collision(self):
        self.player.up = True
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.assertEqual((5, 0), self.player.coords)

    def test_bottom_edge_collision(self):
        self.player.down = True
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.assertEqual((5, 9), self.player.coords)

    def test_right_edge_collision(self):
        self.player.right = True
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.assertEqual((9, 5), self.player.coords)

    def test_left_edge_collision(self):
        self.player.left = True
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.player.update(self.clock.tick(60))
        self.assertEqual((0, 5), self.player.coords)

if __name__ == '__main__':
    unittest.main()