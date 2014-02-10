import pygame, sys
import unittest
from pygame.locals import *
from ..src.gameprimatives.gamestate import GameState
from ..src.menuscene import MenuScene

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestDown('runTest'))
    return test_suite

class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu_scene = MenuScene(['Test One', 'Test Two'])

class TestDown(TestMenu):
    def runTest(self):
        game_state = GameState()
        game_state.events.append(pygame.event.Event(KEYDOWN, key = K_DOWN))
        self.menu_scene.update(game_state)
        self.assertEquals(self.menu_scene.current_item, 1)
