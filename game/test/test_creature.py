import pygame
import sys
import unittest
sys.path.insert(0, '../src')
from creature import CreatureSprite
from locals import Direction
from tile import Tile

class TestCreature(unittest.TestCase):

    creature = None
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    BLACK = (0,0,0)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    def setUp(self):
        self.creature = CreatureSprite('Hero.png', (5, 5), (60, 60), Direction.up)
        self.tile = Tile(None, None, (60, 60))

    def test_move_up(self):
        self.creature.move(Direction.up, self.tile)
        self.assertEqual((5, 4), self.creature.coords)

    def test_move_down(self):
        self.creature.move(Direction.down, self.tile)
        self.assertEqual((5, 6), self.creature.coords)

    def test_move_left(self):
        self.creature.move(Direction.left, self.tile)
        self.assertEqual((4, 5), self.creature.coords)

    def test_move_right(self):
        self.creature.move(Direction.right, self.tile)
        self.assertEqual((6, 5), self.creature.coords)

    def test_foreground(self):
        creature = CreatureSprite('Hero.png', (0, 0), (60, 60), Direction.up)
        tile = Tile(None, None, (60, 60))
        tile.height = 2
        tile.width = 2
        tile.background.append([0, 0])
        tile.background.append([0, 0])
        tile.foreground.append([0, 0])
        tile.foreground.append([1, 0])
        tile.top.append([0, 0])
        tile.top.append([0, 0])
        
        creature.move(Direction.right, tile)
        self.assertEqual((0, 0), creature.coords)

        creature.move(Direction.down, tile)
        self.assertEqual((0, 1), creature.coords)

    def test_top_edge(self):
        self.creature.move(Direction.up, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.up, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.up, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.up, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.up, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.up, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.up, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.assertEqual((5, 0), self.creature.coords)

    def test_bottom_edge(self):
        self.creature.move(Direction.down, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.down, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.down, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.down, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.down, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.down, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.down, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.assertEqual((5, 9), self.creature.coords)

    def test_right_edge(self):
        self.creature.move(Direction.right, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.right, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.right, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.right, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.right, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.right, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.right, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.assertEqual((9, 5), self.creature.coords)

    def test_left_edge(self):
        self.creature.move(Direction.left, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.left, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.left, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.left, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.left, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.left, self.tile)
        self.creature.isOutOfBounds(10, 10, -1, -2, -1, -2)
        self.creature.move(Direction.left, self.tile)
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

