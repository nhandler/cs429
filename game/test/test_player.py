import pygame
import sys
import unittest
sys.path.insert(0,'../src')
from item import Item, MagicShoes
from locals import Direction
from player import PlayerSprite

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
        pygame.mixer.init()
        self.player = PlayerSprite((5, 5), (60, 60), Direction.down)
        self.item = MagicShoes

    def test_AddItemToInventory(self):
        inventory = self.player.inventory
        current_amount = inventory[self.item]
        self.player.addItemToInventory(self.item)
        self.assertEqual(inventory[self.item], current_amount + 1)

    def test_AddItemToInventoryNone(self):
        item = None
        inventory = self.player.inventory.copy()
        self.player.addItemToInventory(item)
        self.assertEqual(inventory, self.player.inventory)

    def test_finalInventory(self):
        pass
    
    def test_final_condition(self):
        pass

    def test_load(self):
        pass

    def test_save(self):
        pass


if __name__ == '__main__':
    unittest.main()

