import pygame
import math
import sys
sys.path.append('../src')
import unittest
from locals import Direction
from creature import CreatureSprite

class TestCreature(unittest.TestCase):

    creature = None
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    BLACK = (0,0,0)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    def setUp(self):
        self.creature = CreatureSprite('Hero.png', (5, 5), (60, 60))

    def test_move_up(self):
        self.creature.move(Direction.up);
        self.assertEqual((5, 4), self.creature.coords)

    def test_move_down(self):
        self.creature.move(Direction.down);
        self.assertEqual((5, 6), self.creature.coords)

    def test_move_left(self):
        self.creature.move(Direction.left);
        self.assertEqual((4, 5), self.creature.coords)

    def test_move_right(self):
        self.creature.move(Direction.right);
        self.assertEqual((6, 5), self.creature.coords)

    def test_top_edge(self):
        self.creature.move(Direction.up)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.up)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.up)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.up)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.up)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.up);
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.up)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.assertEqual((5, 0), self.creature.coords)

    def test_bottom_edge(self):
        self.creature.move(Direction.down)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.down)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.down)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.down)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.down)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.down)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.down)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.assertEqual((5, 9), self.creature.coords)

    def test_right_edge(self):
        self.creature.move(Direction.right)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.right)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.right)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.right)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.right)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.right)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.right)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.assertEqual((9, 5), self.creature.coords)

    def test_left_edge(self):
        self.creature.move(Direction.left)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.left)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.left)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.left)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.left)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.left)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.left)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.assertEqual((0, 5), self.creature.coords)

    def test_can_take_action_true(self):
        self.creature.iters_until_action = 0
        self.assertTrue(self.creature.can_take_action())

    def test_can_take_action_false(self):
        self.creature.iters_until_action = 10
        self.assertFalse(self.creature.can_take_action())

    def test_action_taken(self):
        self.creature.action_taken()
        self.assertEqual(self.creature.iters_until_action, 12)


if __name__ == '__main__':
    print "Running creature test"
    unittest.main()
