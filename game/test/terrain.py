from lettuce import world
import pygame
import sys
import unittest
sys.path.insert(0,'../src')
from creature import CreatureSprite
from locals import Direction
from tile import Tile

@world.absorb
class TestCreature():

    creature = None
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    BLACK = (0,0,0)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)
