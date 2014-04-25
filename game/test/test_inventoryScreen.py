import pygame
from pygame.locals import *
import sys
import unittest
sys.path.insert(0,'../src')
from inventoryScreen import InventoryScreen
from player import PlayerSprite
from state import State

class MockEvent():
    key = None
    type = None
    def __init__(self, key, type):
        self.key = key
        self.type = type

class MockItem():
    used = False
    def use(self, player):
        self.used = True

class TestInventoryScreen(unittest.TestCase):

    invScreen = None
    player = None
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    BLACK = (0,0,0)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    def setUp(self):
        pygame.mixer.init()
        self.player = PlayerSprite()
        self.invScreen = InventoryScreen(self.player)
        self.invScreen.lines = ['Test1', 'Test2']
        State.screens = []
        State.push_screen(self.invScreen)

    def test_InteractUpDn(self):
        curr = self.invScreen.currLine
        self.invScreen.update([MockEvent(K_w, KEYDOWN)])
        self.assertEqual(curr, self.invScreen.currLine)
        
        self.invScreen.update([MockEvent(K_s, KEYDOWN)])
        self.assertEqual(curr + 1, self.invScreen.currLine)
        
        self.invScreen.update([MockEvent(K_s, KEYDOWN)])
        self.assertEqual(curr + 1, self.invScreen.currLine)

        self.invScreen.update([MockEvent(K_w, KEYDOWN)])
        self.assertEqual(curr, self.invScreen.currLine)

    def test_InventoryState(self):
        self.invScreen.update([MockEvent(K_i, KEYDOWN)])
        self.assertEqual(State.screens, [])

    def test_InventoryUse(self):
        self.player.inventory = {}
        item = MockItem()
        self.player.inventory[item] = 1

        self.invScreen.update([MockEvent(K_RETURN, KEYDOWN)])
        count = self.player.inventory[item]
        self.assertEqual(count, 0)
        self.assertTrue(item.used)
        
        self.player.inventory = {}
        item = MockItem()
        self.player.inventory[item] = 0

        self.invScreen.update([MockEvent(K_RETURN, KEYDOWN)])
        count = self.player.inventory[item]
        self.assertEqual(count, 0)
        self.assertFalse(item.used)

if __name__ == '__main__':
    unittest.main()
