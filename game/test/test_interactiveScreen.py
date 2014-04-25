import pygame
from pygame.locals import *
import sys
import unittest
sys.path.insert(0,'../src')
from interactiveScreen import InteractiveScreen

class MockEvent():
    key = None
    type = None
    def __init__(self, key, type):
        self.key = key
        self.type = type

class TestInteractiveScreen(unittest.TestCase):

    intScreen = None

    def setUp(self):
        pygame.mixer.init()
        self.intScreen = InteractiveScreen()
        self.intScreen.lines = ['Test1', 'Test2']
    
    def test_InteractUpDn(self):
        curr = self.intScreen.currLine
        self.intScreen.interact(MockEvent(K_w, KEYDOWN))
        self.assertEqual(curr, self.intScreen.currLine)
        
        self.intScreen.interact(MockEvent(K_s, KEYDOWN))
        self.assertEqual(curr + 1, self.intScreen.currLine)
        
        self.intScreen.interact(MockEvent(K_s, KEYDOWN))
        self.assertEqual(curr + 1, self.intScreen.currLine)

        self.intScreen.interact(MockEvent(K_w, KEYDOWN))
        self.assertEqual(curr, self.intScreen.currLine)

if __name__ == '__main__':
    unittest.main()
