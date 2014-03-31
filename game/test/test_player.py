import pygame, math, sys
from pygame.locals import *
sys.path.append('../src')
import unittest
from player import PlayerSprite, Direction
from item import Item, MagicShoes

class TestPlayer(unittest.TestCase):

    player = None
    item = None
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    BLACK = (0,0,0)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    def setUp(self):
        self.player = PlayerSprite('Hero.png', (5, 5), (60, 60), Direction.down)
        self.item = MagicShoes()

    def test_AddItemToInventory(self):
        self.player.addItemToInventory(self.item)
        inventory = self.player.inventory
        self.assertEqual(inventory["Magic Shoes"], self.item.type)

if __name__ == '__main__':
    unittest.main()

