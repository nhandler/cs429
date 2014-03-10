import pygame, math, sys
from pygame.locals import *
sys.path.append('../src')
import unittest
from player import PlayerSprite, Direction

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
        self.player.move(Direction.up);
        self.assertEqual((5, 4), self.player.coords)

    def test_move_down(self):
        self.player.move(Direction.down);
        self.assertEqual((5, 6), self.player.coords)

    def test_move_left(self):
        self.player.move(Direction.left);
        self.assertEqual((4, 5), self.player.coords)

    def test_move_right(self):
        self.player.move(Direction.right);
        self.assertEqual((6, 5), self.player.coords)

    def test_top_edge_collision(self):
        self.player.move(Direction.up);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.up);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.up);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.up);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.up);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.up);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.up);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.assertEqual((5, 0), self.player.coords)

    def test_bottom_edge_collision(self):
        self.player.move(Direction.down);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.down);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.down);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.down);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.down);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.down);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.down);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.assertEqual((5, 9), self.player.coords)

    def test_right_edge_collision(self):
        self.player.move(Direction.right);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.right);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.right);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.right);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.right);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.right);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.right);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.assertEqual((9, 5), self.player.coords)

    def test_left_edge_collision(self):
        self.player.move(Direction.left);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.left);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.left);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.left);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.left);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.left);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.player.move(Direction.left);
        self.player.isOutOfBounds(10, 10, -1, -2, -1, -2);
        self.assertEqual((0, 5), self.player.coords)

if __name__ == '__main__':
    unittest.main()
